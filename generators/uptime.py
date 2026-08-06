import random

class UptimeGenerator:
    @staticmethod
    def generate():
        hours = random.randint(0, 720) # Up to 30 days
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
