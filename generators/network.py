import random

class NetworkGenerator:
    CARRIERS = [
        {"name": "Verizon", "mcc": "310", "mnc": "012"},
        {"name": "AT&T", "mcc": "310", "mnc": "410"},
        {"name": "T-Mobile", "mcc": "310", "mnc": "260"},
        {"name": "Vodafone", "mcc": "234", "mnc": "15"}
    ]

    @staticmethod
    def generate():
        carrier = random.choice(NetworkGenerator.CARRIERS)
        return {
            "Carrier": carrier["name"],
            "MCC": carrier["mcc"],
            "MNC": carrier["mnc"],
            "Signal Strength": f"-{random.randint(70, 110)} dBm"
        }
