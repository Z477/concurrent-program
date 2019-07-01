#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Jun 30, 2019
@author: siqi.zeng
@change: Jun 30, 2019 siqi.zeng: initialization
'''

import logging
from time import sleep

import gevent

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def take_shower(name):
    logging.info("%s is go to take shower", name)
    sleep(1)
    logging.info("%s is go to clean hair", name)
    gevent.sleep(2)
    logging.info("%s finish clean hair", name)
    sleep(1)
    logging.info("%s finish take shower", name)
    return name


def main():
    task_A = gevent.spawn(take_shower, "A")
    task_B = gevent.spawn(take_shower, "B")
    task_C = gevent.spawn(take_shower, "C")

    gevent.joinall([
        task_A,
        task_B,
        task_C
    ])


main()
