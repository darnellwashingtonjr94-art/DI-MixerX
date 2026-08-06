import json
import os

class ConfigLoader:
    @staticmethod
    def load(filepath="config/settings.json"):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Missing configuration file at {filepath}")
            
        with open(filepath, 'r') as f:
            try:
                config = json.load(f)
                return config
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format in configuration file.")
