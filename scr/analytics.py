import dask.dataframe as ddf
import pandas as pd

# Funkcja przyjmije jako argumenty: Ramkę  Danych Pandas oraz nazwę kolumny
# w której będzie szukać duplikatów
# zwraca ramkę danych zawierającą powtórzone wiersze 


def checkForDups(df, col):
    return df[df.duplicated(subset=[col], keep=False)]