# crypto/management/commands/generate_btc_signals.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from crypto.models import CryptoAsset, CryptoSignal
from crypto.strategies import STRATEGY_CLASSES
from crypto.data_providers import PROVIDERS

from typing import Any


class Command(BaseCommand):
    help = 'Generate BTC signals using modular strategies and pluggable data providers.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--provider',
            type=str,
            default='dummy',
            help='Market data provider to use (dummy, binance, etc.). Default: dummy'
        )
        parser.add_argument(
            '--symbol',
            type=str,
            default='BTCUSDT',
            help='Trading symbol (e.g., BTCUSDT for Binance, ignored for dummy)'
        )

    def handle(self, *args: Any, **options: Any) -> None:
        provider_name: str = options['provider']
        symbol: str = options['symbol']

        # Get asset or create it (if not exists)
        asset, _ = CryptoAsset.objects.get_or_create(
            symbol='BTC',
            defaults={'name': 'Bitcoin', 'enabled': True}
        )

        # Get the correct market data provider class
        ProviderClass = PROVIDERS.get(provider_name)
        if ProviderClass is None:
            self.stderr.write(
                self.style.ERROR(f"Unknown provider '{provider_name}'. Available: {list(PROVIDERS.keys())}"))
            return
        provider = ProviderClass()

        # Fetch current market data for the chosen symbol
        try:
            market_data = provider.get_market_data(symbol)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error fetching market data: {e}"))
            return

        # Run each enabled strategy with market data
        signals_created = 0
        for StrategyClass in STRATEGY_CLASSES:
            strategy = StrategyClass()
            signals = strategy.generate_signals(market_data)
            for sig in signals:
                CryptoSignal.objects.create(
                    asset=asset,
                    signal_type=sig['signal_type'],
                    description=sig['description'],
                    score=sig['score'],
                    raw_data=sig['raw_data'],
                    was_notified=False,
                    timestamp=timezone.now()
                )
                signals_created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Generated {signals_created} signals using '{provider_name}' provider." if signals_created else "No signals generated (criteria not met)."))
