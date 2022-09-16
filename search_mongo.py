import pymongo as mg

myclient=mg.MongoClient()
mydb=myclient['drug_database']
mycol=mydb['drugs']

myquery = { "药名": "珍珠" }

mydoc = mycol.find(myquery)
kk=mycol.find({'性味':{'$regex': '。'}},{'药名':True,'_id':False})
print(mydoc)
result = [doc for doc in kk]
all=''
'''for k in result:
    if k!={}:
        all+=k['贮藏']
print(all)'''

print(result)
