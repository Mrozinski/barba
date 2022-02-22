import dask.dataframe as ddf
import pandas as pd

#Funkcja zwraca duplikaty w zestawie danych na podstawie kolumny col 
def checkForDups(df, col):
    return df[df.duplicated(subset=[col], keep=False)]

#Funkcja usówa wszystkie duplikaty w danych
def dropDups(df, col, myKeep=False):
    return df.drop_duplicates(subset=[col], keep=myKeep)

#Funkcja zwraca mnogościową różnicę df1 - df2 na podstawie columny 'col'
def compare2df(df1, df2, col):
    df1.set_index(col,inplace=True)
    df2.set_index(col,inplace=True)
    return df1.drop(df2.index)
