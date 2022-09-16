# 从两个dic中提取出适应症词库、【】条目词库、疗效词库、存放条件词库、药材名词库
# 疗效与适应症词库：功能
# 分成函数只是方便区分哪段代码是提哪个词库的
import json

import pymongo as mg
import fenci
import re


def find_yaocai_key():  # 提取药材名词库
    yaocai_key = []
    with open('index.txt', encoding='utf-8') as f:
        content = f.read()
    yaocai_key = content.split()
    print(yaocai_key)
    file = 'yaocai_key.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(yaocai_key, f)
    print('yaocai_key已生成')


def find_list_key():  # 【】内的条目名词库
    with open('test.json', encoding='utf-8') as f:
        test = json.load(f)
    list_key = []
    for k, v in test.items():
        for sub_k in v.keys():
            if not list_key:  # 如果list_key空
                list_key = [sub_k]
            if sub_k not in list_key:
                list_key.append(sub_k)
            else:
                continue
    print(list_key)
    file = 'list_key.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(list_key, f)
    print("list_key已生成")


def find_cunfang_key():  # 有人工筛选
    myclient = mg.MongoClient()
    mydb = myclient['drug_database']
    mycol = mydb['drugs']
    kk = mycol.find({}, {'贮藏': True, '_id': False})
    result = [doc for doc in kk]
    all = ''
    for k in result:
        if k != {}:
            all += k['贮藏']
    cunfang_key = fenci.sub_fenci(all)
    # print(all)
    # print(cunfang_key)
    cunfang_key = ['避热', '防霉', '冰冻', '蜜封', '凉处', '阴暗处', '低温', '防热', '干燥', '阴暗', '避光', '遮光', '凉暗', '室温', '冷暗', '通风',
                   '阴凉']  # 人工筛选后结果
    # 复制粘贴到question类里面


def buyi_dic():  # 用于搜索不宜同用药物的dic
    myclient = mg.MongoClient()
    mydb = myclient['drug_database']
    mycol = mydb['drugs']
    kk = mycol.find({'注意': {'$regex': '不宜与'}}, {'注意': True, '药名': True, '_id': False})
    result = [doc for doc in kk]
    buyi_dic = {}
    for k in result:
        i=k['注意']
        i=re.split(r'[‘宜’]', i)
        buyi_dic[k['药名']] = f'不宜{i[1]}'
    buyi_dic['草乌']='不宜与半夏、瓜蒌、瓜蒌子、瓜蒌皮、天花粉、川贝母、浙贝母、平贝母、伊贝母、湖北贝母、白蔹、白及同用。\n'#手动修改不规则数据
    buyi_dic['川乌']='不宜与半夏、瓜蒌、瓜蒌子、瓜蒌皮、天花粉、川贝母、浙贝母、平贝母、伊贝母、湖北贝母、白蔹、白及同用。\n    '
    print(buyi_dic)
    file = 'buyi_dic.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(buyi_dic, f)
    print('buyi_dic已生成')


def find_liaoxiao_key(): 
    myclient = mg.MongoClient()
    mydb = myclient['drug_database']
    mycol = mydb['drugs']
    kk = mycol.find({'功能与主治': {'$regex': '。'}}, {'功能与主治': True, '_id': False})
    result = [doc for doc in kk]
    liaoxiao_key = ''
    for k in result:
        i = ''
        i = k['功能与主治']
        i = i.split('。', 1)
        liaoxiao_key += f"{i[0]}，".strip()
    liaoxiao_key = re.split(r'[,:;：，、；]', liaoxiao_key)
    liaoxiao_key.remove('')
    word_list_ = set(liaoxiao_key)  # 去重复
    liaoxiao_key = list(word_list_)  # set转换成list, 否则不能索引
    print(liaoxiao_key)
    file = 'liaoxiao_key.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(liaoxiao_key, f)
    print('liaoxiao已生成')


#find_yaocai_key()
find_list_key()
#find_cunfang_key()'''
#buyi_dic()
#find_liaoxiao_key()
