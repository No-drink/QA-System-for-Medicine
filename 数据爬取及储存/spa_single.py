#爬取数据并为每个药品输出为一个txt文件，最后将所有药品输出到一个json文件，同时有一个txt类型的索引输出
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import SaveAndLoad as sl
import json

bro = webdriver.Edge()
#获取需要爬取的网页对象
bro.get('http://yaobw.cn/yaobw/book.do?flag=goBook&bookId=1')
bro.maximize_window
madical_all={}


with open('madical.txt', 'w',encoding='utf-8') as mad,open('index.txt','a',encoding='utf-8') as idx:
    #共有284页，对每页进行爬取
    for i in range(1,285):#285
    #每页共有20条数据，对这20条数据的“查看”按钮进行点击并在新页面中获取数据
        for n in range(2,22):
            madical={}
            handles=bro.window_handles
            bro.switch_to.window(handles[0])
            #考虑到最后一页可能不足20条数据，故加入try块捕获异常
            try:
                check=bro.find_element_by_xpath(f'/html/body/div/div[3]/div[3]/div[3]/table/tbody/tr[{n}]/td[5]/a')
                bro.execute_script("arguments[0].click();", check)
                handles=bro.window_handles
                bro.switch_to.window(handles[-1])
                name=bro.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/pre/center[1]/b').text
                context=bro.find_element_by_xpath('//*[@id="content_text"]').text
                madical[name]=context
                madical_all[name]=context
                sl.save_as_txt(madical)
                idx.write(f'{name} \n')
                mad.write(f'{name} : {context}\n\n')
                bro.close()
            except:
                continue
        try:    
            handles=bro.window_handles
            bro.switch_to.window(handles[0])   
            next=bro.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[3]/p/a[9]')      
            bro.execute_script("arguments[0].click();", next)
        except:
            break    

#将所有数据存为json文件
sl.save_as_json(madical_all)

# print(madical)   
