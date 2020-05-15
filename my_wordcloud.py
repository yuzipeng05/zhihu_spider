# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/5/15
# @Software : PyCharm 
# @Python version: Python 3.7.2

import numpy as np
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def draw_word_cloud(word):
    words = jieba.cut(word)
    wordstr = " ".join(words)
    sw = set(STOPWORDS)
    stopwords = ['海尔','冰箱','这个','卡萨帝','品牌','西门子','还是','一个','可以','如果','就是','还是','但是']
    for i in  stopwords:
        sw.add(i)
    mask = np.array(Image.open('2.jpg'))
    wc = WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        mask=mask,
        max_words=200,
        max_font_size=100,
        stopwords=sw,
        scale=4,
    ).generate(wordstr)

    # 显示词云图
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 保存词云图
    wc.to_file('result.jpg')

if __name__ == "__main__":
    with open("卡萨帝冰箱怎么样_内容.txt", "rb") as f:
        word = f.read()
    draw_word_cloud(word)