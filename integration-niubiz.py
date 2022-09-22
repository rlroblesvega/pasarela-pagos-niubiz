import requests

url = "https://apitestenv.vnforapps.com/api.security/v1/security"

headers = {
    "accept": "text/plain",
    "authorization": "Basic aW50ZWdyYWNpb25lc0BuaXViaXouY29tLnBlOl83ejNAOGZG"
}

response = requests.get(url, headers=headers)

#print(response.text)
#print(response.status_code)


token = response.text


ip = requests.get('https://checkip.amazonaws.com').text.strip()
#print(ip)


url = "https://apisandbox.vnforappstest.com/api.ecommerce/v2/ecommerce/token/session/456879852"

payload = {
    "antifraud": {"clientIp": ip},
    "amount": "100.00",
    "channel": "mobile"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": token
}

response_se = requests.post(url, json=payload, headers=headers)

print(response_se.text)