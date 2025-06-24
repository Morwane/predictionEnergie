import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def plot_predictions(actual_prices: pd.Series, predicted_prices: pd.Series, title: str = "Prédictions vs Réalité"):
    """
    Trace les prix réels et les prix prédits.

    Args:
        actual_prices (pd.Series): Série des prix réels.
        predicted_prices (pd.Series): Série des prix prédits.
        title (str): Titre du graphique.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(actual_prices.index, actual_prices, label=\'Prix Réels\', color=\'blue\')
    plt.plot(predicted_prices.index, predicted_prices, label=\'Prix Prédits\', color=\'red\', linestyle=\'--\')
    plt.title(title)
    plt.xlabel(\'Date\')
    plt.ylabel(\'Prix\')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"reports/{title.replace(\' \', \'_\').lower()}.png")
    plt.close()
    logger.info(f"Graphique \'{title}\' sauvegardé.")

def plot_feature_importance(feature_importances: pd.Series, title: str = "Importance des Caractéristiques"):
    """
    Trace l\'importance des caractéristiques.

    Args:
        feature_importances (pd.Series): Série des importances des caractéristiques.
        title (str): Titre du graphique.
    """
    plt.figure(figsize=(10, 8))
    sns.barplot(x=feature_importances.values, y=feature_importances.index)
    plt.title(title)
    plt.xlabel(\'Importance\')
    plt.ylabel(\'Caractéristique\')
    plt.tight_layout()
    plt.savefig(f"reports/{title.replace(\' \', \'_\').lower()}.png")
    plt.close()
    logger.info(f"Graphique \'{title}\' sauvegardé.")


