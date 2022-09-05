#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd


# fail
def main():
    df = pd.DataFrame()
    df.to_parquet('sample.parquet', compression='gzip')


if __name__ == "__main__":
    main()
