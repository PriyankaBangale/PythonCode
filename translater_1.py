# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:30:58 2018

@author: pbangale
"""
#https://stackoverflow.com/questions/52446811/why-googletrans-translator-suddenly-stopped-working
import pandas as pd
import goslate
import psycopg2
import textblob
from googletrans import Translator
from pandas import Series
import os

#from textblob import TextBlob 


def postgrs_conn():
    conn = psycopg2.connect(database="testdb",user="postgres",password='Priya@16',host='localhost')
    #cur = conn.cursor()
    #df=pd.read_sql("Select * from emp_data", conn)
    #print(type(df))
    return conn
def read_prospect():
    conn = postgrs_conn()
    #global X
    cursor = conn.cursor()
    df=pd.read_sql("Select * from x",conn)
   
    translator =Translator()
    get_translated = lambda x:translator.translate(x).text
    P=df.description.apply(get_translated)
    #Q=df.id.apply(get_translated)
    #print(Q)
    print(type(P))
    s = df['description']
   
    df1 = df.join(s.apply(lambda x: Series(x.split('LOT'))))
    clean_df =  df1[['description',0]]

    clean_df = clean_df.rename(index=str, columns={ 0: "Description"})
    clean_df['Description'] = clean_df['description']
    print(clean_df['Description'])
    del clean_df['description']


    if os.path.isfile("translated.csv"):
        os.remove("translated.csv")
    
    with open('translated.csv', 'a+') as file_obj:
        file_obj.write('Translated_Project_Description')
    for index, row in clean_df['Description'].iteritems():
        file_obj.write("\n")
       
        try:
            sys.stdout.write("\rTranslating row no\t:%d" % int(index))
            #sys.stdout.flush()
            file_obj.write(get_translated(row.encode('iso8859')))
        except:
            try:
                file_obj.write(get_translated(row.encode(sys.stdout.encoding)))
            except:
                try:
                    file_obj.write(get_translated(row.encode(sys.stdout.encoding)))
                except:
                    file_obj.write(row)

    df = pd.read_table("translated.csv")
    clean_df['Translated_Project_Description'] = df.values

    clean_df.to_csv("final.csv",index=False)
    
       

                   
    #return X
    #conn.commit()
    #cursor.close()
    #conn.close()
read_prospect()
#X=translate(X[1])
#read_prospect()

#data()
#translate(df1=read_prospect())
#translate()

