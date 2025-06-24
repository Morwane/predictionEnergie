import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def create_lag_features(df: pd.DataFrame, column: str, lags: list) -> pd.DataFrame:
    """
    Crée des variables de décalage (lag features) pour une colonne donnée.

    Args:
        df (pd.DataFrame): DataFrame d'entrée.
        column (str): Nom de la colonne pour laquelle créer les lags.
        lags (list): Liste des décalages à appliquer (ex: [1, 7, 24]).

    Returns:
        pd.DataFrame: DataFrame avec les nouvelles colonnes de lags.
    """
    df_lagged = df.copy()
    for lag in lags:
        df_lagged[f'{column}_lag_{lag}'] = df_lagged[column].shift(lag)
        logger.info(f"Création de la variable de décalage {column}_lag_{lag}.")
    return df_lagged

def create_rolling_features(df: pd.DataFrame, column: str, windows: list, aggregations: list) -> pd.DataFrame:
    """
    Crée des variables de fenêtre glissante (rolling features) pour une colonne donnée.

    Args:
        df (pd.DataFrame): DataFrame d'entrée.
        column (str): Nom de la colonne pour laquelle créer les rolling features.
        windows (list): Liste des tailles de fenêtre (ex: [24, 48, 168]).
        aggregations (list): Liste des fonctions d'agrégation (ex: ['mean', 'std', 'min', 'max']).

    Returns:
        pd.DataFrame: DataFrame avec les nouvelles colonnes de rolling features.
    """
    df_rolled = df.copy()
    for window in windows:
        for agg in aggregations:
            df_rolled[f'{column}_rolling_{window}_{agg}'] = df_rolled[column].rolling(window=window).agg(agg)
            logger.info(f"Création de la variable de fenêtre glissante {column}_rolling_{window}_{agg}.")
    return df_rolled

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crée des variables temporelles à partir de l'index datetime du DataFrame.

    Args:
        df (pd.DataFrame): DataFrame d'entrée avec un index datetime.

    Returns:
        pd.DataFrame: DataFrame avec les nouvelles colonnes temporelles.
    """
    df_time_features = df.copy()
    if not isinstance(df_time_features.index, pd.DatetimeIndex):
        logger.error("L'index du DataFrame doit être de type DatetimeIndex pour créer des variables temporelles.")
        return df_time_features

    df_time_features['hour'] = df_time_features.index.hour
    df_time_features['day_of_week'] = df_time_features.index.dayofweek
    df_time_features['day_of_year'] = df_time_features.index.dayofyear
    df_time_features['month'] = df_time_features.index.month
    df_time_features['year'] = df_time_features.index.year
    df_time_features['quarter'] = df_time_features.index.quarter
    df_time_features['is_weekend'] = (df_time_features.index.dayofweek >= 5).astype(int)
    df_time_features['week_of_year'] = df_time_features.index.isocalendar().week.astype(int)

    logger.info("Variables temporelles créées (heure, jour de la semaine, jour de l'année, mois, année, trimestre, week-end, semaine de l'année).")
    return df_time_features


