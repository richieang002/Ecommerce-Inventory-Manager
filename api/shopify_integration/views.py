import binascii
import os

import shopify
from api.settings import BASE_URL, SHOPIFY_API_KEY, SHOPIFY_API_SECRET
from django.http import HttpResponseRedirect
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from shopify_integration.models import ShopifyShop


@api_view(['GET'])
def shopify_login(request):
    shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_API_SECRET)
    shop_url = request.GET['shop']
    api_version = '2020-10'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = f'{BASE_URL}/shopify/callback/'
    scopes = ['read_products']

    newSession = shopify.Session(shop_url, api_version)
    auth_url = newSession.create_permission_url(scopes, redirect_uri, state)
    # redirect to auth_url

    return HttpResponseRedirect(auth_url)


@api_view(['GET'])
def shopify_callback(request):
    shop_url = "https://lazeapi-testbed.myshopify.com"
    api_version = '2020-10'

    session = shopify.Session(shop_url, api_version)
    access_token = session.request_token(request.GET)  # request_token will validate hmac and timing attacks
    # you should save the access token now for future use.

    return HttpResponseRedirect('http://localhost:3000/import/connect?access_code=' + str(access_token) + '&shop_url=' + str(shop_url))


class ShopifyShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopifyShop
        fields = '__all__'


class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ShopifyShop.objects.all()
    serializer_class = ShopifyShopSerializer
    permission_classes = [IsAuthenticated]
