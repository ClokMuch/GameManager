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
    if not is_pool_list:
        # select the games' dir
        initial_games_dir = methods.get_a_dir(tip_info="Firstly, select your games' dir which storages your all games.")
