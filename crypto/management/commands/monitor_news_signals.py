# crypto/management/commands/monitor_news_signals.py

from django.core.management.base import BaseCommand
import time
from django.core.management import call_command


class Command(BaseCommand):
    help = "Continuously monitor news signals"

    def add_arguments(self, parser):
        parser.add_argument('--interval', type=int, default=300, help='Check every N seconds (default 300=5min)')

    def handle(self, *args, **options):
        interval = options['interval']
        while True:
            call_command('generate_btc_signals')  # assumes your strategy is integrated
            time.sleep(interval)
