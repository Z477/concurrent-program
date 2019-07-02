#!/usr/bin/env python
# encoding: utf-8
'''
Use threading to implement multi thread
 
Created on Jun 28, 2019
@author: siqi.zeng
@change: Jun 28, 2019 siqi.zeng: initialization
'''
import logging
from threading import RLock
from threading import Thread
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

mylock = RLock()


class clear_body(Thread):
    def __init__(self, consumer_name):
        Thread.__init__(self)
        self.name = consumer_name

    def take_shower(self):
        logging.info("%s is taking shower", self.name)
        sleep(2)
        logging.info("%s finish take shower", self.name)

    def dress_in_room(self):
        logging.info("%s is dressing", self.name)
        sleep(2)
        logging.info("%s finish dress", self.name)

    def run(self):
        self.take_shower()
        logging.info("%s is waiting for dress", self.name)
        mylock.acquire()
        self.dress_in_room()
        mylock.release()


def main():
    thread_list = [clear_body("A"), clear_body("B"), clear_body("C")]
    for thread in thread_list:
        thread.start()


main()
