import json
import os
from config import OUTPUT_DIR, OUTPUT_FILE

class ProfileExporter:
    def __init__(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def save_to_json(self, data):
        filepath = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return filepath
