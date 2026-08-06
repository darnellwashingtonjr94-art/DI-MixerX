import argparse
import sys
from advanced_server import AdvancedTrapHandler
from core.daemon import MultiPortDaemon
from analysis.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="DI-MixerX Master Controller")
    parser.add_argument('--start', action='store_true', help='Start the live trap daemon')
    parser.add_argument('--report', action='store_true', help='Generate attacker ledger report')
    parser.add_argument('--ports', type=int, nargs='+', default=[8080, 8888], help='Ports to bind (e.g., --ports 80 8080)')
    
    args = parser.parse_args()

    if args.report:
        generate_report()
        sys.exit(0)

    if args.start:
        daemon = MultiPortDaemon(handler_class=AdvancedTrapHandler, ports=args.ports)
        try:
            daemon.ignite()
        except KeyboardInterrupt:
            print("\n[*] Shutting down DI-MixerX trap...")
            sys.exit(0)
            
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
