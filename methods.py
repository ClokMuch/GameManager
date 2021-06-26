# GamesManager methods
# ver.1
# By Clok Much

import config

from os.path import isfile as winsys_isfile


def xprint(content=None):
    """
    costumed print
    input the content to be printed.

    This is the template for input tuple or list:
        [(queue), ("Plants VS Zombies FinVer."),
         (default), ("Hollow Knight"),
         (default), ("Control"),
         (processing), ("Need For Speed Heat")]
    , it will output like this:
        1. Plants VS Zombies FinVer.    / queue color
        2. Hollow Knight                / default color
        3. Control                      / default color
        4. Need for Speed Heat          / processing color
    Practical no. depends on the lens of list or tuple.

    if input None or not input, xprint will NOT output;
    if input others, xprint will work like print.
    """

def try_find_volume(target=None):
    """
    try to find a volume with target file(s)
    No input: Return False
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
    if len(devices_list) == 1:
        return devices_list[0]
    elif not devices_list:
        return False
    else:
        return devices_list
