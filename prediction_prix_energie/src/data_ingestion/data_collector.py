import refinitiv.data as rd
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def initialize_refinitiv_session():
    """
    Initialise la session Refinitiv Data Platform.
    Nécessite que les variables d'environnement RDP_APP_KEY et RDP_USERNAME soient configurées.
    """
    try:
        rd.open_session()
        logger.info("Session Refinitiv Data Platform initialisée avec succès.")
    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation de la session Refinitiv: {e}")
        raise

def close_refinitiv_session():
    """
    Ferme la session Refinitiv Data Platform.
    """
    try:
        rd.close_session()
        logger.info("Session Refinitiv Data Platform fermée.")
    except Exception as e:
        logger.error(f"Erreur lors de la fermeture de la session Refinitiv: {e}")
        raise

def get_historical_timeseries(ric: str, start_date: str, end_date: str, interval: str = 'daily') -> pd.DataFrame:
    """
    Récupère les séries temporelles historiques pour un RIC donné.

    Args:
        ric (str): Le RIC (Refinitiv Instrument Code) de l'actif.
        start_date (str): Date de début au format 'YYYY-MM-DD'.
        end_date (str): Date de fin au format 'YYYY-MM-DD'.
        interval (str): Intervalle des données ('daily', 'hourly', etc.).

    Returns:
        pd.DataFrame: DataFrame contenant les données historiques.
    """
    try:
        df = rd.get_history(rics=ric, fields=['TRDPRC_1', 'OPEN_PRC', 'HIGH_PRC', 'LOW_PRC', 'VOL_1D'],
                            start=start_date, end=end_date, interval=interval)
        df.index.name = 'Date'
        df.columns = ['Close', 'Open', 'High', 'Low', 'Volume']
        logger.info(f"Données historiques pour {ric} récupérées avec succès.")
        return df
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données historiques pour {ric}: {e}")
        return pd.DataFrame()

def get_weather_forecast_data(city: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Récupère des données météorologiques (exemple fictif, à remplacer par une API réelle).

    Args:
        city (str): Nom de la ville.
        start_date (str): Date de début.
        end_date (str): Date de fin.

    Returns:
        pd.DataFrame: DataFrame contenant des données météorologiques simulées.
    """
    logger.warning("Utilisation de données météorologiques simulées. Intégrez une API météo réelle pour la production.")
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    data = {
        'temperature': np.random.uniform(5, 30, len(dates)),
        'humidity': np.random.uniform(40, 90, len(dates))
    }
    df_weather = pd.DataFrame(data, index=dates)
    df_weather.index.name = 'Date'
    logger.info(f"Données météorologiques simulées pour {city} générées.")
    return df_weather


