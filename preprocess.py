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
    st.subheader('Variables Anlysis ')
    i = st.selectbox('Select a varaiable ',col)
    
    
    num=['float64','int64']
    if data[i].dtype=='O':
        col1, col2= st.columns(2)
        with col1:
            st.write('Count : ',data[i].count())
            st.write('Distinct : ',data[i].nunique())
            st.write('Missing : ',len(data[i])-data[i].isnull().count())
            a = data.groupby(['Area']).size()
            a=pd.DataFrame(a)
        with col2:
            fig = px.pie(values=a[0], names=list(a.index))
        
            st.plotly_chart(fig, use_container_width=True)
        
    elif data[i][1].dtype in num:
        
        col1, col2= st.columns(2)

        with col1:
            st.write('Count : ',data[i].count())
            st.write('Min : ',data[i].min())
            st.write('Max : ',data[i].max())
            st.write('Mean : ',round(data[i].mean(),2))

            zero = (data[i] == 0).sum()
            st.write('Zeors : ',zero)
            st.write('Distinct : ',data[i].nunique())
            st.write('Missing : ',len(data[i])-data[i].isnull().count())
        
        with col2:
            st.line_chart(data[i])
            
        
        with st.expander("More info"):
            tab1, tab2, tab3 = st.tabs(['Statistics','Histogram','Common values'])
            with tab1:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown('**Quantile statisticsl**')
                    st.write('Min : ',data[i].min())
                    st.write('5-th percentile : ',round(data[i].quantile(0.05),2))
                    st.write('Q1 : ',round(data[i].quantile(0.25),2))
                    st.write('Median : ',round(data[i].median(),2))
                    st.write('Q3 : ',round(data[i].quantile(0.75),2))
                    st.write('95-th percentile : ',round(data[i].quantile(0.95),2))
                    st.write('Max : ',data[i].max())
                    st.write('Range : ',data[i].max()-data[i].min())
                    st.write('IQR : ',round(data[i].quantile(0.95)-data[i].quantile(0.25),2))
                with col2:
                    st.markdown('**Descriptive statistics**')
                    u = np.mean(data[i])
                    s = np.std(data[i], ddof=1)                
                    cv = s / u
                    st.write('Standard deviation : ',round(s,2))
                    st.write('Coefficient of variation : ',round(cv,2))
                    st.write('Kurtosis : ',round(data[i].kurt(),2))
                    st.write('Mean : ',round(u,2))
                    st.write('Median Absolute Deviation : ',round(data[i].mad(),2))
                    st.write('Skewness : ',round(data[i].skew(),2))
                    st.write('Sum : ',round(data[i].sum(),2))
                    st.write('Variance : ',round(data[i].var(),2))
                    st.write('Monotonicity : ',data[i].is_monotonic)
                
            with tab2:
                fig = px.histogram(data[i], x=i)
                st.plotly_chart(fig, use_container_width=True)
            with tab3:
                st.write(data[i].value_counts().nlargest(10))
            
        
        
def bi_graph(data):
    col=data.columns
    st.subheader('Interactions')
    col1 , col2=st.columns(2)
    with col1:
        xaxis = st.radio("Select x axis",col)
    with col2:
        yaxis = st.radio("Select y axis",col)
        
    fig = px.scatter(x=data[xaxis], y=data[yaxis],labels={'x':xaxis, 'y':yaxis})
    st.plotly_chart(fig, use_container_width=True)
    
def heatmap(data):
    st.subheader('Heatmap')
    fig = px.imshow(data.corr(),text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
    
def duplicate_row(data):
    st.subheader('Duplicate Rows')
    a=data[data.duplicated()]
    if a.empty==True:
        st.write('No duplicate data avalible ')
    else:
        st.write(a)
        
def sample(data):
    st.subheader('Sample Data')

    tab1, tab2, tab3 = st.tabs(['First 10 rows', 'Last 10 rows', 'Any 10 rows'])

    with tab1:
        st.write(data.head(10))

    with tab2:
        st.write(data.tail(10))

    with tab3:
        st.write(data.sample(10))
    
