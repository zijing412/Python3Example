#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###################################################
# Created : 2020-11-27 19:31:47
# Author : zijing (zijing412@163.com)
###################################################
"""
Topic: 正则式分割字符串
Desc : 
"""
import re


def split_str():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print(re.split(r'[;,\s]\s*', line))
    print(re.split(r'(;|,|\s)\s*', line))
    fields = re.split(r'(;|,|\s)\s*', line)
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(''.join(v+d for v,d in zip(values, delimiters)))

if __name__ == '__main__':
    split_str()
