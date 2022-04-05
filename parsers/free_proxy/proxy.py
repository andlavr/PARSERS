import base64
import random

from bs4 import BeautifulSoup

from utils import get_responce_data

querystring = {"type": "HTTP"}

headers = {
    'content-type': "application/json;charset=utf-8",
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
}


def get_all_proxies_links_from_page(page: int = 1):
    """
    список списков вида
    [IP адрес, порт, протокол, страна, площадь, Сити, анонимность, скорость, наличие, ответ, Проверено]

    :param page:
    :return:
    """

    proxy_links = []

    url = 'http://free-proxy.cz/ru/proxylist/country/all/http/uptime/level1'  # {/page} - в конце ссылки
    print(url)

    responce = get_responce_data(url, headers=headers)

    soup = BeautifulSoup(responce.text, 'html.parser')

    table = soup.find("table", {"id": "proxy_list"})
    tbody = table.find('tbody')

    for tr in tbody.find_all('tr'):
        proxy_link = []

        for td in tr.find_all('td'):
            value = td.string
            if td.string is None:
                value = td.text

            proxy_link.append(value)

        proxy_links.append(proxy_link[:])

    for proxy_link_id in range(len(proxy_links)):
        proxy_links[proxy_link_id] = normalize_ip_in_proxy_link(proxy_links[proxy_link_id])

    return proxy_links


def normalize_ip_in_proxy_link(proxy_link: list):
    for elem_id in range(len(proxy_link)):
        if elem_id == 0:
            try:
                normalize_ip = proxy_link[elem_id].split('\"')
                normalize_ip = base64.decodebytes(normalize_ip[1].encode('utf-8')).decode('utf-8')
                proxy_link[elem_id] = normalize_ip
            except IndexError:
                pass
    return proxy_link


def check_availability_less_value(proxy_links: list, value: int):
    """

    :param proxy_links:
    :param value:
    :return:
    """

    # TODO Написать list comprehension для отбора всех значений,
    # TODO у которых value > заданного
    pass


def get_random_proxy():

    random_proxy = random.choice(get_all_proxies_links_from_page())
    return {random_proxy[2].lower(): f"{random_proxy[2].lower()}://{random_proxy[0]}:{random_proxy[1]}"}


if __name__ == '__main__':
    get_random_proxy()
