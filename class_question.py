# 1.问题类型（暂定）：用倒排索引的：清热解毒（疗效）的药材有哪些？（liaoxiao）  治疗xxx（适应症）的有哪些？(shiyingzheng) 需要放置在xxx(存放条件）下的药材有哪些？(cunfang)
#               用切分后的词典的：xxx（药材名）的【】（条目名）是什么？(tiaomu)  xxx有不宜同用的药吗？(buyi)
# 2.question[0]=疗效/存放条件/（用切分后的词典的）药材名（liaoxiao）/(cunfang)/(buyi)（tiaomu）
#   question[1]=条目名（list）
# 如果需要雕花：切分（把药材与方法切开以后），药材建一个数据库（建图数据库也可以的，因为有相同的适应症与疗效、性味与归经，还有不能共用的东西）
import jieba


class Question:
    """定义question，内含define_question_type,find_key_word,"""

    def __init__(self, raw_question) -> object:  # Question类的属性们

        self.raw_question = raw_question  # 接收到的用户输入的问题原句
        self.fenci_question = []  # 初步处理后的问题原句，处理为分词
        self.question_type = ''  # 问题类型
        self.final_question = []  # 处理后的纯问题关键词组成，格式见第二条注释

        self.yaocai_key = []
        self.liaoxiao_key = []
        self.cunfang_key =['避热','防霉','冰冻','蜜封','密封','凉处','阴暗处','低温','防热','干燥', '阴暗', '避光', '遮光','凉暗','室温','冷暗','通风','阴凉']#人工筛选后结果
        self.buyi_key = ['同用', '共用', '一起', '同时']
        self.list_key = []

    def fenci(self):  # 对输入的问题原句进行分词,得出fenci_question
        jieba.add_word('同用', freq=None, tag=None)
        for word in self.list_key:
            jieba.add_word(word, freq=None, tag=None)
        raw_list = jieba.lcut_for_search(self.raw_question)  # 初步分词之后的wordlist里面有很多多余的东西
        # 去除多余内容
        buyao = [', ', ' ', '。', '，', '？', '～', ':', '.', '\n', '；', '、', '：', '（', '）', '-', '的', '吗',
                 '呢', ]  # 把不需要的词和标点去掉
        for item in buyao:
            while item in raw_list:
                raw_list.remove(item)  # 去除标点符号及不需要的词
        if '性味' in raw_list:
            raw_list.remove('性味')
            raw_list.append('性味与归经') #这个性味与归经老是被拆开
            raw_list.append('性味')#先看性味与归经，后看性味
        self.fenci_question = raw_list

    def find_type(self):  # 明确问题的类型,并获得部分关键词
        if not self.fenci_question:
            self.question_type = 'unknown'
        for word in self.fenci_question:  # 遍历分词后的问题
            # 判断是否是存放类
            # question[0] = 存放条件 / 疗效名 /（用切分后的词典的）药材名（liaoxiao）(cunfang)(buyi)（tiaomu）
            # question[1]=条目名（tiaomu）
            # find_type运行后，可获得（liaoxiao(cunfang)的question[0]，（tiaomu）的 question[1]
            # 未完成：（buyi）与（tiaomu）的question[0]（应存储药材名）
            # 其余三个已经完成final_question
            if word in self.cunfang_key:  # 分词后的问题中有存放'cunfang'相关关键词
                self.question_type = 'cunfang'
                self.final_question = [word]  # final_question[0] = 存放条件
                break

            elif word in self.buyi_key:  # 有不宜同用'buyi'相关关键词
                self.question_type = 'buyi'
                self.final_question = ['']
                break

            elif word in self.liaoxiao_key:  # 有疗效'liaoxiao'相关关键词
                self.question_type = 'liaoxiao'
                self.final_question = [word]  # final_question[0] = 疗效
                break

            elif word in self.list_key:  # 有【】内条目'tiaomu'相关关键词
                self.question_type = 'tiaomu'
                self.final_question = ['']
                self.final_question.append(word)  # final_question[1] = 条目名
                #print(self.final_question)
                break

            else:  # 无法判断的类型
                self.question_type = 'unknown'

    def find_other_key(self):
        if self.question_type == 'tiaomu' or self.question_type == 'buyi':
            for word in self.fenci_question:  # 遍历分词后的问题
                if word in self.yaocai_key:  # 有药材名
                    self.final_question[0] = word
                    #print(self.fenci_question)
                    #print(self.final_question)
                    return

            self.question_type = 'unknown'  # 没有药材名时，无法回答问题
            return
            #print(self.fenci_question)
        else:  # 其他类型不用做什么了，跑路
            return


#q = Question("可以和什么药材同用")
#q.fenci()
#q.find_type()
#q.find_other_key()
#print(q.fenci_question)
#print(q.question_type)
#print(q.final_question)
