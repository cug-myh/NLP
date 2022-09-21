#-*- coding = utf-8 -*-
#@Time : 2022-09-11 19:11
#@Author : 穆永恒
#@File : Merge_TXT.py
#@Software: PyCharm

"""合并一个文件夹下所有txt文件"""


import os

# 获取目标文件夹的路径
filedir = os.getcwd()+'\\English\\split'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.txt文件，如果没有则创建
f = open('merge_result.txt', 'w', encoding="utf-8")
i = 0
# 先遍历文件名
for filename in filenames:
    print(filename)
    i += 1
    print(i)
    if i > 0:
        filepath = filedir + '\\' + filename
        print(filepath)
        # 遍历单个文件，读取行数
        for line in open(filepath, encoding='utf-8', errors='ignore'):
            # print(str(line))
            f.writelines(line)
            # f.write('\n')
# 关闭文件
f.close()