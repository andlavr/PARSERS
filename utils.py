import json
import os
import time
import traceback
import requests

def get_new_proxy():
    """

    :return:
    """
    url = "https://proxypage1.p.rapidapi.com/v1/tier1random"

    querystring = {"type": "HTTP"}

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "proxypage1.p.rapidapi.com",
        "X-RapidAPI-Key": "8596f311femsh16c91d3e3355d37p14befajsn3dd3588db389"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()[0]

    return {data['types'][0]: f"{data['types'][0]}://{data['ip']}:{data['port']}"}


def cache_json_data(data: dict, cache_main_name: str) -> bool:
    """

    :param cache_main_name:
    :param data:
    :return:
    """

    try:
        if not os.path.exists("cache"):
            os.mkdir("cache")

        cache_file_name = f"{cache_main_name}_{time.strftime('%Y%m%d_%H%M%S', time.localtime())}.json"
        cache_full_name = os.path.join("cache", cache_file_name)

        with open(cache_full_name, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return True
    except:
        traceback.print_exc()  # Почитать про конструкцию print_exc
        return False


if __name__ == '__main__':
    # cache_json_data("1234", "avito_avto")
    print(get_new_proxy())
