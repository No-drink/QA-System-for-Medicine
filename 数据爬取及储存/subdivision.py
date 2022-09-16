import re

def check(name):
    '''判断该文件是否有【】条目'''
    with open(f'{name}',encoding='utf-8') as fo:
        all_inf=fo.read()
        all_inf.rstrip()
        characters=re.findall('【.*?】',all_inf)
        if characters:
            return True
        else:
            return False    


def subdivision(name):
    '''将每个药品分词形成字典并返回'''
    madical={}
    with open(f'{name}',encoding='utf-8') as fo:
            all_inf=fo.read()
            all_inf.rstrip()
            characters=re.findall('【.*?】',all_inf)
            contexts=re.findall('】[\s\S]*?【',all_inf)
            before=re.findall('[\s\S]*】',all_inf)
            last_0=all_inf.replace(before[0],'')
            last=re.search(f'.*\s\s',last_0)
            if not last:
                last=last_0
            else:
                last=last.group()    
            contexts.append(f'{last}')
            for i in range(len(characters)):
                name_this=characters[i].strip('【】\n')
                madical[f'{name_this}']=contexts[i].strip('【】\n')
    return madical

# print(subdivision('奥美拉唑肠溶片'))                