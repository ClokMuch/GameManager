# GamesManager - initial methods
# Dependencies: methods.py, config.py
# ver.1
# By Clok Much

import config, methods


def initialize_games_list(is_pool_list=False):
    """
    Create a games list
    is_pool_list = False: Create a games list in games dir;
    is_pool_list = True: Create a games pool list in external storage.
    """
    methods.Tk().withdraw()
    if not is_pool_list:
        with open(config.Default.games_main_dir + config.Default.games_list_sub, encoding='utf8', mode='a'):
            methods.messagebox.showinfo(title="Info", message="Select your game or launcher in next form...")
            target = methods.get_a_game(tip="Select your game or launcher...")



