import pandas as pd
import streamlit as st
import datetime as dt

def main():

    data = {
        "新規陽性者数": "csv/newly_confirmed_cases_daily.csv",
        "重症者数": "csv/severe_cases_daily.csv",
        "死亡者数(累積)": "csv/deaths_cumulative_daily.csv",
    }

    date_from = dt.datetime(2020, 5, 9)
    date_to = dt.datetime(2023, 5, 9)

    st.header("コロナ")

    df = {}
    for d in data.keys():
        df[d] = pd.read_csv(data[d], encoding="utf-8", index_col=0)
        df[d].index = pd.to_datetime(df[d].index)
        df[d] = df[d][(df[d].index >= date_from) & (df[d].index < date_to)]

    key_first = next(iter(df))
    prefecture = st.selectbox("都道府県", ["ALL", *df[key_first].keys()[2:]])

    selected = st.multiselect("表示データ", df.keys(), df.keys())

    df_result = pd.DataFrame(index=df[key_first].index, columns=[])
    for d in df.keys():
        if d in selected:
            df_result[d] = df[d][prefecture]

    st.line_chart(df_result, y=selected)

if __name__ == '__main__':
    main()