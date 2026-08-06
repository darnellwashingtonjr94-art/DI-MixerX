import time

class TrapFirewall:
    def __init__(self, max_requests=10, window_seconds=60):
        self.ip_ledger = {}
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    def is_blocked(self, ip_address):
        current_time = time.time()
        
        if ip_address not in self.ip_ledger:
            self.ip_ledger[ip_address] = []
            
        # Clean up old requests outside the window
        self.ip_ledger[ip_address] = [
            req_time for req_time in self.ip_ledger[ip_address] 
            if current_time - req_time < self.window_seconds
        ]
        
        if len(self.ip_ledger[ip_address]) >= self.max_requests:
            return True # Block the attacker
            
        self.ip_ledger[ip_address].append(current_time)
        return False
