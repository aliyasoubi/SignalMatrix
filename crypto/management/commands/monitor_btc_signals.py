# crypto/management/commands/monitor_btc_signals.py

from django.core.management.base import BaseCommand
import time
from django.core.management import call_command


class Command(BaseCommand):
    help = "Continuously monitor for BTC signals and fire alerts on new signals."

    def add_arguments(self, parser):
        parser.add_argument('--provider', type=str, default='coingecko')
        parser.add_argument('--interval', type=int, default=300, help='Seconds between checks (default 300=5min)')

    def handle(self, *args, **options):
        provider = options['provider']
        interval = options['interval']
        self.stdout.write(self.style.SUCCESS(
            f"Monitoring BTC signals every {interval} seconds using provider '{provider}'..."
        ))
        while True:
            call_command('generate_btc_signals', provider=provider)
            time.sleep(interval)
