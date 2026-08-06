from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from core.builder import ProfileBuilder
from core.obfuscator import PayloadObfuscator
from generators.imei import IMEIGenerator
from generators.serial import SerialGenerator
from generators.network import NetworkGenerator
from middleware.auth_trap import AuthTrap
from middleware.headers import FakeHeaders
from utils.delay import TarpitDelay
from utils.parser import RequestParser
from utils.logger import TrapLogger
from webhooks.notifier import WebhookNotifier

class AdvancedTrapHandler(BaseHTTPRequestHandler):
    logger = TrapLogger()
    auth_trap = AuthTrap()
    notifier = WebhookNotifier(webhook_url=None) # Add URL here

    def do_GET(self):
        # 1. Parse and Log
        req_info = RequestParser.extract_info(self)
        self.logger.info(f"Connection from {req_info['ip']} via {req_info['user_agent']}")
        self.notifier.send_alert(req_info['ip'], req_info['user_agent'])

        # 2. Check for Credentials (Auth Trap)
        self.auth_trap.inspect_headers(self.headers, req_info['ip'])

        # 3. Tarpit (Waste attacker time)
        TarpitDelay.apply_jitter()

        # 4. Build Advanced Profile
        builder = ProfileBuilder()
        profile = builder.build_profile()
        profile["IMEI"] = IMEIGenerator.generate()
        profile["Serial Number"] = SerialGenerator.generate()
        profile.update(NetworkGenerator.generate())

        # 5. Obfuscate Payload
        final_payload = PayloadObfuscator.obfuscate(profile)

        # 6. Send Fake Headers and Response
        self.send_response(200)
        fake_headers = FakeHeaders.get_headers()
        for key, value in fake_headers.items():
            if value:
                self.send_header(key, value)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(final_payload).encode('utf-8'))

if __name__ == "__main__":
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, AdvancedTrapHandler)
    print(f"[*] DI-MixerX Advanced Live Trap running on port {port}...")
    httpd.serve_forever()
