import binascii
import os

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
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
            if len(image):
                image = image[0]
            else:
                image = x.image
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
def shopify_product_discard(request):
    variant_id = request.data['id']
    product_id = request.data['product_id']
    shop = ShopifyShop.objects.get(user=request.user)
    api_version = '2020-10'
    session = shopify.Session(shop.shop_url, api_version, shop.access_code)
    shopify.ShopifyResource.activate_session(session)
    variants = shopify.Variant.find(product_id=product_id)

    if len(variants) > 1:
        variant = shopify.Variant.find(variant_id)
        variant.destroy()
    else:
        product = shopify.Product.find(product_id)
        product.destroy()

    return Response({'message': 'delete product success'}, status=200)


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
            if len(image):
                image = image[0]
            else:
                pass
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


@api_view(['POST'])
def reset_password(request):
    username = request.data['username']
    subject = 'LazeAPI New Password'
    new_password = binascii.b2a_hex(os.urandom(8)).decode("utf-8")
    message = 'Thank you for using our service! We have kindly resetted your password.\nPlease do not share your password with anyone.\nNew password is - ' + str(new_password)
    email_from = settings.EMAIL_HOST_USER
    try:
        user = User.objects.get(username=username)
    except:
        return Response({'message': 'username not found'}, status=400)
    recipient_list = [user.email, ]
    try:
        send_mail(subject, message, email_from, recipient_list)
        user.set_password(new_password)  # replace with your real password
        user.save()
    except:
        return Response({'message': 'mail not sent'}, status=400)

    return Response({'message': 'password change success'}, status=200)
