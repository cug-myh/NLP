#-*- coding = utf-8 -*-
#@Time : 2022-09-11 17:25
#@Author : 穆永恒
#@File : Crawl_English_Text.py
#@Software: PyCharm

"""爬取英文文本"""

import requests
import parsel
from tqdm import tqdm


requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False # 关闭多余连接

def get_response(html_url):
    """
    获取网页响应（访问网页）
    :param html_url: 网址
    :return: 网页响应
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    response = s.get(url=html_url, headers=headers, timeout=5)

    response.encoding = response.apparent_encoding
    return response


def save(novel_name, title, content):
    """
    保存小说的每个章节
    :param novel_name: 小说名称
    :param title: 小说章节标题
    :param content: 章节内容
    :return:
    """
    filename = f'{novel_name}' + '.txt'
    # 一定要记得加后缀 .txt  mode 保存方式 a 是追加保存  encoding 保存编码
    with open(filename, mode='a', encoding='utf-8') as f:
        # 写入标题
        f.write(title)
        # 换行
        f.write('\n')
        # 写入小说内容
        f.write(content)
        f.write('\n\n')


def get_chapter_url(name, chapter_url):
    """
    爬取一章小说的内容并保存
    :param name:
    :param chapter_url:
    :return:
    """
    # 调用请求网页数据函数
    response = get_response(chapter_url)
    # 转行成selector解析对象
    selector = parsel.Selector(response.text)
    # 获取每一章的标题
    # showmain > div.title > span
    title = selector.css('#showmain .title span::text').get()
    # 获取每一章的内容
    # tt_text > div:nth-child(3)
    content_list = selector.css('#tt_text > div::text, #tt_text > div > a > strong::text').getall()
    # # ''.join(列表) 把列表转换成字符串并去除多余的空格
    content_str = ''.join(content_list).strip()
    #print(title, content_str)
    save(name, title, content_str)


def get_all_url(html_url):
    """
    访问小说，获取小说全部章节的url
    :param html_url:
    :return:
    """
    # 调用请求网页数据函数
    response = get_response(html_url+'list.html')  # 每一章
    # 转行成selector解析对象
    selector = parsel.Selector(response.text)

    # 小说名字
    # selector路径：showmain > div.title > span
    novel_name = selector.css('#showmain .title span::text').get()

    # 每一章节的链接
    lis = selector.css('#tt_text .clearfix li a::attr(href)').getall()

    for li in tqdm(lis):   # tqdm是添加进度条
        chapter_url = html_url+li
        get_chapter_url(novel_name, chapter_url)

    return novel_name



if __name__ == '__main__':
    #novel_id = input('输入书名ID：')
    for i in range(30):
        novel_id = 4807 + i
        novel_id = str(novel_id)
        url = f'http://novel.tingroom.com/jingdian/{novel_id}/'  #经典小说
        novel_name = get_all_url(url)
        print(novel_id,':', novel_name, "爬取完毕！")