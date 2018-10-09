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
        potd_element = soup.find('meta', {'property': 'og:image'})
        photo_url = potd_element['content']
        return photo_url


def picpath_wikimedia(saveDir, SHOW_DEBUG):
    photo_url = getphotourl()
    wikimedia_path = saveDir + 'Wikimedia:' + str(date) + '.jpg'
    if SHOW_DEBUG:
        print('Download from:', photo_url)
    savelink = save_image(photo_url, wikimedia_path, SHOW_DEBUG)
    return savelink


def change_wp(wp_wikimedia, saveDir, SHOW_DEBUG):
    savelink = picpath_wikimedia(saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(savelink, SHOW_DEBUG)
