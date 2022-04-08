from utils import get_responce_data
from settings import headers, proxies

print(get_responce_data("https://auto.ru/sankt-peterburg/cars/ford/all/", headers=headers, proxies=proxies))