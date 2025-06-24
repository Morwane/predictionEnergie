import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import logging

logger = logging.getLogger(__name__)

def train_xgboost_model(X_train, y_train, params=None) -> xgb.Booster:
    """
    Entraîne un modèle XGBoost.

    Args:
        X_train (pd.DataFrame): Caractéristiques d'entraînement.
        y_train (pd.Series): Cible d'entraînement.
        params (dict, optional): Paramètres XGBoost. Defaults to None.

    Returns:
        xgb.Booster: Modèle XGBoost entraîné.
    """
    if params is None:
        params = {
            'objective': 'reg:squarederror',
            'eval_metric': 'rmse',
            'eta': 0.01,
            'max_depth': 6,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'seed': 42
        }

    dtrain = xgb.DMatrix(X_train, label=y_train)
    model = xgb.train(params, dtrain, num_boost_round=1000)
    logger.info("Modèle XGBoost entraîné avec succès.")
    return model

def save_model(model, path: str):
    """
    Sauvegarde un modèle entraîné.

    Args:
        model: Le modèle à sauvegarder.
        path (str): Chemin où sauvegarder le modèle.
    """
    joblib.dump(model, path)
    logger.info(f"Modèle sauvegardé à {path}.")

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


