

import streamlit as st
import pandas as pd 
import plotly.express as px 
st.set_page_config(layout='wide')

df = px.data.tips()


def page1():

    st.plotly_chart(px.histogram(data_frame=df , x = 'total_bill'))


def page2():

    st.plotly_chart(px.violin(data_frame=df , x = 'total_bill'))



def page3():

    st.plotly_chart(px.box(data_frame=df , x = 'total_bill'))

pages = {
    'histogram' : page1,
    'violin' : page2,
    'box' : page3
}

pg = st.sidebar.radio('Navigate between pages' , pages.keys())

pages[pg]()
