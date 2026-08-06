# DI-MixerX

DI-MixerX is a defensive cybersecurity honeypot designed to trap, confuse, and monitor malicious actors. It is built to look like a highly valuable, vulnerable system to lure in hackers, automated scrapers, and malware, keeping them away from your real infrastructure.

---

## What Does It Do?

DI-MixerX dynamically generates completely fake, yet highly realistic, device identifiers and system profiles. When an attacker probes the server, the tool feeds them an endless stream of bogus data.

*   **Hardware Identifiers:** Dynamically generates fake MAC addresses, IMEIs, and serial numbers.
*   **Network Info:** Spoofs IP addresses, Wi-Fi connections, and simulated cellular carrier data.
*   **Telemetry:** Creates fake GPS coordinates, realistic battery levels, and simulated sensor movements.
*   **Juicy Bait:** Injects simulated running processes, clipboard data containing fake passwords/wallets, and fake synchronized accounts to keep attackers engaged.

---

## Architecture & Workflow

The repository is built with a highly modular Python architecture to allow for easy scaling and customization.

*   **Generators (`/generators`):** Scripts that handle the creation of the randomized fake data payloads.
*   **Middleware (`/middleware`):** The active defense layer that manages aggressive scrapers, captures attempted passwords, and spoofs connections like Android Debug Bridge (ADB).
*   **Core Logic (`/core` & `/utils`):** Compiles the fake data into single JSON payloads and introduces "tar-pitting"—artificial loading delays that waste the attacker's time.
*   **Server & CLI:** The `advanced_server.py` script spins up the live HTTP trap, while `cli.py` acts as a master control panel to manage the daemons.
*   **Analysis:** Logs all attacker activity (IPs, user agents, captured credentials) to a local SQLite database and can trigger live alerts via webhooks.

---

## Problems Solved

*   **Resource Wasting:** Acts as a tarpit, tying up an attacker's automated scanning tools and wasting their processing threads.
*   **Intelligence Gathering:** Builds a ledger of the IPs, attack methods, and credentials that threat actors attempt to use, allowing you to blacklist them across your real networks.
*   **Active Deception:** Injects unique "Canary Tokens" into the fake data to unmask the real IP addresses of attackers who try to parse the URLs, even if they are behind a proxy.

---

## Installation & Deployment

Because this is an active security tool, it is highly recommended to run it in an isolated environment so it does not expose your host machine.

### Method 1: Docker (Recommended)

Deploy the entire trap safely inside a containerized sandbox using the provided configuration. From the root of the repository, run:

```bash
docker-compose up -d
