import os

# Trap Configuration
OUTPUT_DIR = os.path.join(os.getcwd(), "data")
OUTPUT_FILE = "fake_confidentials.json"
LOG_FILE = "trap_access.log"

# Spoofing Parameters
INCLUDE_IPV6 = False
ANDROID_VERSIONS = ["9", "10", "11", "12", "13", "14"]
