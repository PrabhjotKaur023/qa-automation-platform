import logging
import os

def get_logger():

    logs_dir = "reports/logs"
    os.makedirs(logs_dir, exist_ok=True)

    logger = logging.getLogger("QA_Automation")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "reports/logs/test_execution.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger