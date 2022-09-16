# 运行这个打开qa界面
from class_question import Question
from class_answer import Answer
import jieba

import json
jieba.lcut_for_search('11')
with open('result.json', encoding='utf-8') as f:
    result = json.load(f)

with open('yaocai_key.json', encoding='utf-8') as f:
    yaocai_key = json.load(f)

with open('list_key.json', encoding='utf-8') as f:
    list_key = json.load(f)

with open('buyi_dic.json', encoding='utf-8') as f:
    buyi_dic = json.load(f)

with open('liaoxiao_key.json', encoding='utf-8') as f:
    liaoxiao_key = json.load(f)


print("初始化成功")

print("欢迎打开中国药典QA系统，请输入您的问题，输入q可退出")
while True:
    raw_question = input('Q:')
    if raw_question == 'q':
        break
    else:
        q = Question(raw_question)

        q.yaocai_key=yaocai_key
        q.list_key=list_key
        q.liaoxiao_key=liaoxiao_key

        q.fenci()
        q.find_type()
        q.find_other_key()
        a = Answer(q.final_question, q.question_type)
        a.result = result
        a.buyi_dic=buyi_dic
        a.find_answer()
        a.give_answer()

        print('A:', a.final_answer)
