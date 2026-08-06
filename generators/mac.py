import random

class MACGenerator:
    @staticmethod
    def generate():
        mac = [random.randint(0, 255) for _ in range(6)]
        # Ensure the first byte is even (unicast) and not locally administered
        mac[0] = (mac[0] & 0xfc) 
        return ':'.join(f"{b:02x}" for b in mac)
