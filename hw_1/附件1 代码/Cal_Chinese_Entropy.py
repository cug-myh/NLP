#-*- coding = utf-8 -*-
#@Time : 2022-09-15 14:52
#@Author : 穆永恒
#@File : Cal_Chinese_Entropy.py
#@Software: PyCharm

"""计算中文汉字的熵"""


from collections import Counter
import math
import os
import pandas as pd

#文件读取
def read_txt(filepath):
    file = open(filepath,'r',encoding='utf-8')
    txt = file.read()
    return txt

#词频统计
def counter(txt):
    seg_list = txt
    c = Counter()
    for w in seg_list:
        if w != ' ' and w != '\n':
            c[w] += 1
    return c

# 计算汉字的熵
def cal_chinese_entropy(count_er, sum_value):
    # 计算每个单词的概率并存储到字典
    Pr_dic = {}
    for item in count_er.items():
        Pr_dic[item[0]] = item[1] / sum_value
    # 按照频率大小排列
    Pr_dic_sort = dict(sorted(Pr_dic.items(), key=lambda item: item[1], reverse=True))
    # 计算熵
    Hx = 0
    for key in Pr_dic:
        pr = Pr_dic[key]
        Hx += pr * math.log2(pr)
    Hx = -Hx
    return Pr_dic_sort, Hx

# 保存频数、概率和熵
def save(count_er, pr_dic_sort, hx, path):
    # 字母、个数和概率列表
    key = list(pr_dic_sort.keys())
    counts = sorted(count_er.values(), reverse=True)
    pr = list(pr_dic_sort.values())

    # 利用pandas模块先建立DateFrame类型，然后将三个上面的list存进去
    result_excel = pd.DataFrame()
    result_excel['汉字'] = key
    result_excel['个数'] = counts
    result_excel['概率'] = pr
    result_excel['熵'] = hx

    # 写入excel
    result_excel.to_excel(path)


if __name__ == '__main__':
    # 获取目标文件夹的路径
    filedir = os.getcwd() + '\\Chinese'
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(filedir)
    filepath = filedir + '\\' + "text10\\text10.txt"
    print(filepath)
    # 读取文件
    chinese_txt = read_txt(filepath)
    # 统计汉字个数
    chinese_counter = counter(chinese_txt)
    # 打印汉字计数器
    print(chinese_counter)
    print("共有", len(chinese_counter), "个不同的汉字！")
    sum_values = sum(chinese_counter.values())
    print("汉字个数为：", sum_values)
    # 计算汉字的概率和熵
    Pr_dic_sort, Hx = cal_chinese_entropy(chinese_counter, sum_values)
    print(Pr_dic_sort)
    print("汉字的熵为：", Hx)
    # 将汉字的概率、熵等信息保存
    save_path = filedir + '\\' + "text10\\test10.xls"
    save(chinese_counter, Pr_dic_sort, Hx, save_path)