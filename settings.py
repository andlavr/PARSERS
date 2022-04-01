"""
Модуль используется для хранения настроек пакета requests и приложения в целом
"""
import requests

# prox = {'39.106.228.34:8082', '51.77.159.133:80', '50.87.181.51:80', '58.137.62.133:80','82.223.108.75:80',
# '80.48.119.28:8080','20.105.253.176:8080', '47.111.94.201:1234', '178.73.192.6:8118', '140.246.87.238:3128'}
# for proxy in prox:
#     response = requests.get(proxies=proxy)
#     if response.status_code == requests.codes['ok']:
#         break
#
# # response.text

proxies = {
    'http': 'http://39.106.228.34:8080',
    'http': 'http://167.114.96.27:5566'}
# proxies = {
#     'http': 'http://185.119.59.244:80'}

headers = {
    'content-type': "application/json;charset=utf-8",
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
}
