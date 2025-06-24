import logging
import os

def setup_logging(log_file=\'app.log\', level=logging.INFO):
    """
    Configure le système de logging.

    Args:
        log_file (str): Nom du fichier de log.
        level (int): Niveau de logging (e.g., logging.INFO, logging.DEBUG).
    """
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \'..\', \'..\', \'logs\')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    logging.basicConfig(
        level=level,
        format=\'%(asctime)s - %(name)s - %(levelname)s - %(message)s\',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )
    logging.info(f"Logging configuré. Les logs sont enregistrés dans {log_path}")


