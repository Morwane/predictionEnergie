import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_data_from_csv(file_path: str) -> pd.DataFrame:
    """
    Charge les données depuis un fichier CSV.

    Args:
        file_path (str): Chemin d'accès au fichier CSV.

    Returns:
        pd.DataFrame: DataFrame contenant les données chargées.
    """
    try:
        df = pd.read_csv(file_path, index_col=\'Date\', parse_dates=True)
        logger.info(f"Données chargées depuis {file_path} avec succès.")
        return df
    except FileNotFoundError:
        logger.error(f"Fichier non trouvé: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Erreur lors du chargement du fichier CSV {file_path}: {e}")
        return pd.DataFrame()


