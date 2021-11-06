import requests
import ujson as json

url = "https://1316732125919bce7ee4b91650c0a6fb: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@lazeapi-testbed.myshopify.com//admin/api/2021-10/products.json?fields=id"
payload = ""
headers = {
  'Authorization': 'Basic MTMxNjczMjEyNTkxOWJjZTdlZTRiOTE2NTBjMGE2ZmI6c2hwcGFfZTk0YTQxM2UwMzk2MmY3NGZjNmYyOGY2YWUzYzhkN2U='
}

response = requests.request("GET", url, headers=headers, data=payload)

empty_list = []

for counter in range(len(response.json()['products'])):
    empty_list.append(response.json()['products'][counter].get('id'))

i1 = 0
new_list = []
for id in empty_list:
    temp_list = []
    product_id = str(empty_list[i1])
    url = "https://1316732125919bce7ee4b91650c0a6fb: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@lazeapi-testbed.myshopify.com//admin/api/2021-10/products/"+product_id+"/variants.json?"
    payload={}
    headers = {
    'Authorization': 'Basic MTMxNjczMjEyNTkxOWJjZTdlZTRiOTE2NTBjMGE2ZmI6c2hwcGFfZTk0YTQxM2UwMzk2MmY3NGZjNmYyOGY2YWUzYzhkN2U='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()['variants']
    for x in range(len(r)):
        temp_list.append(r[x]['sku'])
        temp_list.append(r[x]['inventory_quantity'])
    new_list.append(temp_list)
    #print(new_list)
    i1+=1

print(new_list)

