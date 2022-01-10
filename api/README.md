# This project is incomplete and requires you to modify and add:
#### 1. Auth Token and Password for Shopify under api/settings.py
#### 2. Auth Token and Password for your Gmail under api/settings.py
#### 3. Django Secret Key under api/settings/py (use the code below to generate new key)
```
import secrets
```
```
import string
```
```
print("".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for range i in range(100)))
```

## Documentation

## Libs Used
[Rest Auth - Login, Register, Forget, Change Password](https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html)
