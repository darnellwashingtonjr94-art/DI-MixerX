import random

class AppListGenerator:
    JUICY_APPS = [
        "com.bitcoin.core.wallet",
        "io.monad.validator.node",
        "finance.chase.mobile",
        "com.binance.app",
        "org.telegram.messenger",
        "com.github.cryptonotify",
        "com.google.android.apps.authenticator2",
        "app.poppinit.mobile",
        "com.hft.execution.controller"
    ]

    @staticmethod
    def generate():
        # Randomly select a subset of juicy targets to make the device look valuable
        installed = random.sample(AppListGenerator.JUICY_APPS, k=random.randint(3, 7))
        # Add some standard background noise
        installed.extend(["com.android.chrome", "com.google.android.youtube", "com.android.settings"])
        random.shuffle(installed)
        
        return installed
