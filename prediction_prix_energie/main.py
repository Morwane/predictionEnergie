import pandas as pd
import numpy as np
import logging
import os
from dotenv import load_dotenv

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Charger les variables d'environnement
load_dotenv()

# Importer les modules du projet
from src.data_ingestion.data_collector import initialize_refinitiv_session, close_refinitiv_session, get_historical_timeseries, get_weather_forecast_data
from src.data_preprocessing.cleaner import handle_missing_values, remove_duplicates
from src.data_preprocessing.feature_engineer import create_time_features, create_lag_features, create_rolling_features, add_technical_indicators
from src.modeling.model_trainer import train_xgboost_model, save_model, load_model
from src.modeling.model_evaluator import evaluate_model
from src.modeling.predictor import make_predictions
from src.backtesting.strategy_simulator import simulate_hedging_strategy
from src.backtesting.performance_analyzer import calculate_pnl, calculate_backtest_metrics
from src.reporting.visualizer import plot_predictions_vs_actual, plot_feature_importance, plot_cumulative_pnl
from src.reporting.report_generator import generate_price_prediction_report

def run_price_prediction_project():
    logger.info("Démarrage du projet de prédiction des prix de l'énergie.")

    # --- 1. Collecte et Chargement des Données ---
    try:
        initialize_refinitiv_session()
        electricity_ric = os.getenv('ELECTRICITY_RIC', 'EEX_EL_BASE_DE_DA') # RIC conceptuel
        gas_ric = os.getenv('GAS_RIC', 'TTF_DA') # RIC conceptuel
        start_date = os.getenv('START_DATE', '2022-01-01')
        end_date = os.getenv('END_DATE', '2023-12-31')

        df_electricity = get_historical_timeseries(electricity_ric, start_date, end_date, interval='daily')
        df_gas = get_historical_timeseries(gas_ric, start_date, end_date, interval='daily')
        df_weather = get_weather_forecast_data('Paris', start_date, end_date) # Données fictives

        if df_electricity.empty or df_gas.empty or df_weather.empty:
            logger.error("Impossible de récupérer toutes les données nécessaires. Arrêt du projet.")
            return

        # Fusionner les données (exemple simple, à adapter)
        df_merged = df_electricity.rename(columns={'Close': 'electricity_price'}).drop(columns=['Open', 'High', 'Low', 'Volume'])
        df_merged['gas_price'] = df_gas['Close']
        df_merged = df_merged.merge(df_weather[['temperature']], left_index=True, right_index=True, how='left')

    except Exception as e:
        logger.error(f"Erreur lors de la collecte des données: {e}")
        return
    finally:
        close_refinitiv_session()

    # --- 2. Préparation et Feature Engineering ---
    logger.info("Démarrage de la préparation des données et du feature engineering.")
    df_cleaned = handle_missing_values(df_merged, strategy='interpolate')
    df_cleaned = remove_duplicates(df_cleaned)

    df_features = create_time_features(df_cleaned.reset_index(), date_column='Date').set_index('Date')
    df_features = create_lag_features(df_features, 'electricity_price', lags=[1, 7])
    df_features = create_rolling_features(df_features, 'electricity_price', windows=[7, 30], aggregations=['mean', 'std'])
    df_features = add_technical_indicators(df_features, price_column='electricity_price')

    # Définir les caractéristiques et la cible
    target_column = 'electricity_price'
    features = [col for col in df_features.columns if col not in [target_column, 'gas_price'] and df_features[col].dtype != 'object']
    
    # Supprimer les lignes avec NaN résultant des lags/rolling features
    df_final = df_features.dropna(subset=features + [target_column])

    X = df_final[features]
    y = df_final[target_column]

    # Séparer les données en entraînement et test (respecter l'ordre temporel)
    train_size = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
    y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

    # --- 3. Modélisation ---
    logger.info("Démarrage de la modélisation.")
    model_path = 'models/xgboost_price_model.joblib'
    
    # Entraînement du modèle
    best_xgboost_model = train_xgboost_model(X_train, y_train)
    save_model(best_xgboost_model, model_path)

    # --- 4. Prédiction ---
    logger.info("Génération des prédictions.")
    y_pred = make_predictions(best_xgboost_model, X_test)

    # --- 5. Évaluation du Modèle ---
    logger.info("Évaluation du modèle.")
    model_metrics = evaluate_model(y_test, y_pred)

    # --- 6. Backtest ---
    logger.info("Démarrage du backtest.")
    simulation_results = simulate_hedging_strategy(y_test, y_pred)
    pnl_df = calculate_pnl(simulation_results['cost_strategy'], simulation_results['cost_benchmark'])
    backtest_metrics = calculate_backtest_metrics(pnl_df['daily_pnl'])

    # --- 7. Visualisation et Rapport ---
    logger.info("Génération des visualisations et du rapport.")
    reports_dir = 'reports'
    os.makedirs(reports_dir, exist_ok=True)

    plot_predictions_vs_actual(y_test, y_pred, 'Prédictions vs Réalité des Prix de l\'Électricité', 
                               os.path.join(reports_dir, 'predictions_vs_actual.png'))
    
    # Feature importance (nécessite un modèle qui expose feature_importances_)
    if hasattr(best_xgboost_model, 'feature_importances_'):
        feature_importances = pd.Series(best_xgboost_model.feature_importances_, index=X_train.columns)
        plot_feature_importance(feature_importances, 'Importance des Caractéristiques', 
                                os.path.join(reports_dir, 'feature_importance.png'))

    plot_cumulative_pnl(pnl_df['cumulative_pnl'], 'PnL Cumulé de la Stratégie de Hedging', 
                        os.path.join(reports_dir, 'cumulative_pnl.png'))

    generate_price_prediction_report(model_metrics, backtest_metrics, 
                                     os.path.join(reports_dir, 'price_prediction_report.md'))

    logger.info("Projet de prédiction des prix de l'énergie terminé.")

if __name__ == "__main__":
    run_price_prediction_project()


