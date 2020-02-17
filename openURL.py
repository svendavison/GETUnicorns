import urllib.request
import json


def fetch_json_endpoint(input_url=None):
    if input_url is None:
        input_url = "http://benspelledabc.me/news/news_api/9/?format=json"

    data = ""
    try:
        with urllib.request.urlopen(input_url) as url:
            data = json.loads(url.read().decode())
            # print(data)
    except Exception:
        data = fetch_endpoint(input_url)

    return data


def fetch_endpoint(input_url=None):
    import urllib.request
    return_val = ""
    if input_url is None:
        input_url = "http://benspelledabc.me/"

    try:
        contents = urllib.request.urlopen(input_url).read()
        return_val = contents
    except Exception as e:
        return e

    return return_val

