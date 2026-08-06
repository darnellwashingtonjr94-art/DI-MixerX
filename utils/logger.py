import logging
from config import LOG_FILE

class TrapLogger:
    def __init__(self):
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - DI-MixerX - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def info(self, message):
        self.logger.info(message)
        print(f"[*] {message}")
