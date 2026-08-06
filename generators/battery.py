import random

class BatteryGenerator:
    @staticmethod
    def generate():
        is_charging = random.choice([True, False])
        level = random.randint(12, 100)
        temp = random.uniform(25.0, 42.0) # Celsius
        voltage = random.uniform(3.7, 4.3)
        
        return {
            "Battery Level": f"{level}%",
            "Charging": is_charging,
            "Power Source": "AC" if is_charging else "Battery",
            "Temperature": f"{round(temp, 1)} °C",
            "Voltage": f"{round(voltage, 2)} V",
            "Health": random.choice(["Good", "Good", "Excellent", "Fair"])
        }
