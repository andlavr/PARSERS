"""
Модуль используется для хранения настроек пакета requests и приложения в целом
"""

proxies = {
    'http': 'http://58.137.62.133:80',
    'http': 'http://82.223.108.75:80'}

headers = {
    'content-type': "application/json;charset=utf-8",
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
}
