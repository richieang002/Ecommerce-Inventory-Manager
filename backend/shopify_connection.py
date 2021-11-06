import requests
import json

url = "https://1316732125919bce7ee4b91650c0a6fb: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@lazeapi-testbed.myshopify.com//admin/api/2021-07/products.json?fields=id"

payload = ""
headers = {
  'Authorization': 'Basic MTMxNjczMjEyNTkxOWJjZTdlZTRiOTE2NTBjMGE2ZmI6c2hwcGFfZTk0YTQxM2UwMzk2MmY3NGZjNmYyOGY2YWUzYzhkN2U='
}

response = requests.request("GET", url, headers=headers, data=payload)
# response_native = json.loads(response.text)

try: 
    response_native = response.json()
except ValueError as exc:
    print(f"Exception: {exc}")

emptyList = []

for counter in range(len(response_native["products"])):
    emptyList.append(response_native["products"][counter].get('id'))

print("\n")
print(emptyList)
