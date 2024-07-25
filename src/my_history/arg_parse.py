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

    if args.count:
        cnt(args.count)
    elif args.top and args.date:
        top(args.top, args.date)
    else:
        parser.print_help()
        perser.error("-t 옵션은 -d 옵션과 함께 사용하십시오.")

def cnt(q):
    df = pd.read_parquet('~/data/parquet')
    fdf = df[df['cmd'] == q ]
    cnt = fdf['cnt'].sum()
    print(f'{q} 사용 횟수는 {cnt}회 입니다.')

def top(n, date):
    df = pd.read_parquet('~/data/parquet')
    fdf = df[df['dt'] == date].sort_values(by='cnt', ascending=False).head(n)
    ddf = fdf.drop(columns=['dt']).to_string(index=False)
    print(ddf)

