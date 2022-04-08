import requests
from bs4 import BeautifulSoup
import csv
import time


# Функция получения кода страницы
def get_html(url):
    r = requests.get(url)
    return r.text


# Функция получения максимального числа страниц
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


# Функция записи данных в CSV файл
def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow((data['time'],
                         data['title'],
                         data['price'],
                         data['url']))


# Функция получения нужных данных из страницы
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('div', class_='about').text.strip().strip('  ₽')
        except:
            price = ''

        ad_time = time.strftime("%H:%M:%S %d.%m.%Y", time.localtime())

        data = {'time': ad_time,
                'title': title,
                'price': price,
                'url': url
                }
        write_csv(data)


def main():
    url = 'https://www.avito.ru/sankt-peterburg/mebel_i_interer/kompyuternye_stoly_i_kresla?p=1&pmax=1000&pmin=0'
    base_url = 'https://www.avito.ru/sankt-peterburg/mebel_i_interer/kompyuternye_stoly_i_kresla?'
    page_part = 'p='
    query_part = '&pmax=1000&pmin=0'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)


while True:
    i = 600
    main()
    print('Отчёт сформирован')
    while i > -1:
        print('Отчёт будет обновлён через ' + str(i // 60) + ' минут ' + str(i % 60) + ' секунд')
        i -= 30
        time.sleep(30)
