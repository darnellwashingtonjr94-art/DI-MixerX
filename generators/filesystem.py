import random

class FileSystemGenerator:
    @staticmethod
    def generate():
        total_gb = random.choice([64, 128, 256, 512])
        used_gb = random.uniform(15.0, total_gb - 5.0)
        free_gb = total_gb - used_gb
        
        return {
            "Internal Storage (Total)": f"{total_gb} GB",
            "Internal Storage (Used)": f"{round(used_gb, 2)} GB",
            "Internal Storage (Free)": f"{round(free_gb, 2)} GB",
            "External SD Card": random.choice(["Mounted", "Unmounted", "Not Present"])
        }
