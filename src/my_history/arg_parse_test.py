import pandas as pd
import argparse
import sys

def argp():
    parser = argparse.ArgumentParser(description="history search programm")
    group = parser.add_argument_group()
    group.add_argument("-c", "--count", type=str, action="store", help="my-history -c <cmd>")
    group.add_argument("-t", "--top", type=int, action="store", help="my-history -t <num>")
    group.add_argument("-d", "--date", type=str, action="store", help="my-history -d <date>")

    args = parser.parse_args()

    df = pd.read_parquet('~/data/parquet')

    if args.count:
        cnt(df, args.count)
    elif args.date or args.top:
        if args.date:
            df = date(df, args.date)
        if args.top:
            df = top(df, args.top)
        print(df)
    else:
        parser.print_help()

def cnt(df, q):
    fdf = df[df['cmd'] == q ]
    cnt = fdf['cnt'].sum()
    print(f'{q} 사용 횟수는 {cnt}회 입니다.')

def date(df, date):
    fdf = df[df['dt'] == date].sort_values(by='cnt', ascending=False)
    return fdf

def top(df, n):
    ddf = df.head(n).drop(columns=['dt']).to_string(index=False)
    return ddf
