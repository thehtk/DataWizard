import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px


def missing_cell(data):
    shape=data.shape
    a=data.isnull().count()
    sum=0
    for i in a:
        sum+=i
    return shape[0]*shape[1]-sum

def missing_cell_per(data):
    shape=data.shape
    a=missing_cell(data)
    return (a/shape[0]*shape[1])*100

def duplicate(data):
    return data[data.duplicated(keep = 'last')].count()[0]

def stats(data):
    col=data.columns
    
    i = st.selectbox('Select column',col)
    st.header(i)
    st.write('Count : ',data[i].count())
    
    num=['float64','int64']
    if data[i].dtype=='O':
        st.write('Distinct : ',data[i].nunique())
        st.write('Missing : ',len(data[i])-data[i].isnull().count())
        a = data.groupby(['Area']).size()
        a=pd.DataFrame(a)
        
        fig = px.pie(values=a[0], names=list(a.index))
        
        st.plotly_chart(fig, use_container_width=True)
        
    elif data[i][1].dtype in num:
        st.write('Min : ',data[i].min())
        st.write('Max : ',data[i].max())
        zero = (data[i] == 0).sum()
        st.write('Zeors : ',zero)
        st.write('Mean : ',data[i].mean())
        st.write('Distinct : ',data[i].nunique())
        st.write('Missing : ',len(data[i])-data[i].isnull().count())
        st.line_chart(data[i])
        
def bi_graph(data):
    col=data.columns
    options = st.multiselect('Select any two columns',col,[col[0],col[1]],max_selections=2)
    
    fig = px.scatter(x=data[options[0]], y=data[options[1]],labels={'x':options[0], 'y':options[1]})
    
    st.plotly_chart(fig, use_container_width=True)
    
def heatmap(data):
    fig = px.imshow(data,x=data,y=data,)
    st.plotly_chart(fig, use_container_width=True)
    
    
