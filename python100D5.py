# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:37:15 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""

# 找出所有水仙花数
for num in range(100, 1000):
    low = num % 100 #取余数
    mid = num // 10 % 10
    high = num //100
    if num == low**3 + mid**3 + high **3:
        print(num)
    
    
# 回文数
num = int(input('请输入一个正整数： '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('{:d}是回文数'.format(num))
else:
    print('{:d}不是回文数'.format(num))