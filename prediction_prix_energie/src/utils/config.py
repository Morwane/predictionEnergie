import os

class Config:
    """
    Classe de configuration pour le projet de prédiction de prix de l'énergie.
    """
    # Chemins des données
    RAW_DATA_PATH = os.path.join("data", "raw", "energy_prices.csv")
    PROCESSED_DATA_PATH = os.path.join("data", "processed", "processed_energy_data.csv")

    # Paramètres Refinitiv (à configurer dans un fichier .env ou variables d'environnement)
    RDP_APP_KEY = os.getenv("RDP_APP_KEY")
    RDP_USERNAME = os.getenv("RDP_USERNAME")

    # RICs pour les prix de l'énergie (exemples, à adapter)
    ELECTRICITY_RIC = "EEX_PHEL_DA_BASE_DE-FR_MWH"
    GAS_RIC = "TTF_GAS_DA_EUR_MWH"

    # Période de données
    START_DATE = "2020-01-01"
    END_DATE = "2023-12-31"

    # Paramètres de modélisation
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    TARGET_COLUMN = "Close"

    # Paramètres de logging
    LOG_FILE = "app.log"
    LOG_LEVEL = "INFO"


