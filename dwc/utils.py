import os
import urllib
from urllib.request import urlretrieve

from PIL import Image
import win32gui

from balloontip import balloon_tip
from debug import print_download_status


def save_image(url, picPath, SHOW_DEBUG):
    try:
        if SHOW_DEBUG:
            urlretrieve(url, picPath, print_download_status)
        else:
            urlretrieve(url, picPath)

    except urllib.error.HTTPError as e:
        print('HTTPError: %s. Exiting' % (str(e)))
        exit()

    except urllib.error.URLError as e:
        print('URLError: %s. Exiting' % (str(e)))
        os.remove(picPath)
        exit()

    except ConnectionAbortedError as e:
        print('ConnectionAbortedError: %s. Exiting' % (str(e)))
        os.remove(picPath)
        exit()

    except Exception as e:
        print('Some error occurred: %s. Exiting' % (str(e)))
        if os.path.isfile(picPath):
            os.remove(picPath)
        exit()

    if SHOW_DEBUG:
        print('URL retrieved')

    picData = Image.open(picPath)
    if SHOW_DEBUG:
        print('Image opened')
    picData.save(picPath)
    if SHOW_DEBUG:
        print('Saving ...')
    return picPath


def set_wallpaper_permanent(picPath, SHOW_DEBUG):
    if SHOW_DEBUG:
        print('Setting the wallpaper')
    win32gui.SystemParametersInfo(0x0014, picPath, 1+2)
    balloon_tip("Desktop Wallpaper Changer", "Wallpaper Updated!")
