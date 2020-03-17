# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:31 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""
from random import randint



def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c

# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 函数名重复,使用模块解决,一个文件为一个模块
"""
需要说明的是，如果我们导入的模块除了定义函数之外还中有可以执行代码，
那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，
因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，
因为只有直接执行的模块的名字才是"__main__"。
"""

def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
"""
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
"""


def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x,y)

def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
        
def foo():
    global a # 修改全局变量
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200        
        
