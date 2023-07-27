import os.path as osp
import os
import sys
import pandas as pd

def check_exits(path: str):
    if not osp.exists(path):
        return False
    return True


def check_is_file(path: str):
    if not osp.isfile(path):
        return False
    return True


def check_is_folder(path: str):
    if not osp.isdir(path):
        return False
    return True


def makedirs_folder(path: str):
    if not osp.exists(path):
        os.makedirs(path)