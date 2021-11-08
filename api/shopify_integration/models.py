from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ShopifyShop(models.Model):
    shop_url = models.URLField(unique=True)
    access_code = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
