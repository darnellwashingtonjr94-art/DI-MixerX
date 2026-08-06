import random

class IPGenerator:
    @staticmethod
    def generate_ipv4():
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}." \
               f"{random.randint(0, 255)}.{random.randint(1, 255)}"

    @staticmethod
    def generate_ipv6():
        return ':'.join('{:x}'.format(random.randint(0, 2**16 - 1)) for _ in range(8))
