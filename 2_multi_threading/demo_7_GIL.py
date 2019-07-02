#!/usr/bin/env python
# encoding: utf-8
'''
Prove the existence of GIL

Created on Jun 28, 2019
@author: siqi.zeng
@change: Jun 28, 2019 siqi.zeng: initialization
'''
import time
from threading import Thread

import matplotlib.pyplot as plt


def my_counter(count_num):
    i = 0
    for x in range(count_num):
        i = i + 1
    return True


def single_run(count_num):
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter, args=(count_num,))
        t.start()
        t.join()
    total_time = time.time() - start_time
    return total_time


def multi_thread_run(count_num):
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter, args=(count_num,))
        t.start()
        thread_array[tid] = t
    for i in range(2):
        thread_array[i].join()
    total_time = time.time() - start_time
    return total_time


def draw_picture():
    numbers = [x for x in range(100000000, 300000000, 50000000)]

    x = range(len(numbers))
    time_single = []
    time_multi = []

    for number in numbers:
        single_time = single_run(number)
        multi_time = multi_thread_run(number)
        time_single.append(single_time)
        time_multi.append(multi_time)

    plt.plot(x, time_single, marker='o', mec='r', mfc='w', label='time_single')
    plt.plot(x, time_multi, marker='*', ms=10, label='time_multi')
    plt.legend()
    plt.xticks(x, numbers, rotation=1)

    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('count number')
    plt.ylabel("time")
    plt.title("Prove GIL")
    plt.show()


if __name__ == '__main__':
    draw_picture()
