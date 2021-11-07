import binascii
import os

import shopify
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.response import Response

from api.settings import BASE_URL, SHOPIFY_API_KEY, SHOPIFY_API_SECRET


@api_view(['GET'])
def shopify_login(request):
    shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_API_SECRET)
    shop_url = "https://lazeapi-testbed.myshopify.com"
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

    return HttpResponse('Shopify Integration Success')
