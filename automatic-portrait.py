#!/bin/python3

"""
This project will create an automatic display of pictures of what happend
today but years before.
"""

import os
import re
import shutil

ALBUMS_DIR = os.path.join(os.getcwd(), 'my_love')


def organize_pictures():
    """
    Function for organizaing the pictures according to date.
    """
    list_dir = os.listdir((ALBUMS_DIR))
    for picture in list_dir:
        regex_match = re.search('\d{8}', picture)

        if regex_match:
            date = str(regex_match.group())
            folder_name =  f'{date[-4:]}'
            try:
                os.mkdir(os.path.join(ALBUMS_DIR, folder_name))
            except FileExistsError:
                pass
        
        try:
            if folder_name in picture:
                shutil.move(os.path.join(ALBUMS_DIR, picture), 
                            os.path.join(ALBUMS_DIR, folder_name, picture))
        except UnboundLocalError:
            pass


def main():
    """
    Where the magic happens!
    """
    organize_pictures()


if __name__ == '__main__':
    main()

