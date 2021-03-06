import json
import os
import time
import traceback
import requests
import datetime
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
    new_proxy = {data['types'][0]: f"{data['types'][0]}://{data['ip']}:{data['port']}"}
    update_api_proxy_status(new_proxy)
    show_api_proxy_status()
    return new_proxy


def update_api_proxy_status(proxy: dict):
    if not os.path.exists("logs"):
        os.mkdir("logs")
    year_month = f'{datetime.date.today().year}_{datetime.date.today().month}'
    with open(f'logs\\api_count_{year_month}.log', 'a') as file:
        file.write(f'{time.ctime()}: "Change proxy on {proxy}')
        file.write('\n')


def show_api_proxy_status():
    year_month = f'{datetime.date.today().year}_{datetime.date.today().month}'
    with open(f'logs\\api_count_{year_month}.log', 'r') as file:
        data = file.read()
    row_count = len(data.split("\n"))-1
    print(f'За {year_month}, сделано {row_count} запросов')


def get_proxy_from_free_proxy():
    return get_random_proxy()


def get_responce_data(url, headers, proxies=None) -> requests.Response:
    params = {
        'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
    }
    if proxies is None:
        responce = requests.get(url, headers=headers, params=params)
    else:
        responce = requests.get(url, headers=headers, proxies=proxies, params=params)

    responce_count = 0
    while responce.status_code != 200:
        proxy = get_new_proxy_from_rapidapi()
        print(f'ответ от сайта: {responce.status_code}. Провожу смену прокси')
        print(f'Новый прокси: {proxy}')
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
        show_my_ip(headers, proxies)

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


def show_my_ip(headers, proxies):
    try:
        responce = requests.get('http://icanhazip.com/', proxies=proxies)
        print(responce.text)
    except requests.exceptions.ProxyError:
        print("Не удалось узнать новый IP")






if __name__ == '__main__':
    # cache_json_data("1234", "avito_avto")
    print(get_new_proxy_from_rapidapi())
    # print(requests.get('https://www.ozon.ru/'))


