import requests
from requests.structures import CaseInsensitiveDict

url = "http://faucet.noislabs.com/credit"

headers = CaseInsensitiveDict()
headers["X-Custom-Header"] = "value"
headers["Content-Type"] = "application/json"

data = '{"address": "nois1l4u3g0w7zqqsk46hw5j56dex9ppcp58mmsfdye","denom": "unois"}'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
