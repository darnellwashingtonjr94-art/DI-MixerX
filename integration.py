from core.builder import ProfileBuilder
from generators.processes import ProcessGenerator
from generators.clipboard import ClipboardGenerator
from generators.accounts import AccountGenerator
from core.canary import CanaryInjector
from utils.config_loader import ConfigLoader

class MasterIntegration:
    @staticmethod
    def compile_full_trap_payload():
        # Load Config
        config = ConfigLoader.load()
        
        # Build Base
        builder = ProfileBuilder()
        payload = builder.build_profile()
        
        # Inject Advanced Subsystems
        payload["Running Processes"] = ProcessGenerator.generate()
        payload["Clipboard Data"] = ClipboardGenerator.generate()
        payload["Synchronized Accounts"] = AccountGenerator.generate()
        
        # Inject Canary Tokens if enabled
        if config["tracking"].get("enable_canary"):
            injector = CanaryInjector(config["tracking"]["canary_domain"])
            payload, token = injector.inject(payload)
            # Log the token issuance to the DB here...
            
        return payload
