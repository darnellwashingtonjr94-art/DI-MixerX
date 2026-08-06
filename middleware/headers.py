import random

class FakeHeaders:
    SERVERS = [
        "nginx/1.21.6",
        "Apache/2.4.52 (Ubuntu)",
        "Microsoft-IIS/10.0",
        "lighttpd/1.4.59"
    ]

    @staticmethod
    def get_headers():
        return {
            "Server": random.choice(FakeHeaders.SERVERS),
            "X-Powered-By": random.choice(["PHP/8.1.0", "Express", "ASP.NET", None]),
            "X-Frame-Options": "SAMEORIGIN"
        }
