import urllib.request
import json


def fetch_endpoint(input_url=None):
    if input_url is None:
        input_url = "http://benspelledabc.me/news/news_api/9/?format=json"

    with urllib.request.urlopen(input_url) as url:
        data = json.loads(url.read().decode())
        # print(data)

    return data


output = fetch_endpoint()
print(output)
output = fetch_endpoint("http://benspelledabc.me/pi_test")
print(output)
