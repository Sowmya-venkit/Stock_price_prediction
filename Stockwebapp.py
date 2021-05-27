#Description: This is a stock market dashboard to show some charts and data on some stock
import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# Stock Market Web Application
 **Visually** show data on a stock! Date range from jan 2 ,2019 - may 4,2021""")
image = Image.open("C:/Users/sowmya ammu/Desktop/stock_image.png")
st.image(image,use_column_width=True)

st.sidebar.header('User Input')

def get_input():
    start_date=st.sidebar.text_input("Start Date","2019-01-02")
    End_date = st.sidebar.text_input("End Date", "2021-05-04")
    Stock_symbol = st.sidebar.text_input("Stock symbol", "AMZN")
    return start_date,End_date,Stock_symbol

def get_company_name(symbol: object):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'google':
        return 'google'
    else:
        'None'
def get_data(symbol,start,end):

 if symbol.upper() == 'AMZN':
    df=pd.read_csv("C:/Users/sowmya ammu/Desktop/0ffice Projects/stock price prediction/AMZNtest.csv")
 elif symbol.upper() == 'TSLA':
    df=pd.read_csv("C:/Users/sowmya ammu/Desktop/0ffice Projects/stock price prediction/TSLA.csv")
 elif symbol.upper() == 'google':
    df = pd.read_csv("C:/Users/sowmya ammu/Desktop/0ffice Projects/stock price prediction/stock_dataset/Google_Stock_Price_Test.csv")
 else:
    df =pd.DataFrame(column=['Date','Close','Open','Volume','Adj Close','High','Low'])

 start =pd.to_datetime(start)
 end=pd.to_datetime(end)

 start_raw=0
 end_raw=0

 for i in range(0,len(df)):
     if start<=pd.to_datetime(df['Date'][i]):
        start_raw=i
        break
 for j in range(0,len(df)):
     if end>=pd.to_datetime(df['Date'][len(df)-1-j]):
        end_raw=len(df)-1-j
        break
 return df.iloc[start_raw:end_raw+1,:]

start, end, symbol = get_input()
df = get_data(symbol,start,end)
company_name=get_company_name(symbol.upper())

st.header(company_name+"close price\n")
st.line_chart(df['Close'])

st.header(company_name+ "Volume\n")
st.line_chart(df['Volume'])

st.header('Data statistics')
st.write(df.describe())

