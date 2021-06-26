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
    # select the volume


def get_a_dir(is_dir=True):
    """
    选择一个路径，并返回以斜杠结尾的有效路径；
    对 is_dir 指定非 True 内容时，将再次选择，直到选择一个驱动器
    ▲ 这里有一个坑：获取目录的含树没有想到指定为我的电脑初始路径的方法
    这个函数可以尝试优化结构
    """
    loop_inct = True
    tmp = 0
    while loop_inct:
        tmp = askdirectory()
        if not tmp:
            loop_inct = True
            print('未选择任何路径，将再次选择...')
            showinfo(title="未选择驱动器", message="您取消选择，将重新自动检查设备路径.")
            return 'Cancel'
        else:
            if is_dir:
                tmp = tmp.replace("/", "\\") + '\\'
                loop_inct = False
            else:
                if tmp[-1] == '/':
                    tmp = tmp.replace("/", "\\")
                    loop_inct = False
                else:
                    print("选择的对象不是一个驱动器的根目录，请选择驱动器的根目录（C:\\等）")
                    showinfo(title="对象选择错误", message="请选择一个驱动器的根目录，如 C:\\ ，不要选择驱动器内的文件夹.")
    return tmp
