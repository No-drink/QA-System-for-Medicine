import jieba
from SaveAndLoad import load_txt


def txt_fen_ci(txt):  # 给总txt做的分词，本来想给单个药材的txt也这样分词，但是怕py读这么多文件寄了
    # txt = "data.txt"
    raw_content = {}
    raw_content = load_txt(txt)
    word_list = []  # 存储分词结果
    word_list = jieba.lcut_for_search(raw_content[txt])# 分词，并将结果以列表形式存储
    print('总txt分词已完成')
    buyao = [', ', ' ', '。', '，', '【', '】', '～', ':', '.', '\n', '；', '、', '：', '（', '）', '-', '的', '取', '或', '有', '含',
             '加', '本品', '与']  # 把不需要的和标点去掉
    word_list_ = set(word_list)  # 去重复
    word_list = list(word_list_)  # set转换成list, 否则不能索引
    for item in buyao:
        while item in word_list:
            word_list.remove(item)  # 去除标点符号
    return word_list


def sub_fenci(v):  # 给爬取到的词典里面的值做分词，值的类型从string变为list
    word_list = []  # 存储分词结果
    word_list = jieba.lcut_for_search(v)  # 分词，并将结果以列表形式存储
    buyao = [', ', ' ', '。', '，', '【', '】', '～', ':', '.', '\n', '；', '、', '：', '（', '）', '-', '的', '取', '或', '有', '含',
             '加', '本品', '与']  # 把不需要的和标点去掉,如果想多了别的就再加点
    word_list_ = set(word_list)  # 去重复
    word_list = list(word_list_)  # set转换成list, 否则不能索引
    for item in buyao:
        while item in word_list:
            word_list.remove(item)  # 去除标点符号
    return word_list  # 代码重复就是本five TAT


def save_fenci(filename, word_list):
    # filename = 'fenci.txt'  # 将列表存入txt中
    with open(filename, 'w') as file:
        file.write(" ".join(word_list) + "\n")




"""print(word_list)
# print("/".join(jieba.lcut(seg_str)))    # 精简模式，返回一个列表类型的结果
# print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定
print("/".join(jieba.lcut_for_search(seg_str)))  # 搜索引擎模式"""
