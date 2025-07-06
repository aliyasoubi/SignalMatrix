from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CryptoAsset, CryptoSignal

admin.site.register(CryptoAsset)
admin.site.register(CryptoSignal)
