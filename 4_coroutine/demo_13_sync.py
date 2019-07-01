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
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def sync_process():
    sleep(1)


async def task(value):
    logging.info("task execute on %d", os.getpid())
    sync_process()
    logging.info("task finish on %d", os.getpid())
    return value * value


async def main():
    result = await asyncio.gather(task(2), task(3))
    logging.info("result %d %d", result[0], result[1])


asyncio.run(main())
