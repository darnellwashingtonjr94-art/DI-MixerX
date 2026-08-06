import random

class ClipboardGenerator:
    @staticmethod
    def generate():
        baits = [
            "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", # Fake Bitcoin address
            "0x71C7656EC7ab88b098defB751B7401B5f6d8976F", # Fake Monad/EVM address
            "export HFT_API_KEY='ak_live_8f93nd83jdhx82ndb'", # Fake API key
            "https://rpc.monad.xyz/v1/node/auth?token=temp_992", # Fake RPC endpoint
            "Password123!@#" # Generic fake password
        ]
        return {
            "last_copied_text": random.choice(baits),
            "timestamp": "Just now"
        }
