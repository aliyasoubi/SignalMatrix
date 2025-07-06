from django.shortcuts import render
from crypto.models import CryptoAsset, CryptoSignal


def btc_signals(request):
    # Only show BTC signals, sorted newest first
    try:
        btc = CryptoAsset.objects.get(symbol='BTC')
        signals = CryptoSignal.objects.filter(asset=btc).order_by('-timestamp')[:10]
    except CryptoAsset.DoesNotExist:
        signals = []
    return render(request, 'dashboard/btc_signals.html', {'signals': signals})
