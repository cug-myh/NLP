#-*- coding = utf-8 -*-
#@Time : 2022-09-15 11:30
#@Author : 穆永恒
#@File : Clean_Chinese_Text.py
#@Software: PyCharm

"""清洗中文文本"""

import re
import jieba
import os

#文件读取
def read_txt(filepath):
    file = open(filepath,'r',encoding='utf-8')
    txt = file.read()
    return txt

# 可用来匹配到所有汉字
def find_chinese (text):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese_text = re.sub(pattern,'',text)
    return chinese_text

#中文分词
def cut_word(text):
    # 精准模式
    jieba_list = jieba.cut(text, cut_all=False)
    return jieba_list

#去除停用词
def seg_sentence(list_txt):
    #读取停用词表
    stopwords = stopwords = read_txt('D:\桌面\pytorch\Chinese\stopwords-master\hit_stopwords.txt')
    seg_txt = [ w for w in list_txt if w not in stopwords]
    return seg_txt

# 获取目标文件夹的路径
filedir = os.getcwd()#+'\\English'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.txt文件，如果没有则创建
f = open('wash_result.txt', 'w', encoding="utf-8")


if __name__ == '__main__':
    # 需要清洗的中文文本的文件路径
    filepath = filedir + '\\' + "merge_result.txt"
    print(filepath)
    num = 0
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding='utf-8', errors='ignore'):
        text = str(line)
        chinese_text = find_chinese(text)  # 获取所有汉字
        chinese_cut = cut_word(chinese_text)  # 分词
        chinese_sentence = seg_sentence(chinese_cut)  # 去除停用词
        result = ''.join(chinese_sentence) # 将列表连接成字符串
        f.writelines(result)
        num = num + 1
        if num%1000 == 0:
            f.write('\n')
            print(num/1000, "清洗中，请稍后...")

    print("清洗中文文本完毕！")


