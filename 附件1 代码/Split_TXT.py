#-*- coding = utf-8 -*-
#@Time : 2022-09-15 11:24
#@Author : 穆永恒
#@File : Split_TXT.py
#@Software: PyCharm

"""按照行数分割txt文件"""

def split(path, number):
    # 读取源文件，文件名最好加上绝对路径
    with open(path, 'r', encoding='utf-8') as f:
        # 把数据写入列表
        wordlist = f.readlines()
        # 算出总行数
        length = len(wordlist)
    # 设置每个拆分文件的行数
    unit = number
    # 计算新文件的个数，如果总行数整除新文件行数，就取这个商的值，如果不整除，取商加1的值
    file_amount = length // unit + 1 if length % unit > 0 else length // unit
    # 遍历所有新文件
    for num in range(file_amount):
        # 计算新文件中第一行在源文件中对应的行号
        start = num * unit
        # 计算新文件中最后一行在源文件中对应的行号
        end = length if length < (num + 1) * unit else (num + 1) * unit
        # 写入新文件，文件名最好加上绝对路径
        with open(str(num + 1) + '.txt', 'w+', encoding='utf-8') as f:
            # 遍历新文件的所有行
            for i in range(start, end):
                # 把列表中的数据写入新文件
                f.write(wordlist[i])


if __name__ == '__main__':
    file_path = "D:\桌面\pytorch\wash_result.txt"
    count = len(open(file_path, 'rU', encoding='utf-8').readlines())
    print(count)

    num = input('输入每个拆分文件的行数：')
    split(file_path, int(num))