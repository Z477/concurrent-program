#!/usr/bin/env python
# encoding: utf-8
'''
Module Description

Created on Jun 30, 2019
@author: siqi.zeng
@change: Jun 30, 2019 siqi.zeng: initialization
'''

import concurrent.futures
import logging
import os
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def drink_water(name):
    time.sleep(2)
    logging.info("%s finish drink, pid:%s, ppid:%s", name, os.getpid(), os.getppid())
    return "result of {}".format(name), os.getpid()


def eat_food(name):
    time.sleep(2)
    logging.info("%s finish eat, pid:%s, ppid:%s", name, os.getpid(), os.getppid())
    return "result of {}".format(name), os.getpid()


def do_sports(name):
    time.sleep(2)
    logging.info("%s finish do sport, pid:%s, ppid:%s", name, os.getpid(), os.getppid())
    return "result of {}".format(name), os.getpid()


def play_game(name):
    time.sleep(2)
    logging.info("%s finish play game, pid:%s, ppid:%s", name, os.getpid(), os.getppid())
    return "result of {}".format(name), os.getpid()


def watch_tv(name):
    time.sleep(2)
    logging.info("%s finish watch TV, pid:%s, ppid:%s", name, os.getpid(), os.getppid())
    return "result of {}".format(name), os.getpid()


with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    logging.info("start %s", os.getpid())
    future_to_person = [executor.submit(drink_water, "A"), executor.submit(eat_food, "B"),
                        executor.submit(do_sports, "C"), executor.submit(play_game, "D"),
                        executor.submit(watch_tv, "E")]
    concurrent.futures.wait(future_to_person, timeout=5)
    for future_object in future_to_person:
        result = future_object.result()
        logging.info("%s pid: %s", result[0], result[1])
    logging.info("end %s", os.getpid())
