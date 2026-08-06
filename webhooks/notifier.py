import json
import urllib.request
import threading

class WebhookNotifier:
    def __init__(self, webhook_url=None):
        self.webhook_url = webhook_url

    def send_alert(self, attacker_ip, user_agent):
        if not self.webhook_url:
            return

        payload = {
            "content": f"🚨 **TRAP TRIGGERED** 🚨\n**IP:** `{attacker_ip}`\n**Agent:** `{user_agent}`"
        }
        
        def _post():
            req = urllib.request.Request(
                self.webhook_url, 
                data=json.dumps(payload).encode(),
                headers={'Content-Type': 'application/json'}
            )
            try:
                urllib.request.urlopen(req, timeout=5)
            except Exception as e:
                print(f"Failed to send webhook: {e}")

        # Run in background so it doesn't slow down the response
        threading.Thread(target=_post).start()
