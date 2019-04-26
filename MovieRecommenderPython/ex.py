# -*- coding: utf-8 -*-

import wx
import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
class nig(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Movie Recommender',size=(300,300))
        panel=wx.Panel(self) 
        button=wx.Button(panel,label='exit',pos=(180,170),size=(40,30))
        pd.set_option('display.max_columns', 100)
        tf = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')
        tf = tf[['Title']]
        ls=[]
        for index,row in tf.iterrows():
            ls.append(row['Title'])
        list1 = wx.SingleChoiceDialog(self,"Enter a Movie","Movie Recommender",ls)
        if list1.ShowModal()==wx.ID_OK:
            txt=list1.GetStringSelection()
            self.calc(txt)
            with open("rname.txt","r+") as file:
                rname=file.read()
            wx.StaticText(self,-1,rname, (20,20))
        '''box=wx.TextEntryDialog(self,"Enter a name of the movie you have seen","Movie Recommender","Fargo")
        if box.ShowModal()==wx.ID_OK:
            txt=box.GetValue()
            self.calc(txt)
            with open("rname.txt","r+") as file:
                rname=file.read()
            wx.StaticText(self,-1,rname, (20,20))'''
        self.Bind(wx.EVT_BUTTON,self.closeb,button)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
    def closeb(self,event):
        self.Close(True)
    def calc(self,mname):
        pd.set_option('display.max_columns', 100)
        df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')
        df.head()
        df.shape
        df = df[['Title','Genre','Director','Actors','Plot']]
        df.head()
        df.shape
        # discarding the commas between the actors' full names and getting only the first three names
        df['Actors'] = df['Actors'].map(lambda x: x.split(',')[:3])

        # putting the genres in a list of words
        df['Genre'] = df['Genre'].map(lambda x: x.lower().split(','))

        df['Director'] = df['Director'].map(lambda x: x.split(' '))

        # merging together first and last name for each actor and director, so it's considered as one word 
        # and there is no mix up between people sharing a first name
        for index, row in df.iterrows():
            row['Actors'] = [x.lower().replace(' ','') for x in row['Actors']]
            row['Director'] = ''.join(row['Director']).lower()
        # initializing the new column
        df['Key_words'] = ""

        for index, row in df.iterrows():
            plot = row['Plot']

            # instantiating Rake, by default is uses english stopwords from NLTK
            # and discard all puntuation characters
            r = Rake()

            # extracting the words by passing the text
            r.extract_keywords_from_text(plot)

            # getting the dictionary whith key words and their scores
            key_words_dict_scores = r.get_word_degrees()

            # assigning the key words to the new column
            row['Key_words'] = list(key_words_dict_scores.keys())

        # dropping the Plot column
        df.drop(columns = ['Plot'], inplace = True)
        df.set_index('Title', inplace = True)
        df.head()
        df['bag_of_words'] = ''
        columns = df.columns
        for index, row in df.iterrows():
            words = ''
            for col in columns:
                if col != 'Director':
                    words = words + ' '.join(row[col])+ ' '
                else:
                    words = words + row[col]+ ' '
            row['bag_of_words'] = words

        df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)
        df.head()
        # instantiating and generating the count matrix
        count = CountVectorizer()
        count_matrix = count.fit_transform(df['bag_of_words'])

        # creating a Series for the movie titles so they are associated to an ordered numerical
        # list I will use later to match the indexes
        indices = pd.Series(df.index)
        indices[:5]
        # generating the cosine similarity matrix
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        cosine_sim
        # function that takes in movie title as input and returns the top 10 recommended movies
        def recommendations(title, cosine_sim = cosine_sim):
            rm=""
            try:   
                recommended_movies = []

                # gettin the index of the movie that matches the title
                idx = indices[indices == title].index[0]

                # creating a Series with the similarity scores in descending order
                score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

                # getting the indexes of the 10 most similar movies
                top_10_indexes = list(score_series.iloc[1:11].index)

                # populating the list with the titles of the best 10 matching movies
                for i in top_10_indexes:
                    recommended_movies.append(list(df.index)[i])
                
                for i in range(len(recommended_movies)-1):
                    rm=rm+"\n"+recommended_movies[i]
            except IndexError:
                rm="Movie not in dataset"
            finally:
                with open("rname.txt","w+") as file:
                    file.seek(0)
                    file.write(rm)
        recommendations(mname)
if __name__=='__main__':
    app=wx.App()
    frame=nig(parent=None,id=-1)
    frame.Show()
    app.MainLoop()








