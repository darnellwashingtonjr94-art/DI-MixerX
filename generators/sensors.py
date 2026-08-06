import random

class SensorGenerator:
    @staticmethod
    def generate():
        # Simulate slight hand tremors or movement
        return {
            "Accelerometer": {
                "x": round(random.uniform(-0.5, 0.5), 4),
                "y": round(random.uniform(9.5, 10.0), 4), # Gravity effect
                "z": round(random.uniform(-0.5, 0.5), 4)
            },
            "Gyroscope": {
                "x": round(random.uniform(-0.1, 0.1), 4),
                "y": round(random.uniform(-0.1, 0.1), 4),
                "z": round(random.uniform(-0.1, 0.1), 4)
            }
        }
