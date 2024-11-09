import streamlit as st, pandas as pd
from bs4 import BeautifulSoup
import requests
import time

st.header('Indian stock market dashboard')
ticker = st.sidebar.text_input('Symbol Code','INFY')
exchange = st.sidebar.text_input('Exchange','NSE')
try:
    url=f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class1="YMlKec fxKbKc"
    price = soup.find(class_=class1).text.strip()[1:].replace(",","")
    previous_close = soup.find(class_='P6K39c').text.strip()[1:].replace(",","")
    revenue = soup.find(class_='QXDnM').text
    news = soup.find(class_='Yfwt5').text
    about = soup.find(class_='bLLb2d').text

    dict1 = {'Price':price,
            'Previous close':previous_close,
            'Revenue of company':revenue,
            'Latest News': news,
            'Company Info': about

    }

    df = pd.DataFrame(dict1,index=["Extracted data"]).T
    st.write(df)
except:
    st.write("Symbol doesn't exist")   
