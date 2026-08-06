import random
import string

class SerialGenerator:
    @staticmethod
    def generate(length=12):
        """Generates a random hardware serial number."""
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=length))
