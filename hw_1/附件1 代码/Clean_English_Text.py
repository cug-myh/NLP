#-*- coding = utf-8 -*-
#@Time : 2022-09-11 20:30
#@Author : 穆永恒
#@File : Clean_English_Text.py
#@Software: PyCharm

"""清洗英文文本"""

import re
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag  # 分词、打词性标签
from nltk.stem import WordNetLemmatizer  # 用于词形还原
import os


def tokenize(sentence):
    '''
        去除多余空白、分词、词性标注
    '''
    sentence = re.sub(r'\s+', ' ', sentence)   # sub函数用来替换字符串中的内容，将所有类型的空白替换成一个空格
    token_words = word_tokenize(sentence) # 分词
    token_words = pos_tag(token_words)
    return token_words


wordnet_lematizer = WordNetLemmatizer()
def stem(token_words):
    '''
        词形归一化
    '''
    words_lematizer = []
    for word, tag in token_words:
        if tag.startswith('NN'):
            word_lematizer = wordnet_lematizer.lemmatize(word, pos='n')  # n代表名词
        elif tag.startswith('VB'):
            word_lematizer = wordnet_lematizer.lemmatize(word, pos='v')  # v代表动词
        elif tag.startswith('JJ'):
            word_lematizer = wordnet_lematizer.lemmatize(word, pos='a')  # a代表形容词
        elif tag.startswith('R'):
            word_lematizer = wordnet_lematizer.lemmatize(word, pos='r')  # r代表代词
        else:
            word_lematizer = wordnet_lematizer.lemmatize(word)
        words_lematizer.append(word_lematizer)
    return words_lematizer


sr = stopwords.words('english')   # 英语中的停用词列表
def delete_stopwords(token_words):
    '''
        去停用词
    '''
    cleaned_words = [word for word in token_words if word not in sr]
    return cleaned_words


def delete_characters(token_words):
    '''
        去除特殊字符、数字等，仅保留英文字母
    '''
    pattern = re.compile(r'[^a-zA-Z]')
    English_text = re.sub(pattern,'',token_words)
    return English_text


def to_lower(token_words):
    '''
        统一为小写
    '''
    words_lists = [x.lower() for x in token_words]
    return words_lists


# 获取目标文件夹的路径
filedir = os.getcwd()#+'\\English'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.txt文件，如果没有则创建
f = open('wash_result.txt', 'w', encoding="utf-8")


if __name__ == '__main__':

    filepath = filedir + '\\' + "merge_result.txt"
    print(filepath)
    num = 0
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding='utf-8', errors='ignore'):
        text = str(line)
        token_words = tokenize(text)  # 去除多余空白、分词、词性标注
        token_words = stem(token_words)  # 词性还原
        token_words = delete_stopwords(token_words)  # 删除停用词（包括be动词、连词等等）
        token_words = ''.join(token_words)
        token_words = delete_characters(token_words)  # 删除特殊字符、数字
        token_words = to_lower(token_words)  # 将大写转为小写
        f.writelines(token_words)
        f.write('\n')
        num = num + 1
        if num%1000 == 0:
            print(num/1000, "清洗中，请稍后...")
    print(num)
    print("清洗英文文本完毕！")


