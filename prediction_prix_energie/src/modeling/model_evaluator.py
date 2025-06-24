from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import numpy as np
import logging

logger = logging.getLogger(__name__)

def evaluate_regression_model(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """
    Évalue les performances d'un modèle de régression.

    Args:
        y_true (np.ndarray): Valeurs réelles.
        y_pred (np.ndarray): Valeurs prédites.

    Returns:
        dict: Dictionnaire contenant les métriques d'évaluation (RMSE, MAE, MAPE).
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100

    metrics = {
        "RMSE": rmse,
        "MAE": mae,
        "MAPE": mape
    }
    logger.info(f"Métriques d'évaluation: RMSE={rmse:.2f}, MAE={mae:.2f}, MAPE={mape:.2f}%")
    return metrics


