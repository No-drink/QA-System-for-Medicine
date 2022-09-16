#不知道为什么那个insert跑不了，我就直接用test加工了一下输出一个json，加了药名的索引，然后再把id变成从0到n递增
#这个json可以直接进mongo的软件导入生成数据库（菜鸡只会用图形界面TAT）
import json
with open('test.json',encoding='utf-8') as f:
    dic=json.load(f)
kk=dic
n=0
for k in dic.keys():
        kk[k]['_id']=n
        kk[k]['药名']=k
        n+=1
print(kk)
file='new_dic.json'
with open(file, 'w', encoding='utf-8') as f:
    json.dump(kk, f)