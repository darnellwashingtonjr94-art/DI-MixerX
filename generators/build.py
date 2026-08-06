import random
import string
from config import ANDROID_VERSIONS

class BuildGenerator:
    @staticmethod
    def generate():
        prefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        part2 = random.randint(10, 99)
        part3 = random.randint(10, 99)
        part4 = random.randint(100, 999)
        version = random.choice(ANDROID_VERSIONS)
        return f"{prefix}{part2}.{part3}-{part4}-{version}-{random.randint(1, 9)}"
