# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:30:58 2018

@author: pbangale
"""
import pandas as pd
import goslate
import psycopg2


def postgrs_conn():
    conn = psycopg2.connect(database="iLead",user="postgres",password='password',host='localhost')
    #cur = conn.cursor()
    #df=pd.read_sql("Select * from emp_data", conn)
    #print(type(df))
    return conn
def read_prospect():
    conn = postgrs_conn()
    global df
    cursor = conn.cursor()
    cursor.execute("Select * from prospects")
    row = cursor.fetchall()
    df=pd.DataFrame(row)
    #print(df)
    conn.commit()
    cursor.close()
    conn.close()
    
   
def translate(df1):
    #read_prospect()
    global df
    #data=df
    df1=pd.DataFrame(df)
    
    #print(df1)
    gs=goslate.Goslate()
    df["1"]= df1[2].map(lambda x:gs.translate(x,"en"))
    print(df["1"])
    #p=df1[3].map(lambda x1:gs.translate(x1,"en"))
    #print(p)
    #return row
def data():
    read_prospect()
    df=pd.DataFrame(row)
    print(df)
read_prospect()
#data()
translate(df1=read_prospect())
#translate()

