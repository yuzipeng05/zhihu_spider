# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/5/15
# @Software : PyCharm 
# @Python version: Python 3.7.2

from snownlp import SnowNLP
from pyecharts import Pie
import matplotlib.pyplot as plt
import numpy as np


def emotion_analysis(file):
    f = open(file, "r")
    comments = f.readlines()
    sentimentslist = []
    for comment in comments:
        s = SnowNLP(comment)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    # plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='red')
    # plt.xlabel('Sentiments Probability')
    # plt.ylabel('Quantity')
    # plt.title('Emotion Analysis')
    # plt.show()

    attr = ["很差", "较差", "一般", "较好", "很好"]
    v1 = [0 for i in range(5)]
    for i in sentimentslist:
        if i <= 0.2:
            v1[0] = v1[0] + 1
        elif 0.2 < i <= 0.4:
            v1[1] = v1[1] + 1
        elif 0.4 < i <= 0.6:
            v1[2] = v1[2] + 1
        elif 0.6 < i <= 0.8:
            v1[3] = v1[3] + 1
        else:
            v1[4] = v1[4] + 1
    pie = Pie('商品评价圆饼图')
    pie.add("", attr, v1,is_label_show=True)
    pie.render()


if __name__ == "__main__":
    emotion_analysis("卡萨帝冰箱怎么样_内容.txt")
