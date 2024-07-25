import pandas as pd

def read_data(path='~/data/parquet'):
    df = pd.read_parquet(path)
    return df

def top(n, dt, p):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    
    if p:
        r = tabulate(ddf, headers=["", "cmd", "cnt"], tablefmt="pipe")
    else:
        r = ddf
    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
