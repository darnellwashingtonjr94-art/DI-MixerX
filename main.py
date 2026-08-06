from core.builder import ProfileBuilder
from core.exporter import ProfileExporter
from utils.logger import TrapLogger

def main():
    logger = TrapLogger()
    logger.info("Initializing DI-MixerX Trap...")
    
    # Generate the fake profile
    builder = ProfileBuilder()
    fake_profile = builder.build_profile()
    
    # Export the profile to the trap directory
    exporter = ProfileExporter()
    filepath = exporter.save_to_json(fake_profile)
    
    logger.info(f"Trap set. Fake confidentials saved to {filepath}")

if __name__ == "__main__":
    main()
