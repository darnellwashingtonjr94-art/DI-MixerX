import base64
from utils.logger import TrapLogger

class AuthTrap:
    def __init__(self):
        self.logger = TrapLogger()

    def inspect_headers(self, headers, client_ip):
        auth_header = headers.get('Authorization')
        if auth_header:
            self.logger.info(f"CREDENTIALS CAPTURED from {client_ip}: {auth_header}")
            # If basic auth, try to decode it for the logs
            if auth_header.startswith("Basic "):
                try:
                    decoded = base64.b64decode(auth_header[6:]).decode()
                    self.logger.info(f"Decoded Basic Auth ({client_ip}): {decoded}")
                except Exception:
                    pass
        return True # Always grant access to the trap
