import requests
import os
API_KEY = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"

}
print(API_KEY)
response = requests.get("https://example.com/products",
                        headers = headers)
response.raise_for_status()
print(response.json())
