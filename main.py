"""
Модуль для запуска парсеров
"""

import random
import time

from parsers.avito import avto as avito_avto
from utils import cache_json_data


def parse_avito_avto(max_page, cache_json_status: bool = False, cache_db_status: bool = False) -> None:
    """

    :param max_page:
    :param cache_json_status:
    :param cache_db_status:
    :return:
    """

    print(f"Парсер начал работу {time.strftime('%Y-%m-%d в %H:%M:%S', time.localtime())}")

    # Получение ссылок со страниц
    cars_link = []
    for page_number in range(1, max_page+1):
        try:
            cars_link += avito_avto.get_all_car_links_from_page(page_number)
            time.sleep(random.randint(3, 5))
        except ConnectionError as err:
            print(err)
            return None

    # Обрабатываем конкретную ссылку на автомобиль
    all_data = {}
    for link in cars_link:
        all_data[link] = avito_avto.get_car_data_by_link(link)

    if cache_json_status:
        cache_json_data(all_data, "avito_avto")

    print(f"Парсер закончил работу {time.strftime('%Y-%m-%d в %H:%M:%S', time.localtime())}")


if __name__ == '__main__':
    parse_avito_avto(1, cache_json_status=True)
