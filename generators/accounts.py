import random
import string

class AccountGenerator:
    @staticmethod
    def generate():
        prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 8)))
        num = random.randint(80, 99)
        
        return [
            {"type": "com.google", "name": f"{prefix}{num}@gmail.com"},
            {"type": "com.github", "name": f"{prefix}_dev"},
            {"type": "com.exchange.cryptocurrency", "name": f"{prefix}{num}@protonmail.com"}
        ]
