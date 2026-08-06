import random

class GPSGenerator:
    @staticmethod
    def generate():
        # Generate random coordinates (excluding extreme poles for realism)
        lat = random.uniform(-60.0, 70.0)
        lon = random.uniform(-180.0, 180.0)
        altitude = random.uniform(0.0, 3000.0) # Meters
        speed = random.uniform(0.0, 25.0) # Meters per second (simulating driving/walking)
        
        return {
            "Latitude": round(lat, 6),
            "Longitude": round(lon, 6),
            "Altitude (m)": round(altitude, 2),
            "Speed (m/s)": round(speed, 2),
            "GPS Accuracy": random.choice(["High", "Medium", "Low"])
        }
