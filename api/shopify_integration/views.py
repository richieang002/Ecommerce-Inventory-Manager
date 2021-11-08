import binascii
import os

import shopify
from rest_framework.response import Response

from api.settings import BASE_URL, SHOPIFY_API_KEY, SHOPIFY_API_SECRET
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.permissions import IsAuthenticated
import csv

from shopify_integration.models import ShopifyShop


@api_view(['GET'])
def shopify_login(request):
    shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_API_SECRET)
    shop_url = request.GET['shop']
    api_version = '2020-10'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = f'{BASE_URL}/shopify/callback/'
    scopes = ['read_products', 'write_products', 'read_inventory', 'write_inventory']

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

    return HttpResponseRedirect(
        'http://localhost:3000/import/connect?access_code=' + str(access_token) + '&shop_url=' + str(shop_url))


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def shopify_products(request):
    shop = ShopifyShop.objects.get(user=request.user)
    api_version = '2020-10'
    session = shopify.Session(shop.shop_url, api_version, shop.access_code)
    shopify.ShopifyResource.activate_session(session)
    products = shopify.Product.find()
    data = []
    for x in products:
        for y in x.attributes['variants']:
            image = list(filter(lambda z: z.attributes['id'] == y.attributes['image_id'], x.attributes['images']))
            image = image[0] if len(image) else None
            data.append({
                'id': x.attributes['id'],
                'platform': 'shopify',
                'title': x.attributes['title'] + ' ' + y.attributes['title'],
                'product_type': x.attributes['product_type'],
                'status': x.attributes['status'],
                'updated_at': x.attributes['updated_at'],
                'image': image.attributes['src'] if image else '',
                'variant_id': y.attributes['id'],
                'inventory_item_id': y.attributes['inventory_item_id'],
                'SKU': y.attributes['sku'],
                'price': y.attributes['price'],
                'inventory_quantity': y.attributes['inventory_quantity'],
            })

    return Response({'products': data}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shopify_product_update(request):
    location_id = 64986349727
    inventory_item_id = request.data['id']
    quantity = request.data['quantity']
    shop = ShopifyShop.objects.get(user=request.user)
    api_version = '2020-10'
    session = shopify.Session(shop.shop_url, api_version, shop.access_code)
    shopify.ShopifyResource.activate_session(session)
    product = shopify.InventoryLevel()
    product.set(location_id=location_id, inventory_item_id=inventory_item_id, available=quantity)

    return Response({'message': 'update product success'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shopify_product_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    shop = ShopifyShop.objects.get(user=request.user)
    api_version = '2020-10'
    session = shopify.Session(shop.shop_url, api_version, shop.access_code)
    shopify.ShopifyResource.activate_session(session)
    products = shopify.Product.find()
    data = []
    for x in products:
        for y in x.attributes['variants']:
            image = list(filter(lambda z: z.attributes['id'] == y.attributes['image_id'], x.attributes['images']))
            image = image[0] if len(image) else None
            data.append({
                'id': x.attributes['id'],
                'platform': 'shopify',
                'title': x.attributes['title'] + ' ' + y.attributes['title'],
                'product_type': x.attributes['product_type'],
                'status': x.attributes['status'],
                'updated_at': x.attributes['updated_at'],
                'image': image.attributes['src'] if image else '',
                'variant_id': y.attributes['id'],
                'inventory_item_id': y.attributes['inventory_item_id'],
                'SKU': y.attributes['sku'],
                'price': y.attributes['price'],
                'inventory_quantity': y.attributes['inventory_quantity'],
            })
    writer.writerow(list(data[0].keys()))
    for row in data:
        writer.writerow(row.values())
    return response
