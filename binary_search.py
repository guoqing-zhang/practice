# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:35:02 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""
# 二分法查找

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <=high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None            