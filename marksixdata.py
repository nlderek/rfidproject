#import bs4 as bs
#import urllib.request
import pandas as pd
#import sys
import csv


dfs=pd.read_html('http://www.9800.com.tw/drop.asp')

df = pd.DataFrame(dfs[3])

#Number of Draws
adata = df[0]
adata_a = adata[20]
print(adata_a)

#Date of Draw
bdata = df[1]
bdata_a = bdata[20]
print(bdata_a)

#original serial
odata = df[3]
odata_a = odata[1:21]
odata_b = odata_a[20]
odata_c = odata_b.replace("&nbsp", ",")
print (odata_c)

#Seq serial
data = df[4]
data_a = data[1:21]
data_b = data_a[20]
data_c = data_b.replace("&nbsp", ",")
s = ","
seq= (adata_a,bdata_a,odata_c[0:2],odata_c[3:5],odata_c[6:8],odata_c[9:11],odata_c[12:14],odata_c[15:17],odata_c[18:19],odata_c[20:22],data_c[0:2],data_c[3:5],data_c[6:8],data_c[9:11],data_c[12:14],data_c[15:17],data_c[18:19],data_c[20:22])
number = s.join(seq) + "\r\n"
print(number)

with open('mark6.csv','a', newline='') as fd:
    fd.write(number)

#data.to_csv('log.csv', sep=',', encoding='utf-8')
#for df in dfs:
#    print(df)
#data = dfs.text
#out = csv.writer(open("log.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
#out.writerow(data_c)
#print (df[4])
