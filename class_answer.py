# 按照问题的分类给出回答
# 问题类型（暂定）：用倒排索引的：清热解毒（疗效）的药材有哪些？（liaoxiao）   需要放置在xxx(存放条件）下的药材有哪些？(cunfang)
#               用切分后的词典的：xxx（药材名）的【】（条目名）是什么？(tiaomu)  xxx有不宜同用的药吗？(buyi)
# raw_answer为一个列表，有根据问题类型有两种情况：
#   raw_answer[0]=条目名，raw_answer[1]=条目内容（tiaomu）
#   raw_answer=['药材1'，'药材2'……]（liaoxiao）(cunfang)(buyi)
import pymongo as mg
class Answer:
    def __init__(self,question,question_type):
        self.question=question
        self.question_type=question_type
        self.raw_answer=[]
        self.final_answer=''

        self.buyi_dic={}
        self.result={}


    def find_answer(self):#根据final_qusetion从处理后的数据或数据库中找答案
        if self.question_type == 'liaoxiao':
            self.raw_answer = self.result[self.question[0]]
        elif self.question_type == 'cunfang':
            self.raw_answer = self.result[self.question[0]]
        elif self.question_type == 'buyi':
            if self.question[0] in self.buyi_dic.keys():
                self.raw_answer = self.buyi_dic[self.question[0]]
                #print(self.raw_answer)
            else:
                return
        elif self.question_type == 'tiaomu':
            myclient = mg.MongoClient()
            mydb = myclient['drug_database']
            mycol = mydb['drugs']
            only_xingwei= ['九里香', '广枣', '小叶莲', '天山雪莲', '毛诃子', '冬葵果', '亚乎奴（锡生藤）', '藏菖蒲', '翼首草']
            if self.question[1]=='性味与归经' and self.question[0] in only_xingwei:
                self.question[1]='性味'#这几种药只有性味
            kk = mycol.find({"药名": self.question[0]}, {self.question[1]: True, '_id': False})
            result = [doc for doc in kk]
            #print(result)
            if result!=[{}] :#有这个条目
                self.raw_answer=['','']
                self.raw_answer[0] = self.question[1]
                self.raw_answer[1] = result[0][self.question[1]]
            else:
                self.question_type='no_tiaomu'


    def give_answer(self):#加工一下raw_answer,变成人话
        if self.question_type=='unknown':  # 无法解析的问题种类
            self.final_answer="无法回答该问题，请重新提问"
        if self.question_type == 'liaoxiao':
            _raw_answer = '，'.join(self.raw_answer)
            self.final_answer = f"有这一疗效的药材为：{_raw_answer}\n"
        elif self.question_type == 'cunfang':
            _raw_answer = '，'.join(self.raw_answer)
            self.final_answer = f"需要存放在该条件下的药材为：{_raw_answer}\n"
        elif self.question_type == 'buyi':
            if self.raw_answer:
                self.final_answer = f"{self.raw_answer}"
            else:
                self.final_answer='无不宜同用的药材\n'
        elif self.question_type == 'tiaomu':
            self.final_answer = f"该药材的{self.raw_answer[0]}为：{self.raw_answer[1]}"
        elif self.question_type == 'no_tiaomu':
            self.final_answer = f"该药材无条目{self.question[1]}"

