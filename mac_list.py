#! /usr/bin/python

from urllib import urlopen
import re
import time
import pandas as pd


html = urlopen("http://linuxnet.ca/ieee/oui.txt")
raw_text=  (html.read())
time.sleep(5)

with open("mac_list.txt", "w") as text_file:
    text_file.write(raw_text)
seek_work = '(base 16)'

regex = ur"(base 16)|\t\t|\t|     |\)|\n|\("

f = open('mac_list.csv','wb')
last_line = None
for line in open("mac_list.txt", 'r'):
    for word in line:
        if (seek_work in line) and (last_line!=line):
            # print  re.sub(regex,',',line)
            last_line = line
            parsed_line = re.sub(regex,',',line)
            f.write(parsed_line)
            f.write('\n')
f.close()

time.sleep(2)


df = pd.read_csv('mac_list.csv', usecols=[0, 5],sep=",",names=['mac_List', 'vendor'])
df.to_csv("mac_list.csv")