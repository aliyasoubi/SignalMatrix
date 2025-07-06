from django.db import models


class CryptoAsset(models.Model):
    DoesNotExist = None
    objects = None
    symbol = models.CharField(max_length=10, unique=True)  # e.g. "BTC"
    name = models.CharField(max_length=40)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.symbol


class CryptoSignal(models.Model):
    objects = None
    asset = models.ForeignKey(CryptoAsset, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    signal_type = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    score = models.FloatField(default=0)
    raw_data = models.JSONField()
    was_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asset.symbol} {self.signal_type} @{self.timestamp:%Y-%m-%d %H:%M:%S}"
