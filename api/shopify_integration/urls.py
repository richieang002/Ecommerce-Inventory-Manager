"""
shopify integration urls
"""
from django.urls import path

from shopify_integration.views import shopify_login, shopify_callback

urlpatterns = [
    path('login/', shopify_login),
    path('callback/', shopify_callback),
]
