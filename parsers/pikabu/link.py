import requests
from bs4 import BeautifulSoup
from lxml import html
import time
import os
import re
import httplib2
import sys

url = 'https://pikabu.ru/new'
Connection_to_Pikabu = requests.get(url)

if Connection_to_Pikabu.status_code == 200:
    print('Я в системе')
else:
    print('Вот этот код я вернул:', Connection_to_Pikabu.status_code)

soup = BeautifulSoup(Connection_to_Pikabu.text, features='lxml')

new_container = soup.find('div', {'class': 'stories-feed__container'})
# print (new_container)
new_story = new_container.find_all('article', {'class': 'story'})
# print(new_story)


count = 0
page_links_dic = []
file = open('Pikabu_finished_parser_for_Vlad.html', 'w', encoding='utf-8')

for story_info in new_story:
    try:
        story_title = story_info.find('h2', {'class': 'story__title'}).text
        # print(story_title)
    except:
        pass
    try:
        story_text = story_info.find('div', {'class': 'story-block_type_text'}).text
        # print(story_text)
    except (AttributeError, NameError):
        story_text = ""
    try:
        story_link_old = story_info.find('a', {'class': 'story__title-link'})
        story_link_new = story_link_old.get('href')
        page_links_dic.append(story_link_new)
        # print(page_links_dic, end= '\n')
    except:
        pass
    try:
        story_image_url_old = story_info.find('div', {'class': 'story-image__content'}).next_element.next_element
        story_image_url_new = story_image_url_old.get('src')
        # print(story_image_url_new)
    except(AttributeError, IndexError):
        story_image_url_new = ""
    try:
        story_text_hidden = story_info.find('div', {'class': 'story__hidden-blocks'}).text
        # print(story_text_hidden)
    except(AttributeError, IndexError):
        story_text_hidden = ""

    if count != 3:
        file.write('<h1>' + story_title + '<h2>')
        file.write('<br>' + story_text + '<br>')
        file.write('<br>' + story_text_hidden + '<br>')
        file.write('<img src=' + story_image_url_new + '>')
        file.write('<br>' + story_link_new + '<br>')
        count += 1
