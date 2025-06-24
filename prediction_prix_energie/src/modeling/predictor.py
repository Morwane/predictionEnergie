import xgboost as xgb
import pandas as pd
import logging
import joblib

logger = logging.getLogger(__name__)

def predict_prices(model: xgb.Booster, X_test: pd.DataFrame) -> pd.Series:
    """
    Génère des prédictions de prix à partir d'un modèle XGBoost entraîné.

    Args:
        model (xgb.Booster): Le modèle XGBoost entraîné.
        X_test (pd.DataFrame): Les caractéristiques pour lesquelles faire des prédictions.

    Returns:
        pd.Series: Les prédictions de prix.
    """
    dtest = xgb.DMatrix(X_test)
    predictions = model.predict(dtest)
    logger.info("Prédictions générées avec succès.")
    return pd.Series(predictions, index=X_test.index)


def load_model(path: str):
    """
    Charge un modèle sauvegardé.

    Args:
        path (str): Chemin du modèle à charger.

    Returns:
        model: Le modèle chargé.
    """
    model = joblib.load(path)
    logger.info(f"Modèle chargé depuis {path}.")
    return model


