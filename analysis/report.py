from utils.db import TrapDatabase

def generate_report():
    db = TrapDatabase()
    cursor = db.conn.cursor()
    
    print("\n--- DI-MixerX Attacker Report ---")
    
    # Top Attacking IPs
    print("\n[+] Top 5 Aggressive IPs:")
    cursor.execute("SELECT ip_address, COUNT(*) as hits FROM attackers GROUP BY ip_address ORDER BY hits DESC LIMIT 5")
    for row in cursor.fetchall():
        print(f"    - IP: {row[0]} | Hits: {row[1]}")
        
    # Captured Credentials
    print("\n[+] Harvested Credentials:")
    cursor.execute("SELECT ip_address, captured_credentials FROM attackers WHERE captured_credentials IS NOT NULL")
    for row in cursor.fetchall():
        print(f"    - From {row[0]}: {row[1]}")
        
    print("\n---------------------------------")

if __name__ == "__main__":
    generate_report()
