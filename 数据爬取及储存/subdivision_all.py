from subdivision import subdivision
from subdivision import check

def subdivision_all(index):
    '''将索引中的药品全部分词并存在一个字典中'''
    madical_all={}
    n=0
    with open(f'{index}',encoding='utf-8') as fo:
        for line in fo:
            try:
                line=line.strip(' \n')
                if check(f'{line}'):
                    madical_all[f'{line}']=subdivision(f'{line}')
                    n+=1
                    print(n)
            except FileNotFoundError:
                continue        
    return madical_all


def subdivision_all2list(index):
    '''将索引中的药品全部分词并存在一个列表中'''
    madical_all=[]
    n=0
    with open(f'{index}',encoding='utf-8') as fo:
        for line in fo:
            try:
                madical_this={}
                line=line.strip(' \n')
                if check(f'{line}'):
                    madical_this=subdivision(f'{line}')
                    madical_this['药名']=f'{line}'
                    madical_all.append(madical_this)
                    n+=1
                    print(n)
            except FileNotFoundError:
                continue        
    return madical_all    