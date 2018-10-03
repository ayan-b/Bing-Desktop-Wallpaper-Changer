import datetime
from os import path

import requests

from utils import save_image, set_wallpaper_permanent

date = datetime.date.today()


def get_photourl():
    url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.gallery.json'
    source = requests.get(url)
    print(source)
    if source.status_code == 200:
        source_code = source.json()
        photo_url = source_code['items'][0]['sizes']['2048']
        return photo_url
    else:
        return "Proper URL not received"


def picpath_natgeo_pod(saveDir, SHOW_DEBUG):
    photo_url = get_photourl()
    natgeo_pod_path = saveDir + 'NatGeo_PoD' + str(date) + '.jpg'
    if SHOW_DEBUG:
        print("Download from: ", photo_url)
    savelink = save_image(photo_url, natgeo_pod_path, SHOW_DEBUG)
    return savelink


def change_wp(wp_natgeo_pod, saveDir, SHOW_DEBUG):

    if path.isfile(wp_natgeo_pod) is True:
        if SHOW_DEBUG:
            print('Nat Geo PoD Picture already found, updating that only')
        set_wallpaper_permanent(wp_natgeo_pod, SHOW_DEBUG)

    else:
        if SHOW_DEBUG:
            print('Picture is not in the system, updating process starts ...')
        savelink = picpath_natgeo_pod(saveDir, SHOW_DEBUG)
        set_wallpaper_permanent(savelink, SHOW_DEBUG)
