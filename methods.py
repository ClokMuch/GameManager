# GamesManager methods
# ver.1
# By Clok Much

import config

from os.path import isfile as winsys_isfile
from tkinter.filedialog import askdirectory
from tkinter import Tk, messagebox


def xprint(content=None):
    """
    costumed print
    input the content to be printed.

    This is the template for input tuple or list:
        [
        [(queue), ("Plants VS Zombies FinVer.")],
        [(default), ("Hollow Knight")],
        [(default), ("Control")],
        [(processing), ("Need For Speed Heat")]
        ]
    , it will output like this:
        1. Plants VS Zombies FinVer.    / queue color
        2. Hollow Knight                / default color
        3. Control                      / default color
        4. Need for Speed Heat          / processing color
    Practical no. depends on the len of list or tuple.

    if input None or not input, xprint will NOT output;
    if input others, xprint will work like print.
    """
    if (type(content) == list) or (type(content) == tuple):
        for item in content:
            try:
                print(item[0][0] + item[1] + item[0][1])
            except IndexError:
                print("############INNER ERROR ON xprint due to content index, please contact author to fix it.")
            else:
                pass
    elif not content:
        pass
    else:
        print(content)


def try_find_volume():
    """
    try to find a volume with games pool
    Find the target: Return driver litter in a list
    Not found: Return False
    """
    volume_list = []
    for i in range(67, 91):
        volume_litter = chr(i) + ":\\"
        if winsys_isfile(volume_litter + config.GamesPoolOfExternalStorage.pool_subdir
                         + config.GamesPoolOfExternalStorage.pool_games_list):
            volume = volume_litter
            volume_list.append(volume)
    if not volume_list:
        return False
    else:
        return volume_list


def get_a_dir(tip_info=None, is_volume=False):
    """
    Get a location via tkinter.filedialog.askdirectory
    if is_volume = True: will return the target's volume
    return a dir end with '\\'
    """
    if not tip_info:
        tip_info = ""
    Tk().withdraw()
    if is_volume:
        messagebox.showinfo(title="Tip", message=(tip_info + "Select a volume in next form...\n\n\
                                                             Or select a folder to take its volume."))
        askdirectory_title = "Select a volume..."
    else:
        messagebox.showinfo(title="Tip", message=(tip_info + "Select a folder in next form...."))
        askdirectory_title = "Select a folder..."

    target = askdirectory(title=askdirectory_title)

    if is_volume:
        target = target.replace("/", "\\")[:3]
        return target
    else:
        if target[-1] != '/':
            target = target.replace("/", "\\") + "\\"
        else:
            target = target.replace("/", "\\")
        return target


