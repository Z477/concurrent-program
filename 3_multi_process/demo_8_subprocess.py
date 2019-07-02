#!/usr/bin/env python
# encoding: utf-8
'''
Use subprocess to implement multi process
 
Created on Jun 29, 2019
@author: siqi.zeng
@change: Jun 29, 2019 siqi.zeng: initialization
'''

import subprocess

child = subprocess.Popen('ping -c 4 127.0.0.1', shell=True)
child.wait()
print(child.returncode)
print("parent process")
