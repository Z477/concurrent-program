#!/usr/bin/env python
# encoding: utf-8
'''
Use asyncio to implement asynchronous
 
Created on Jun 29, 2019
@author: siqi.zeng
@change: Jun 29, 2019 siqi.zeng: initialization
'''

import asyncio
import logging
from time import sleep

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


async def take_shower(name):
    logging.info("%s go to take shower", name)
    sleep(1)
    logging.info("%s go to clean hair", name)
    await asyncio.sleep(1)
    logging.info("%s finish clean hair", name)
    sleep(1)
    logging.info("%s finish take shower", name)


async def main():
    task_A = asyncio.create_task(take_shower("A"))
    task_B = asyncio.create_task(take_shower("B"))
    task_C = asyncio.create_task(take_shower("C"))
    await asyncio.gather(task_A, task_B, task_C)


asyncio.run(main())
