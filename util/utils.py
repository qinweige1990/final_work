import os

import functools

# 定义装饰器
def debug_params(func):
    """打印函数的参数名和值"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # 获取函数参数名
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        # 将参数名和值组成字典
        args_dict = dict(zip(arg_names, args))
        # 更新字典，添加关键字参数
        args_dict.update(kwargs)
        # 打印参数名和值
        print(f"调用{func.__name__},参数如下：")
        for name, value in args_dict.items():
            print(f"{name} = {value}")
        # 调用原函数
        return func(*args, **kwargs)

    return wrapper_debug

def list_files_abs_path(directory):
    # This function will return a list of absolute file paths
    abs_file_paths = []

    for dirpath, dirnames, files in os.walk(directory):
        # dirpath is a string for the path to the directory
        # dirnames is a list of the names of the subdirectories in dirpath
        # files is a list of the names of the non-directory files in dirpath
        for file in files:
            # Construct the absolute path
            abs_path = os.path.abspath(os.path.join(dirpath, file))
            abs_file_paths.append(abs_path)

    return abs_file_paths