from typing import Optional

import requests
from bs4 import BeautifulSoup

from settings import headers, proxies
from utils import get_new_proxy, get_proxy_from_free_proxy, get_responce_data


def get_all_car_links_from_page(page: int = 1) -> Optional[list[str]]:
    """
    Функция возвращает список ссылок на автомобили на странице

    :param page: номер страницы
    :return: список ссылок
    """

    cars_link = []

    url = f'https://www.avito.ru/sankt-peterburg/avtomobili?p={page}&radius=0'
    print(url)

    responce = get_responce_data(url, headers, proxies)

    soup = BeautifulSoup(responce.text, 'html.parser')

    for div in soup.find_all('div', class_="iva-item-titleStep-pdebR"):
        for link in div.find_all('a', href=True):
            cars_link.append(f"https://www.avito.ru/{link['href']}")

    return list(set(cars_link))


def get_car_data_by_link(link: str) -> dict:
    """

    :param link:
    :return:
    """

    responce = get_responce_data(link, headers, proxies)
    soup = BeautifulSoup(responce.text, 'html.parser')

    car_name = get_car_brand_and_model_from_soup(soup)
    car_parameters = get_car_parameters_from_soup(soup)

    car_parameters.update(car_name)  # складываем два словаря

    return car_parameters


def get_car_brand_and_model_from_soup(soup: BeautifulSoup) -> dict:
    """

    :param soup:
    :return:
    """

    data = soup.find('span', class_='title-info-title-text').text

    # TODO: Подумать как лучше разделять брэнд и модель
    # TODO: Список можно хранить в БД и как-то сравнивать на дальнейшую перспективу

    # Алгоритм не предусматривает существования названий брэндов состоящих из 2 слов
    data = data.split(",")[0]  # Отсекаем год
    data = data.split(" ")

    return {"Брэнд": data[0], "Модель": data[1]}


def get_car_parameters_from_soup(soup: BeautifulSoup) -> dict:
    """

    :param soup:
    :return:
    """

    link_dict = {}

    for ul in soup.find_all('ul', class_="item-params-list"):
        for li in ul.find_all('li', class_="item-params-list-item"):
            current_param = [value.strip() for value in li.text.split('\n')]
            if len(current_param) > 2:
                continue

            link_dict[current_param[0]] = current_param[1]

    return link_dict


def get_all_brands():
    pass


if __name__ == '__main__':
    get_car_data_by_link("https://www.avito.ru//sankt-peterburg/avtomobili/mazda_6_2008_2391707169")