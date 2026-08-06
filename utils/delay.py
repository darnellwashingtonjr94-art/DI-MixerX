import time
import random

class TarpitDelay:
    @staticmethod
    def apply_jitter(min_seconds=0.5, max_seconds=3.5):
        """Pauses execution to simulate slow server response and waste attacker time."""
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
        return delay
