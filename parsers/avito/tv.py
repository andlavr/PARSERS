import requests
from bs4 import BeautifulSoup


# url = 'https://www.avito.ru/sankt-peterburg/audio_i_video/televizory_i_proektory?pmax=10000&pmin=5000&q=lg'

def search_my_tv(model, min_price, max_price):
    count_page = 1

    while True:
        url = f'https://www.avito.ru/sankt-peterburg/audio_i_video/televizory_i_proektory?p=' \
              f'{str(count_page)}&pmax={max_price}&pmin={min_price}&q={model}'

        print(url)
        connection_to_avito = requests.get(url)
        count_page += 1
        print(count_page)
        print(connection_to_avito.status_code)
        soup = BeautifulSoup(connection_to_avito.text, features='lxml')
        print(soup)

    # for page in total_page:
    #     print(page)
    #     connection_to_page = requests.get(page)
    #     print(connection_to_page.status_code)
    #     soup = BeautifulSoup(connection_to_page.text, features='lxml')
    #     tv_on_page = soup.find_all('a', {'class':'item-description-title-link'})
    #
    #     for current_tv in tv_on_page:
    #         link_to_tv = 'https://www.avito.ru' + current_tv.get('href')
    #         print(link_to_tv)
    #         #connection_to_link_to_tv = requests.get(link_to_tv)
    #         #print(connection_to_link_to_tv)



    #else:
    #    print("Вот этот код я тебе вернул:", connection_to_avito.status_code)


search_my_tv('samsung', '5000', '10000')

'''
avito_catalog = soup.find('div',{'class':'catalog-content'})

avito_tovari = avito_catalog.find_all('div', {'class':'item_table-wrapper'})
count = 0
tovari_dic = {}

for tovar_info in avito_tovari:

        tovar_link = 'https://www.avito.ru/moskva' + tovar_info.find('a', {'class' : 'item-description-title-link' }).get('href')
        #print(tovar_info)
        #print(tovar_link)
        '''



