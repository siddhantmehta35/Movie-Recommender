# -*- coding: utf-8 -*-

import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
with open(r'''C:\xampp\htdocs\WP\finalrm.txt''',"r+") as file:
    mname=file.read().split('&')
pd.set_option('display.max_columns', 100)
tf = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')
tf = tf[['Title','Year']]
titledic={}
year=''
for index, row in tf.iterrows():
    titledic[row['Title']]=row['Year']

for i in mname:
    if (i in titledic):
        year=year+"\n"+str(titledic[i])+"&"


with open(r'''C:\xampp\htdocs\WP\title.txt''',"w+") as file:
            file.seek(0)
            file.write(year)

desf = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')
desf = desf[['Title','Plot']]
descdic={}
desc=''
for index, row in desf.iterrows():
    descdic[row['Title']]=row['Plot']
for i in mname:
    if (i in descdic):
        desc=desc+"\n"+descdic[i]+"&"
with open(r'''C:\xampp\htdocs\WP\plot.txt''',"w+") as file:
            file.seek(0)
            file.write(desc)


postf=pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')
postf = postf[['Title','Poster']]
postdic={}
post=''
for index, row in postf.iterrows():
    postdic[row['Title']]=row['Poster']
for i in mname:
    if (i in postdic):
        post=post+"\n"+postdic[i]+"&"
with open(r'''C:\xampp\htdocs\WP\post.txt''',"w+") as file:
            file.seek(0)
            file.write(post)