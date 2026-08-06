import random

class ProcessGenerator:
    BAIT_PROCESSES = [
        {"name": "monad-hft-node", "pid": random.randint(1000, 5000), "status": "running"},
        {"name": "cryptocurrency-notify-bot", "pid": random.randint(1000, 5000), "status": "sleeping"},
        {"name": "poppinit-engine", "pid": random.randint(5000, 9000), "status": "running"},
        {"name": "com.bitcoin.core", "pid": random.randint(5000, 9000), "status": "background"},
        {"name": "sshd", "pid": random.randint(100, 999), "status": "listening"}
    ]

    @staticmethod
    def generate():
        # Mix bait with normal Android/Linux background processes
        processes = [
            {"name": "zygote64", "pid": 312, "status": "running"},
            {"name": "system_server", "pid": 1024, "status": "running"},
            {"name": "com.android.phone", "pid": 1400, "status": "running"}
        ]
        
        # Inject 2-3 random bait processes
        processes.extend(random.sample(ProcessGenerator.BAIT_PROCESSES, k=random.randint(2, 4)))
        return processes
