import json
import os
import time
import traceback
import requests
from keys import proxy_key
from parsers.free_proxy.proxy import get_random_proxy


def get_new_proxy_from_rapidapi():
    """

    :return:
    """
    url = "https://proxypage1.p.rapidapi.com/v1/tier1random"

    querystring = {"type": "HTTP"}

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "proxypage1.p.rapidapi.com",
        "X-RapidAPI-Key": proxy_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()[0]

    return {data['types'][0]: f"{data['types'][0]}://{data['ip']}:{data['port']}"}


def get_proxy_from_free_proxy():
    return get_random_proxy()


def get_responce_data(url, headers, proxies=None) -> requests.Response:
    if proxies is None:
        responce = requests.get(url, headers=headers)
    else:
        responce = requests.get(url, headers=headers, proxies=proxies)

    responce_count = 0
    while responce.status_code != 200:
        proxy = get_new_proxy_from_rapidapi()
        responce = requests.get(url, headers=headers, proxies=proxy)
        responce_count += 1

        # Чтобы не потратить все ключи API
        if responce_count > 5:
            proxy = get_proxy_from_free_proxy()
            responce = requests.get(url, headers=headers, proxies=proxy)
            responce_count += 1

            if responce_count > 10:
                raise ConnectionError(f"Доступ к сайту ограничен. "
                                      f"Не удалось подобрать прокси. Ошибка {responce.status_code}")

    return responce


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
    print(get_new_proxy_from_rapidapi())
