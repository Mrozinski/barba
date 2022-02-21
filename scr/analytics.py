import dask.dataframe as ddf
import pandas as pd

def checkForDups(df, col):
    return df[df.duplicated(subset=[col], keep=False)]

def compare2df(df1, df2, col):
    df1.set_index(col,inplace=True)
    df2.set_index(col,inplace=True)
    return df1.drop(df2.index)
