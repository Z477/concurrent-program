#!/usr/bin/env python
# encoding: utf-8
'''
Use concurrent.futures to implement multi thread

Created on Jun 30, 2019
@author: siqi.zeng
@change: Jun 30, 2019 siqi.zeng: initialization
'''

import concurrent.futures
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def drink_water(name):
    time.sleep(2)
    logging.info("%s finish drink", name)
    return "result of {}".format(name)


def eat_food(name):
    time.sleep(2)
    logging.info("%s finish eat", name)
    return "result of {}".format(name)


def do_sports(name):
    time.sleep(2)
    logging.info("%s finish do sports", name)
    return "result of {}".format(name)


def play_game(name):
    time.sleep(2)
    logging.info("%s finish play game", name)
    return "result of {}".format(name)


def watch_tv(name):
    time.sleep(2)
    logging.info("%s finish watch TV", name)
    return "result of {}".format(name)


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    logging.info("start")
    future_to_person = [executor.submit(drink_water, "A"), executor.submit(eat_food, "B"),
                        executor.submit(do_sports, "C"), executor.submit(play_game, "D"),
                        executor.submit(watch_tv, "E")]
    concurrent.futures.wait(future_to_person, timeout=5)
    for future_object in future_to_person:
        result = future_object.result()
        logging.info("%s", result)
    logging.info("end")
