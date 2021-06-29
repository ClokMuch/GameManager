# GamesManager
# ver.1
# By Clok Much

import config
import initial
import methods


methods.Tk().withdraw()

while True:
    # chk config.Default
    games_location = methods.winsys_isdir(config.Default.games_main_dir)
    if not games_location:
        tmp_message = "Your games' location in config.py is: %s , this folder is NOT exist!\n\n" \
                      "Solution:\nEdit: config.py - Default.games_main_dir to your game location.\n\n" \
                      "Press OK to exit." % config.Default.games_main_dir
        methods.messagebox.showerror(title="Invalid config!",
                                     message=tmp_message)
        exit()
    else:
        games_index_location = config.Default.games_main_dir + config.Default.games_shortcuts_subdir
        if not methods.winsys_isdir(games_index_location):
            tmp_message = "Your games' shortcuts in config.py is: %s (Full path: %s), this folder is NOT exist!\n\n" \
                          "Solution:\nEdit: config.py - Default.games_shortcut_subdir to your shortcut subdir.\n\n" \
                          "Press OK to exit." % (config.Default.games_shortcuts_subdir,
                                                 config.Default.games_main_dir + config.Default.games_shortcuts_subdir)
            methods.messagebox.showerror(title="Invalid config!",
                                         message=tmp_message)
            exit()
        else:
            initial.arrange_a_game()
