import json
import csv

f = open("xxx.json")  #替换成json文件
data = json.load(f)
f.close()
with open('xxx.csv', 'wb') as csvfile: #替换成需要的csv文件
    spamwriter = csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_ALL)
    for item in data:
        spamwriter.writerow([item["key1"],item["key2"]...] )  #修改成key值