# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import codecs
from wordcloud import WordCloud
import random
__author__ = 'BrownWong'

"""
模块功能：
    根据已分好词的文本生成词云
"""


def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """
    :param word:
    :param font_size:
    :param position:
    :param orientation:
    :param random_state:
    :param kwargs:
    :return:
    Description:
        调配词云中文字的颜色
    """
    return "hsl(210, 100%%, %d%%)" % random.randint(10, 80)  # 这里以蓝色为基本色调

text = codecs.open(r'C:\Users\Administrator\Desktop\python\1.txt', 'r').read()
# 切分好词的纯文本(我这里并没有设置分词工具，这里我是用的文本是已经切好的，并去除了停用词的文本)
phone_mask = np.array(Image.open(r'C:\Users\Administrator\Desktop\python\2.jpg'))
# 词云形状的来源图片
wc = WordCloud(background_color="white", max_words=2000, mask=phone_mask,
               font_path=r'C:\Windows\Fonts\simfang.ttf', width=800, height=400)  # 需设置中文字体
wc.generate(text)
wc.recolor(color_func=color_func, random_state=3)  # 更改原先色调
plt.imshow(wc)
plt.axis("off")
plt.show()