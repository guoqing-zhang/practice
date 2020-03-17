# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:44:21 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""
"""面向对象编程基础"""

# =============================================================================
# 把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），
# 通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现
# 类的特化（specialization）和泛化（generalization），通过多态（polymorphism）
# 实现基于对象类型的动态分派。
# =============================================================================

# 在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，
# 这样就可以将对象的动态特征描述出来

# 三大要素，封装、继承、多态

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)
            
# 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。            
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
    
    
# 私有属性：访问可见性
class Test:

    def __init__(self, foo):
        self.__foo = foo # 两个下划线表示私有属性

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)
# 私有属性无法访问，因此常常以单下划线开头表示属性是受保护的。    


if __name__ == "__main__":
    main()    


# 封装
from time import sleep


class Clock(object):
    """数字时钟"""
    
    def __init__(self, hour=0, minute=0, second=0):
        
        
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        
        self._second += 1
        if self._second ==60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
























    
    
