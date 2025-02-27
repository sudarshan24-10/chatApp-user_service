import logging
import os

LOG_FILE = "logs/app.log"
LOG_LEVEL = logging.DEBUG if os.getenv("DEBUG") == "True" else logging.INFO

def setup_logging():
    """Sets up logging configuration."""
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        filename=LOG_FILE,
        level=LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logging.getLogger().addHandler(console_handler)

    logging.info("Logging setup complete.")
