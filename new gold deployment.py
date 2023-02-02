import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas import DataFrame
from pylab import rcParams
import plotly 
from plotly import graph_objs as go



st.title("Gold Price Predictor")

nav=st.sidebar.radio("Navigation",["Home","Data","Visualisation","Prediction"])

if nav == "Home":
    st.write("""
    This app predicts the **Daily Gold Price**!
    """)
    st.image("Gold image.jpg",width=500)

if nav == "Data":
    st.write("Data")
    #Import the Gold Dataset
    df = pd.read_excel(r"C:\Users\Tejasvi\Desktop\Gold\Gold_data.xlsx")
    df['Month'] = pd.to_datetime(df.date).dt.strftime('%b')
    df['Year'] = pd.to_datetime(df.date).dt.strftime('%Y')
    st.table(df)




if nav == "Visualisation":
    st.write("Visualisation")
    
    graph = st.selectbox("What kind of Graph ? ",["Line Plot","Average Gold Prices Yearwise","Original v/s Forecasted"])
    data=pd.read_excel(r"C:\Users\Tejasvi\Desktop\Gold\Gold_data.xlsx")
    data['Month'] = pd.to_datetime(data.date).dt.strftime('%b')
    data['Year'] = pd.to_datetime(data.date).dt.strftime('%Y')
    

    if graph == "Line Plot":  
        st.image("Gold graph.png")
        
    
    if graph == "Average Gold Prices Yearwise":   
        st.image("Average Price.png")
        
    

    if graph == "Original v/s Forecasted":   
        st.image("Forecasting.png",width=800)


if nav == "Prediction":
    dates = ['2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25', '2021-12-26', '2021-12-27', '2021-12-28',
         '2021-12-29', '2021-12-30', '2021-12-31', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04',
         '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11',
         '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18',
         '2022-01-19', '2022-01-20','2022-01-21']
    price = ['4312.7821', '4303.6339', '4318.0934', '4323.4805', '4345.3657',  '4363.6564',    '4360.6757',
         '4348.5714',     '4327.6739',     '4364.4554',    '4337.0930',    '4222.3403',     '4274.5556',    '4316.9404',
         '4383.8456',     '4354.6111',     '4296.5783',    '4310.0877',    '4322.1080',     '4403.6854',    '4342.2799',
         '4349.7068',     '4348.9574',     '4353.8943',    '4381.3280',    '4377.6380',     '4370.8730',    '4356.5252',
         '4336.7213',     '4332.5949','4313.6487']
    d1 = d1 = st.selectbox('Select Date', sorted(dates))
    if d1 == '2021-12-22':
        st.header(price[0])
    elif d1 == '2021-12-23':
        st.header(price[1])
    elif d1 == '2021-12-24':
        st.header(price[2])
    elif d1 == '2021-12-25':
        st.header(price[3])
    elif d1 == '2021-12-26':
        st.header(price[4])
    elif d1 == '2021-12-27':
        st.header(price[5])
    elif d1 == '2021-12-28':
        st.header(price[6])
    elif d1 == '2021-12-29':
        st.header(price[7])
    elif d1 == '2021-12-30':
        st.header(price[8])
    elif d1 == '2021-12-31':
        st.header(price[9])
    elif d1 == '2022-01-01':
        st.header(price[10])
    elif d1 == '2022-01-02':
        st.header(price[11])
    elif d1 == '2022-01-03':
        st.header(price[12])
    elif d1 == '2022-01-04':
        st.header(price[13])
    elif d1 == '2022-01-05':
        st.header(price[14])
    elif d1 == '2022-01-06':
        st.header(price[15])
    elif d1 == '2022-01-07':
        st.header(price[16])
    elif d1 == '2022-01-08':
        st.header(price[17])
    elif d1 == '2022-01-09':
        st.header(price[18])
    elif d1 == '2022-01-10':
        st.header(price[19])
    elif d1 == '2022-01-11':
        st.header(price[20])
    elif d1 == '2022-01-12':
        st.header(price[21])
    elif d1 == '2022-01-13':
        st.header(price[22])
    elif d1 == '2022-01-14':
        st.header(price[23])
    elif d1 == '2022-01-15':
        st.header(price[24])
    elif d1 == '2022-01-16':
        st.header(price[25])
    elif d1 == '2022-01-17':
        st.header(price[26])
    elif d1 == '2022-01-18':
        st.header(price[27])
    elif d1 == '2022-01-19':
        st.header(price[28])
    elif d1 == '2022-01-20':
        st.header(price[29])
    elif d1 == '2022-01-21':
        st.header(price[30])
    else:
        st.subheader('please select valid date')
    
    




