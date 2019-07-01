#!/usr/bin/env python
# encoding: utf-8
'''
Module Description

Created on Jun 28, 2019
@author: siqi.zeng
@change: Jun 28, 2019 siqi.zeng: initialization
'''
import _thread
import logging
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

mylock = _thread.allocate()


def take_shower(name):
    logging.info("%s is taking shower", name)
    sleep(2)
    logging.info("%s finish take shower", name)


def dress_in_room(name):
    logging.info("%s is dressing", name)
    sleep(2)
    logging.info("%s finish dress", name)


def clear_body(name):
    take_shower(name)
    logging.info("%s is waiting for dress", name)
    mylock.acquire()
    dress_in_room(name)
    mylock.release()


def main():
    _thread.start_new_thread(clear_body, ("A",))
    _thread.start_new_thread(clear_body, ("B",))
    _thread.start_new_thread(clear_body, ("C",))
    # wait all thread end
    sleep(10)


if __name__ == '__main__':
    main()
