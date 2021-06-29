# GamesManager - initial methods
# Dependencies: methods.py, config.py
# ver.1
# By Clok Much

import config, methods


def get_a_game(pool_dir=None):
    """
    Get a game info.
    :return tuple: (game_full_name, game_full_path, game_icon, game_dir, game_state)
    """
    methods.Tk().withdraw()
    if not pool_dir:
        methods.messagebox.showinfo(title="Info", message="Select your game or launcher in next form...")
        target = methods.get_a_file(tip="Select your game or launcher...")
        # Create a full name and chk full name...
        full_name = ""
        while not full_name:
            full_name = methods.askstring('Name create...', "Give me the name of this game or launcher:\n" +
                                          target + '\nName should NOT over 150 or contain: / \\ ? * " | : < >')
            flag_len_of_full_name = False
            flag_symbols_of_full_name = False
            name_error_info = ""
            if len(full_name) > 150:
                flag_len_of_full_name = True
            for i in full_name:
                if i in config.Default.no_symbols:
                    flag_symbols_of_full_name = True
            if flag_len_of_full_name:
                name_error_info += "\n  Length of name is over 150, it should NOT over 150;"
            if flag_symbols_of_full_name:
                name_error_info += '\n  Name contains forbidden symbol(s), ' \
                                   'it should NOT contain: / \\ ? * " | : < > " ,'
            if name_error_info:
                full_name = ""
                name_error_info = "Re-input game or launcher name, tips:\n" + name_error_info
                methods.messagebox.showerror(title="Invalid name!", message=name_error_info)
            else:
                break
        if target[1] == "launcher":
            methods.messagebox.showinfo(title="Select an icon or true game file...",
                                        message="You select a launcher, " +
                                                "you need to select an icon or true game associate to the launcher" +
                                                "in next form.")
            icon = methods.askopenfilename(title="Select an icon or true game file associate to " + target[0],
                                           filetypes=[('True game or icon', [".exe", ".ico"])],
                                           initialdir=target[2])
        result = (full_name, target[0], icon, target[2], "enabled")
    elif pool_dir:
        pool_dir = methods.try_find_volume() + config.GamesPoolOfExternalStorage.pool_subdir
        methods.messagebox.showinfo(title="Info", message="Select your game or launcher in next form...")
        target = methods.get_a_file(tip="Select your game or launcher...",
                                    initial_selector_dir=pool_dir)
        # ↑ POINT-dual pool support coming soon...
        # Create a full name and chk full name...
        full_name = ""
        while not full_name:
            full_name = methods.askstring('Name create...', "Give me the name of this game or launcher:\n" +
                                          target + '\nName should NOT over 150 or contain: / \\ ? * " | : < >')
            flag_len_of_full_name = False
            flag_symbols_of_full_name = False
            name_error_info = ""
            if len(full_name) > 150:
                flag_len_of_full_name = True
            for i in full_name:
                if i in config.Default.no_symbols:
                    flag_symbols_of_full_name = True
            if flag_len_of_full_name:
                name_error_info += "\n  Length of name is over 150, it should NOT over 150;"
            if flag_symbols_of_full_name:
                name_error_info += '\n  Name contains forbidden symbol(s), ' \
                                   'it should NOT contain: / \\ ? * " | : < > " ,'
            if name_error_info:
                full_name = ""
                name_error_info = "Re-input game or launcher name, tips:\n" + name_error_info
                methods.messagebox.showerror(title="Invalid name!", message=name_error_info)
            else:
                break
        if target[1] == "launcher":
            methods.messagebox.showinfo(title="Select an icon or true game file...",
                                        message="You select a launcher, " +
                                                "you need to select an icon or true game associate to the launcher" +
                                                "in next form.")
            icon = methods.askopenfilename(title="Select an icon or true game file associate to " + target[0],
                                           filetypes=[('True game or icon', [".exe", ".ico"])],
                                           initialdir=target[2])
        result = (full_name, target[0], icon, target[2], "disabled")

    return result
