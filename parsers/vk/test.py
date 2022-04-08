#импорт библиотек
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
#import webbrowser
#import requests
#import string
import time


#путь к драйверу chrome
chromedriver ='C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


#переход на страницу входа
browser.get('https://m.vk.com/login')

#поиск тегов по имени
email = browser.find_element_by_name('email')
password = browser.find_element_by_name('pass')
time.sleep(2)

#добавление учетных данных для входа
email.send_keys('')
time.sleep(2)
password.send_keys('')
time.sleep(2)
login = browser.find_element_by_class_name('button.wide_button')

#нажатие на кнопку отправить
time.sleep(2)
login.click()

#переход на интересующую нас страницу
browser.get('https://m.vk.com/robert_t29?act=info')


#получение HTML-содержимого
html = urlopen('https://m.vk.com/robert_t29?act=info')
bs = BeautifulSoup(html.read(), "html.parser")
req = requests.get('https://m.vk.com/robert_t29?act=info')    #запрос HTML содержимого

id = browser.find_element_by_class_name("header__text")
print(id.text)

name = bs.find("h2", {"class": "op_header"}).string
print(name).string

status = bs.find("div",{"class": "OwnerInfo__rowInfo"})
print(status.text)

activity = bs.find("div",{"class": "pp_last_activity"}).string
print(activity).string

gorod_prozhivaniya = bs.find("div",{"class": "OwnerInfo__row OwnerInfo__row_black"})
print(gorod_prozhivaniya.text)

group = bs.find("div",{"class": "Menu__itemTitle"}).string
kol_group = bs.find("div",{"class": "Menu__itemCount"}).string
print(group).string
print(kol_group)

kolichestvo = browser.find_element_by_class_name("OwnerInfo__row.OwnerInfo__row_black")
print(kolichestvo.text)

osnovnaya_infa = browser.find_element_by_class_name("profile_info_cont")
print(osnovnaya_infa.text)

podarki = browser.find_element_by_class_name("slim_header.slim_header_black.clearfix")
print(podarki.text)

rod_gorod = browser.find_element_by_class_name("pinfo_row.pinfo_block")
print(rod_gorod.text)

phone = bs.find("div",{"class": "Menu__item Row"})
print(phone.text)




















#html = urlopen('https://m.vk.com/robert_t29?act=info')
#class content:
   # def init(self, url, title, body):
        #self.url = url
        #self.title = title
        #self.body = body
#bs = BeautifulSoup(html.read(), 'html.parser')
#req = requests.get('https://m.vk.com/robert_t29?act=info')
#def get_page(url):
    #if req.status_code == 200:
        #return BeautifulSoup(req.text, 'html.parser')
    #eturn None
#def news_from_vk(url):
    #bs = get_page(url)
    #if bs is None:
       # return bs
   # title = bs.find("h2", {"class": "op_header"})
    #lines = bs.find("div", {"class": "pp_status"})
    #body = '\n'.join
#content = news_from_vk('https://m.vk.com/robert_t29?act=info')
#if content is None:
    #print("Ошибка")
#else:
   #print('FAMILIA_IMYA_OTCHESTVO: {}'.format(content.title))
    #print('ADress: {}'.format(content.url))
    #print(content.body)
