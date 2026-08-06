import uuid

class CanaryInjector:
    def __init__(self, base_tracking_domain):
        self.base_domain = base_tracking_domain

    def inject(self, payload):
        # Generate a unique token for this specific attacker
        token = uuid.uuid4().hex
        tracking_url = f"https://{self.base_domain}/ping/{token}"
        
        # Inject a fake "update_server" or "backup_url" that an automated 
        # scraper might try to crawl.
        payload["system_update_url"] = tracking_url
        payload["backup_sync_endpoint"] = tracking_url
        
        return payload, token
