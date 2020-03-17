# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:48:12 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""

# 图像和办公文档处理

from PIL import pillow

image = Image.open('guido.jpg')
image.format, image.size, image.mode
image.show()

# 剪裁图像
rect = 80, 20 ,310 ,360
image.crop(rect).show()

# 缩放图像
size = 128 ,128
image.thumbnail(size)
image.show()
















