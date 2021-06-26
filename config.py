# GamesManager configs
# ver.1
# By Clok Much

# suffix of dir is '\\'

class Default:
    games_main_dir = "D:\\Game\\"
    games_shortcuts_subdir = "!Index\\"
    games_list_sub = "games_lists"
    interrupt_inct_sub = "games_lists_interrupt"
    games_file_type = [".exe"]
    launcher_file_type = [".bat", ".cmd"]


class GamesPoolOfExternalStorage:
    # config for external storage of games
    auto_select_the_external_storage_pool = True
    pool_subdir = "Game\\"
    pool_games_list = "pool_game_list"


class MultiProcess:
    # config for multi-process
    main_switch = False
    multi_process = True
    process_bar = True


class ListOrder:
    # config for list order
    # If main_switch is False: order by game name.
    main_switch = False
    order_method = "name"
    """
    Supported modes:
        1. name : order by game name (Full name of game, not file name);
        2. date : order by added index;
        3. random : order randomly (not suggest).
    If not supported modes, list will be ordered by full game name.
    Do NOT edit supported modes beyond to avoid unexpectedness.
    """
    supported_modes = ["name", "date", "random"]


class XPrintColor:
    # config for print colors
    queue = ("\033[0;30;40m", "\033[0m")  # normal, fore-black, back-yellow.
    processing = ("\033[5;30;40m", "\033[0m")  # flash, fore-black, back-yellow.
    default = ("", "")  # nothing.
