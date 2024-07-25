import pandas as pd

def read_data(path='~/data/parquet'):
    df = pd.read_parquet(path)
    return df

def top():
    df = read_data()
    fdf = df[df['dt'] == '2024-07-12']
    sdf = fdf.sort_values(by='cnt', ascending=False).head(10)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
