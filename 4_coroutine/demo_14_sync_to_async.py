#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Jul 01, 2019
@author: siqi.zeng
@change: Jul 01, 2019 siqi.zeng: initialization
'''

import asyncio
import logging
import os
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def sync_process():
    sleep(1)


def task(value):
    logging.info("task execute on %d", os.getpid())
    sync_process()
    logging.info("task finish on %d", os.getpid())
    return value * value


async def main():
    thread_executor = ThreadPoolExecutor(max_workers=1)
    process_executor = ProcessPoolExecutor(max_workers=1)
    loop = asyncio.get_event_loop()
    logging.info("current pid %d", os.getpid())
    thread_future = loop.run_in_executor(thread_executor, task, 2)
    process_future = loop.run_in_executor(process_executor, task, 3)
    result = await asyncio.gather(thread_future, process_future)
    logging.info("result %d %d", result[0], result[1])


asyncio.run(main())
