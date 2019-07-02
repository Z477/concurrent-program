#!/usr/bin/env python
# encoding: utf-8
'''
Serial execution
 
Created on Jul 02, 2019
@author: siqi.zeng
@change: Jul 02, 2019 siqi.zeng: initialization
'''
import logging
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def take_shower(name):
    logging.info("%s is taking shower", name)
    sleep(2)
    logging.info("%s finish take shower", name)


def dress_in_room(name):
    logging.info("%s is dressing", name)
    sleep(2)
    logging.info("%s finish dress", name)


def main():
    for name in ["A", "B", "C"]:
        take_shower(name)
        dress_in_room(name)


main()
