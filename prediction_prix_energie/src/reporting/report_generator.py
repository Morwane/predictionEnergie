import pandas as pd
import logging

logger = logging.getLogger(__name__)

def generate_performance_report(metrics: dict, output_path: str = "reports/performance_report.txt"):
    """
    Génère un rapport de performance simple.

    Args:
        metrics (dict): Dictionnaire des métriques de performance.
        output_path (str): Chemin où sauvegarder le rapport.
    """
    with open(output_path, "w") as f:
        f.write("--- Rapport de Performance du Modèle ---\n")
        for key, value in metrics.items():
            f.write(f"{key}: {value:.2f}\n")
    logger.info(f"Rapport de performance sauvegardé à {output_path}.")


