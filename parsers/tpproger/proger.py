import requests
from bs4 import BeautifulSoup
import random
import re


def get_tpproger_random_link():

    url = 'https://tproger.ru/'
    connection_to_tpproger = requests.get(url)

    soup = BeautifulSoup(connection_to_tpproger.text, features='lxml')

    new_container = soup.find('div', {'class': 'columns masonry main-page'})
    new_story = new_container.find_all('a', {'class': 'article-link'})
    page_links_dic = []

    for story_info in new_story:
        pattern = re.compile(r'href="(.*)" rel')
        page_links_dic.append(re.findall(pattern, str(story_info))[0])

    return random.choice(page_links_dic)


print(get_tpproger_random_link())








