# CONTRIBUTING

## Overview

The code is quite modular and here is a brief overview how it works.

There is a global variable `SHOW_DEBUG` which is taken as a parameter by almost all functions. If this is set to true it shows useful debugging info and a nice progress bar.

Inside the `lib` folder the python codes reside.

* `ballontip.py` sends a notification to the notification panel.

* `debug.py` prints download status bar on the terminal.

* `utils.py` does the following - 

    1. `save_image`: This takes url of image, path where the image will be saved locally and SHOW_DEBUG as parameters. It returns the path where the image is saved.

    2. `set_wallpaper_permanent`: This takes the path of the image where it is saved locally and SHOW_DEBUG as parameters. It changes the wallpaper to the specifies image and also sends a notification.

* If you want to add another source simply create a file in the `lib` folder and use the above functionalities.

## Getting Involved

This project is in its early stage of development and we need your help. Please open an issue if you have spotted a bug or create a pull request if you have added a cool feature! 

### Making a pull request

Please open a **new issue** before making any pull request. **Every pull request should have a reference to an issue**.

* First, fork this repository.

* Clone it using `git clone https://github.com/[username]/Desktop-Wallpaper-Changer.git`

* It is always recommended to make your changes in a new branch rather than master. So create a new branch using `git branch mybug`.

* Checkout into your new branch using `git checkout mybug`.

* Hack the code, kill the bug or introduce the new feature you had in mind, do all kinds of awesome stuff.

* After you are done add your changes using `git add --all`

* Commit your changes using git commit and provide a commit message: `git commit -m "<commit message>" `.

* After you have committed your changes push your changes to your forked repository using `git push origin mybug`.

* Finally create a pull request from github.

* If everything is alright then soon your changes will get merged or else you will be asked to make changes.

There should be **only one commit per pull request**.

Please try to make sure that your commit message and body follows the guidelines below.

* Commit message should be of the form : `fixes issue #[issue_number] - what you solved in one line`

* After Commit message there should follow a commit body where you can mention what you did in short or in detail.

* Please make sure that your code follows `PEP8` guidelines. You may read more at [here](https://pep8.org).

* Also keep your master branch always updated.

Please try to follow this format as it will be helpful for maintainers as well as co-developers/contributors to stay aligned.
