import json


def save_as_txt(dic):
    """以txt格式存储字典，键为文件名，值为文本内容，一个键值对一个txt"""
    for k, v in dic.items():
        filename = k
        with open(filename, 'w',encoding='utf-8') as file:
            file.write(v)


def save_as_json(dic):
    """以json格式存储dic"""
    file = f'{dic}_dic.json'
    with open(file, 'w',encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False)


def load_json(_json):
    """加载json"""
    file = _json
    try:
        with open(file) as f:
            dic = json.load(f)
    except FileNotFoundError:
        print(f"找不到文件{file}")
    else:
        return dic


def load_txt(_txt):
    """加载单个txt,存为字典，{xxx.txt：内容}"""
    file = _txt
    ndic = {}
    try:
        with open(file,encoding='utf-8') as f:
            content = f.read()  # content为txt的内容
    except FileNotFoundError:
        print(f"找不到文件{file}")
    else:
        ndic[_txt] = content
        return ndic
