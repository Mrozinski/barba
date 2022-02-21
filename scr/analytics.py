import dask.dataframe as ddf
import pandas as pd

def checkForDups(df, col):
    return df[df.duplicated(subset=[col], keep=False)]

def compare2df(df1, df2, col):
    return df1.drop(df1.join(df2.set_index(col).index))
