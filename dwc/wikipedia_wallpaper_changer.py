import datetime

import requests
from bs4 import BeautifulSoup

from utils import save_image, set_wallpaper_permanent

date = datetime.date.today()
url = 'https://commons.wikimedia.org/wiki/Main_Page'


def getphotourl():
    source = requests.get(url)
    if source.status_code == 200:
        soup = BeautifulSoup(source.text, 'html.parser')
        potd_element = soup.find('div', {'id': 'mainpage-potd'})
        photo_url = potd_element.find('img')['src']
        return photo_url


def picpath_wikipedia(saveDir, SHOW_DEBUG):
    photo_url = getphotourl()
    wikipedia_path = saveDir + 'Wikipedia:' + str(date) + '.jpg'
    if SHOW_DEBUG:
        print('Download from:', photo_url)
    savelink = save_image(photo_url, wikipedia_path, SHOW_DEBUG)
    return savelink


def change_wp(wp_wikipedia, saveDir, SHOW_DEBUG):
    savelink = picpath_wikipedia(saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(savelink, SHOW_DEBUG)
