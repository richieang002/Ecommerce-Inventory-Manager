from django.contrib import admin

# Register your models here.
from shopify_integration.models import ShopifyShop


class ShopifyShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShopifyShop, ShopifyShopAdmin)