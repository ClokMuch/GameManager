# GamesManager methods
# ver.1
# By Clok Much

import config

from os.path import isfile as winsys_isfile
from os.path import isdir as winsys_isdir
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.simpledialog import askstring
from tkinter import Tk, messagebox
import win32com.client
import pythoncom



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
        messagebox.showinfo(title="Tip", message=(tip_info + "\nSelect a volume in next form...\n\n\
                                                             Or select a folder to take its volume."))
        askdirectory_title = "Select a volume..."
    else:
        messagebox.showinfo(title="Tip", message=(tip_info + "\nSelect a folder in next form...."))
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


def get_a_file(tip=None, special_filetype=None, initial_selector_dir=config.Default.games_main_dir):
    """
    Get a game with tip.
    special_filetype: [(description, ['.exe', '.doc']), +++++]
    Return tuple: (game_full_path, file_type, file_dir)
    file_type: "game" - ".exe", "launcher" - ".cmd", ".bat", "other" - other.
    file_dir: with \\
    """
    if not tip:
        tip = "Select a file..."
    if not special_filetype:
        special_filetype = [('Executable game file', config.Default.games_file_type),
                            ('Game launcher file', config.Default.launcher_file_type)]
    Tk().withdraw()
    target = askopenfilename(title=tip, filetypes=special_filetype,
                             initialdir=initial_selector_dir)
    file_dir = "\\".join(target.replace("/", "\\").split('\\')[:-1]) + "\\"
    if target[-4:] in config.Default.games_file_type:
        result = (target, 'game', file_dir)
    elif target[-4:] in config.Default.launcher_file_type:
        result = (target, 'launcher', file_dir)
    else:
        result = (target, 'other', file_dir)
    return result


def create_a_shortcut(source, name, target_dir, icon=None):
    """
    Create a shortcut.
    :param source: Original game or launcher.
    :param name: Shortcut name with NO '.lnk'.
    :param target_dir: Folder where shortcut will appear.
    :param icon: Shortcut icon, need if target is a launcher.
    """
    if source[-4:] in config.Default.launcher_file_type:
        if not icon:
            return 'ERROR, launcher need an icon!'
        else:
            icon = icon + ', 0'
    else:
        icon = source + ', 0'
    shortcut = win32com.client.Dispatch("WScript.Shell").CreateShortCut(target_dir + name + '.lnk')
    shortcut.TargetPath = source
    shortcut.IconLocation = icon
    shortcut.save()

