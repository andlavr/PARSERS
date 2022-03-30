import json
import random
import time

from parsers.avito import avto
print(avto.m)
#
# import requests  # для запросов к сайту, получения содержимого веб-страницы
# from bs4 import BeautifulSoup  # для парсинга уже полученной страницы
#
# proxies ={'http': 'http://51.77.159.133:80',
#           'http': 'http://50.87.181.51:80'}
# headers = {
#     'content-type': "application/json;charset=utf-8",
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
# }
#
#
# def url_and_name_file():
#     # responce = requests.get(link, headers=headers)
#     # soup = BeautifulSoup(responce.text, 'html.parser')
#     # time.sleep(2)
#     cars_link = []
#     page_count = 1
#     page_max = 1
#     while page_count <= page_max:
#         # цикл получения ссылок на машины
#         url = f'https://www.avito.ru/sankt-peterburg/avtomobili?p={page_count}&radius=0'
#         print(url)
#         responce = requests.get(url, headers=headers, proxies=proxies)
#         soup = BeautifulSoup(responce.text, 'html.parser')
#
#         for div in soup.find_all('div', class_="iva-item-titleStep-pdebR"):
#             for link in div.find_all('a', href=True):
#                 cars_link.append(f"https://www.avito.ru/{link['href']}")
#
#         print(list(set(cars_link)))
#
#         time.sleep(random.randint(3, 5))
#         page_count += 1
#     all_data = {}
#     for link in cars_link:
#         link_dict = {}
#         link_dict.clear()
#
#         responce = requests.get(link, headers=headers)
#         soup = BeautifulSoup(responce.text, 'html.parser')
#         car_name = soup.find('span', class_='title-info-title-text').text
#
#
#
#         for ul in soup.find_all('ul', class_="item-params-list"):
#             # print(ul)
#
#             for li in ul.find_all('li', class_="item-params-list-item"):
#                 # key, value = li.text.split('\n')
#                 current_param = [value.strip() for value in li.text.split('\n')]
#                 if len(current_param) > 2:
#                     continue
#                 # key = key.strip()
#                 # value = value.strip()
#                 link_dict[current_param[0]] = current_param[1]
#         all_data[link] = link_dict
#         print(all_data)
#         with open('data.json', 'w') as outdickt:
#             json.dump(all_data, outdickt, indent=4, ensure_ascii=False)
#
#                 # print(li.text.split('\n'))
#                 # print(li.text.split('/n')[0].split('/n'))
#
#
#
#
#         a = time.sleep(random.randint(2, 4))
#         pass
#
#
#
#
#
# if __name__ == '__main__':
#     url_and_name_file()
#     # url_and_name_file('https://www.avito.ru/sankt-peterburg/avtomobili/kia-ASgBAgICAUTgtg3KmCg?cd=1&radius=0')