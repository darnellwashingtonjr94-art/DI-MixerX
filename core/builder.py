import random
from generators.ip import IPGenerator
from generators.mac import MACGenerator
from generators.uptime import UptimeGenerator
from generators.build import BuildGenerator

class ProfileBuilder:
    def build_profile(self):
        return {
            "IP address": random.choice([IPGenerator.generate_ipv4(), "Unavailable"]),
            "Wi-Fi MAC address": "To view, choose saved network",
            "Device Wi-Fi MAC address": MACGenerator.generate(),
            "Bluetooth address": random.choice([MACGenerator.generate(), "Unavailable"]),
            "Uptime": UptimeGenerator.generate(),
            "Build number": BuildGenerator.generate()
        }
