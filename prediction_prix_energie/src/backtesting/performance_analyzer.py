import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def calculate_backtest_metrics(simulation_df: pd.DataFrame) -> dict:
    """
    Calcule les métriques de performance pour le backtest.

    Args:
        simulation_df (pd.DataFrame): DataFrame de simulation avec les colonnes 'actual_price', 'predicted_price', 'PnL'.

    Returns:
        dict: Dictionnaire des métriques de backtest (Profit Total, Nombre de Trades, Taux de Succès).
    """
    total_pnl = simulation_df["PnL"].sum()
    num_trades = simulation_df[simulation_df["PnL"] != 0].shape[0]
    successful_trades = simulation_df[simulation_df["PnL"] > 0].shape[0]
    success_rate = (successful_trades / num_trades) * 100 if num_trades > 0 else 0

    metrics = {
        "Total PnL": total_pnl,
        "Number of Trades": num_trades,
        "Success Rate (%)": success_rate
    }
    logger.info(f"Métriques de backtest calculées: Total PnL={total_pnl:.2f}, Nombre de Trades={num_trades}, Taux de Succès={success_rate:.2f}%")
    return metrics


