#! /usr/bin/python3

import datetime
import pathlib
import os

import bing_wallpaper_changer
import desktoppr_wallpaper_changer
import natgeopod_wallpaper_changer
import pod_wallpaper_changer
import unsplash_wallpaper_changer
import wikipedia_wallpaper_changer

SHOW_DEBUG = True


# Directory to save images
if os.path.exists("F:") is True:
    saveDirBing = "F:\\WallPaper\\Bing\\"
    saveDirAPoD = "F:\\WallPaper\\APoD\\"
    saveDirUnsplash = "F:\\WallPaper\\Unsplash\\"
    saveDirSpace = "F:\\WallPaper\\Space\\"
    saveDirNatGeoPoD = "F:\\WallPaper\\NatGeoPoD\\"
    saveDirDesktoppr = "F:\\WallPaper\\Desktoppr\\"
    saveDirWikipedia = "F:\\WallPaper\\Wikipedia\\"

else:
    saveDirBing = os.path.join(os.getcwd(), r'WallPaper\\Bing\\')
    saveDirAPoD = os.path.join(os.getcwd(), r'WallPaper\\APoD\\')
    saveDirUnsplash = os.path.join(os.getcwd(), r'WallPaper\\Unsplash\\')
    saveDirSpace = os.path.join(os.getcwd(), r'WallPaper\\Space\\')
    saveDirNatGeoPoD = os.path.join(os.getcwd(), r'WallPaper\\NatGeoPoD\\')
    saveDirDesktoppr = os.path.join(os.getcwd(), r'WallPaper\\Desktoppr\\')
    saveDirWikipedia = os.path.join(os.getcwd(), r'WallPaper\\Wikipedia\\')

date = datetime.date.today()


def directoryCheck():
    # create the directory if it does not exist
    pathlib.Path(saveDirBing).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirAPoD).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirUnsplash).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirSpace).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirNatGeoPoD).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirDesktoppr).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirWikipedia).mkdir(parents=True, exist_ok=True)


def throw_choices():
    print("""Choice: ?
                0: NASA Astronomy Picture of the Day,
                1: Bing Image of the Day,
                2: Random Pictures from Unsplash,
                3: National Geographic PoD,
                4: Random Images from Desktoppr,
                5: Picture of the Day from Wikipedia""")

    choice = int(input())
    return choice


def main():
    choice = 0
    directoryCheck()
    choice = throw_choices()
    wp_bing = saveDirBing + 'bingwallpaper' + str(date) + '.jpg'
    wp_pod = saveDirAPoD + 'NASA_PoD' + str(date) + '.jpg'
    wp_unsplash = saveDirUnsplash + 'unsplash' + str(date) + '.jpg'
    wp_natgeo_pod = saveDirNatGeoPoD + 'NatGeo_PoD' + str(date) + '.jpg'
    wp_desktoppr = saveDirDesktoppr + 'Desktoppr' + str(date) + '.jpg'
    wp_wikipedia = saveDirWikipedia + 'Wikipedia' + str(date) + '.jpg'

    if choice == 1:
        bing_wallpaper_changer.change_wp(wp_bing, saveDirBing, SHOW_DEBUG)

    elif choice == 0:
        pod_wallpaper_changer.change_wp(
            wp_pod, saveDirAPoD, SHOW_DEBUG, date)

    elif choice == 2:
        unsplash_wallpaper_changer.change_wp(
            wp_unsplash, saveDirUnsplash, SHOW_DEBUG)

    elif choice == 3:
        natgeopod_wallpaper_changer.change_wp(
            wp_natgeo_pod, saveDirNatGeoPoD, SHOW_DEBUG)

    elif choice == 4:
        desktoppr_wallpaper_changer.change_wp(
            wp_desktoppr, saveDirDesktoppr, SHOW_DEBUG)

    elif choice == 5:
        wikipedia_wallpaper_changer.change_wp(
            wp_wikipedia, saveDirWikipedia, SHOW_DEBUG)


if __name__ == '__main__':
    main()
