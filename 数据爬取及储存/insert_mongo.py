import pymongo as mg
from subdivision_all import subdivision_all2list

myclient=mg.MongoClient()
mydb=myclient['drug_database']
mycol=mydb['drugs']
x = mycol.insert_many(subdivision_all2list('index.txt'))

print(x)