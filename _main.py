import pandas as pd
import streamlit as st

df = pd.read_csv("csv/c03.csv", encoding="utf-8")
print("head\n", df.head())
print("dtypes\n", df.dtypes)
print("describe\n", df.describe())

PREFECTURE_CHOICES = set(df["都道府県名"].unique())
AGE_CLASS = "総数"

prefecture = st.selectbox("都道府県名", PREFECTURE_CHOICES)


df = df[(df["都道府県名"] == prefecture) & (df["年齢5歳階級"] == AGE_CLASS)]

st.header(f"{prefecture}の人口推移（{AGE_CLASS}）")

if st.toggle("生データを表示"):
    st.dataframe(df)

st.line_chart(df, x="西暦（年）", y="人口（総数）")
st.area_chart(df, x="西暦（年）", y=["人口（総数）", "人口（女）"])