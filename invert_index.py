import re
import string
import codecs
import os
import json
from collections import Counter
from fenci import txt_fen_ci, sub_fenci, save_fenci
from SaveAndLoad import load_json, save_as_json

# 思路：对总txt进行分词，对爬虫所得字典的每个键值对里面的值也分词（避免出现奇奇怪怪的匹配），总txt分词list的每个词都在处理后的字典的键值对的值里面找一遍（避免巨量文件读操作），value匹配到了就标记一下key，就可得到倒排索引
# 参考：https://github.com/9ayhub/nlp-search-engine/blob/32a0adf7f1fc61a86b0b614e385e6d275a1f6f03/daopaisuoyin.py#L13
# 带#的代码都是测试用，无视就好
# 输出:result  格式: {word ：[所在文件1，所在文件2]...}    e.g{'干燥': ['八角茴香', '丁香']}

word_list = txt_fen_ci("madical.txt")
print('分词结果已传回')
# save_fenci('fenci.txt', word_list)

# 统计词频（不知道有什么用，但是教程里面都统计了）（草）（不统计了，先去重）
# dic_word_count = Counter(word_list)  # 存储方式：{k=词：y=词频（出现的次数）
# print(dic_word_count)
# 去重（去重提到fenci里去了，加快运行速度）
# word_list_ = set(word_list)  # 去重复
# word_list = list(word_list_)  # set转换成list, 否则不能索引
# 对词典进行分词

dic = load_json("dic.json")  # 先假设叫这个吧
for k, v in dic.items():
    v = sub_fenci(v)  # 能转list吗？
print('各药品条目分词已完成')
result = {}
for word in word_list:  # 总txt分词list的每个词都在处理后的字典的键值对的值里面找一遍（避免巨量文件读操作）
    for k, v in dic.items():  # 遍历分词过后的爬取的字典
        if word in v:  # 如果总txt分词中的某个词出现在字典里值的word list的话，就在result的那个word对应的值的list里面加上文件名
            if word in result.keys():  # append要在list非空时才能用
                result[word].append(k)
            else:
                result[word] = [k]
print("倒排索引result已生成")
file = 'result.json'
with open(file, 'w', encoding='utf-8') as f:
    json.dump(result, f)
print('result.json已生成')
