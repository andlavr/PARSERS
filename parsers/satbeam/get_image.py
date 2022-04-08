# -*- coding: utf-8 -*-

import os
import re
import time

import httplib2
import requests
from bs4 import BeautifulSoup

url = 'https://www.satbeams.com/satellites'
request_to_SatBeam = requests.get(url)

if request_to_SatBeam.status_code == 200:
    print('Всё в норме, подключение установлено!')
else:
    print('Был возвращён код: ', request_to_SatBeam.status_code)

soup = BeautifulSoup(request_to_SatBeam.text, features='lxml')

satellite_table = soup.find('div', {'id':'table_wrap'})
#print(satellite_table)
satellites_list = satellite_table.find_all('tr', {'class':'class_tr'})
#print(satellites_list)
count = 0
satellite_links_dict = {}
for satellite_info in satellites_list:
    satellite_status = satellite_info.contents[3].text
    if satellite_status == 'active' or satellite_status == 'planned':
        satellite_name = satellite_info.contents[4].text
        satellite_link = 'https://www.satbeams.com' + satellite_info.find('a', {'class':'link'}).get('href')
        #print(satellite_name)
        #print(satellite_status)
        #print(satellite_link)
        new_dict_value = '{satellite_name:satellite_link}'
        satellite_links_dict[satellite_name]=satellite_link
        count += 1
    else:
        pass
#Для planned надо получить info
#Для active info и картинки
#print(satellite_links_dict)
print('Всего записей: ', count)

time.sleep(2)

for key in satellite_links_dict:
    print(key)
    request_to_infopage = requests.get(satellite_links_dict[key])
    soup = BeautifulSoup(request_to_infopage.text, features='lxml')
    #print(soup)
    #Ищем позицию
    satellite_position = re.search(r'\(\d{1,3}.?\d?° [E|W]\)', str(soup.contents))
    try:
        satellite_position = satellite_position.group(0).strip('(').strip(')').replace(' ', '').replace('°', '')
        print(satellite_position)
    except AttributeError:
        pass

    try:
        satellite_folder = '.\\SatArea\\' + satellite_position
        os.mkdir(satellite_folder)
    except (FileExistsError, TypeError):
        pass

    #Ищем инфу
    try:
        satellite_info = soup.find('div', {'class': 'comments'})
        satellite_info = satellite_info.text
        print(satellite_info + '\n')
        try:
            with open(satellite_folder + '\\' + satellite_position + '.txt', 'a') as info:
                info.write(key + '\n' + satellite_info + '\n\n')
        except:
            pass

    except AttributeError:
        pass

    try:
        satellite_images = soup.find('td', {'class': 'beam_img'}).find_all('img')
        for satellite_image in satellite_images:
            #print(satellite_image)
            satellite_image = re.findall(r'(src=\".*?.jpg)', str(satellite_image))
            satellite_image_url = 'https://www.satbeams.com' + satellite_image[0].replace('src="', '')
            satellite_image_name = satellite_image[0].replace('src="', '').replace('/images/footprints/', '')
            print(satellite_image_url)
            h = httplib2.Http('.cache')
            response, content = h.request(satellite_image_url)
            out = open(satellite_folder + '\\' + satellite_image_name, 'wb')
            out.write(content)
            out.close()
        #print(satellite_images)
    except (AttributeError, IndexError):
        pass


