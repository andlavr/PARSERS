import requests
from bs4 import BeautifulSoup
import random


def get_pikabu_random_link():

    url = 'https://pikabu.ru/new'
    connection_to_pikabu = requests.get(url)

    soup = BeautifulSoup(connection_to_pikabu.text, features='lxml')

    new_container = soup.find('div', {'class': 'stories-feed__container'})
    new_story = new_container.find_all('article', {'class': 'story'})

    page_links_dic = []

    for story_info in new_story:
        story_link_old = story_info.find('a', {'class': 'story__title-link'})
        story_link_new = story_link_old.get('href')
        page_links_dic.append(story_link_new)

    return random.choice(page_links_dic)


print(get_pikabu_random_link())





