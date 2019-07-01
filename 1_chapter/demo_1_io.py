#!/usr/bin/env python
# encoding: utf-8
'''
Define some common function

Create on 06/16/2019
@author: Siqi Zeng

'''
import os


def read_write():
    base_dir = 'xxx'
    result_file = 'xxx/total.txt'
    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if os.path.isfile(file_path):
            content = read_file(file_path)
            write_file(result_file, content)


def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def write_file(file_path, content):
    with open(file_path, 'w+') as f:
        f.write(content)


read_write()
