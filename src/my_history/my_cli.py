import pandas as pd
import sys

def cnt(q):
    #df = read_parquet()
    df = read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()
    return cnt

def read_parquet():
    df = read_parquet("~/tmp/history.parquet")
    return df

def read_parquet(path):
    df = pd.read_parquet(path)
    return df

def query():
    q = sys.argv[1]
    i = cnt(q)
    print(f'질의:{q}에 대한 검색결과는 {i}입니다.')
