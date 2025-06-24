import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def handle_missing_values(df: pd.DataFrame, strategy: str = 'interpolate') -> pd.DataFrame:
    """
    Gère les valeurs manquantes dans un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame d'entrée.
        strategy (str): Stratégie de gestion des valeurs manquantes ('interpolate', 'drop', 'fill_zero', 'fill_mean').

    Returns:
        pd.DataFrame: DataFrame avec les valeurs manquantes gérées.
    """
    df_cleaned = df.copy()
    if strategy == 'interpolate':
        df_cleaned = df_cleaned.interpolate(method='time', limit_direction='both')
        logger.info("Valeurs manquantes interpolées.")
    elif strategy == 'drop':
        df_cleaned = df_cleaned.dropna()
        logger.info("Lignes avec valeurs manquantes supprimées.")
    elif strategy == 'fill_zero':
        df_cleaned = df_cleaned.fillna(0)
        logger.info("Valeurs manquantes remplies avec zéro.")
    elif strategy == 'fill_mean':
        df_cleaned = df_cleaned.fillna(df_cleaned.mean(numeric_only=True))
        logger.info("Valeurs manquantes remplies avec la moyenne.")
    else:
        logger.warning(f"Stratégie de gestion des valeurs manquantes '{strategy}' non reconnue. Aucune action effectuée.")
    return df_cleaned

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les lignes dupliquées d'un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame d'entrée.

    Returns:
        pd.DataFrame: DataFrame sans les lignes dupliquées.
    """
    initial_rows = len(df)
    df_cleaned = df.drop_duplicates()
    if len(df_cleaned) < initial_rows:
        logger.info(f"{initial_rows - len(df_cleaned)} lignes dupliquées supprimées.")
    else:
        logger.info("Aucune ligne dupliquée trouvée.")
    return df_cleaned


