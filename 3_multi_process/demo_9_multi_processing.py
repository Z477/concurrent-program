#!/usr/bin/env python
# encoding: utf-8
'''
Use multiprocessing to implement multi process
 
Created on Jun 29, 2019
@author: siqi.zeng
@change: Jun 29, 2019 siqi.zeng: initialization
'''
import logging
import os
from multiprocessing import Lock, Pool
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

mylock = Lock()


def take_shower(name):
    logging.info("%s is taking shower", name)
    sleep(2)
    logging.info("%s finish take shower", name)


def dress_in_room(name):
    logging.info("%s is dressing", name)
    sleep(2)
    logging.info("%s finish dress", name)


def clear_body(name):
    logging.info("sub process started>>> pid={},ppid={},name={}".format(os.getpid(), os.getppid(), name))
    take_shower(name)
    logging.info("%s is waiting for dress", name)
    mylock.acquire()
    dress_in_room(name)
    mylock.release()
    logging.info("sub process stoped>>> pid={},ppid={},name={}".format(os.getpid(), os.getppid(), name))
    return name


def main():
    logging.info("start parent process>>> pid={}".format(os.getpid()))
    ps = Pool(3)
    results = [ps.apply_async(clear_body, args=(name,)) for name in ["A", "B", "C"]]
    for result in results:
        print(result.get())
    ps.close()
    ps.join()
    print(" parent process stoped")


if __name__ == '__main__':
    main()
