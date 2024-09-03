import requests

url = 'https://vulners.com/api/v3/search/lucene/'
data = {
    "query": "Cisco",
    "apiKey": "SXXX9EXXXXXXXXXXXXXX9X0N1HH4S2F59KM2MD7OC7WZUV9BSKO1SSFBHBUHUHUHHI3",
}

response = requests.post(url, json=data)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
