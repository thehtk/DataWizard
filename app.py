import streamlit as st
import pandas as pd
from io import StringIO
import preprocess

uploaded_file = st.file_uploader("Choose a file")
 
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    col=data.columns
    
    st.header('Dataset statistics')
    shape=data.shape
    st.write('Number of variables : ',shape[1])
    st.write('Number of observations : ',shape[0])
    st.write('Missing cells	: ',preprocess.missing_cell(data))
    st.write('Missing cells (%) : ',preprocess.missing_cell_per(data))
    
    st.write('Duplicate rows : ',preprocess.duplicate(data))
    st.write('Duplicate rows (%) : ',preprocess.duplicate(data)*100/shape[0])
    st.write('Total size in memory : ',uploaded_file.size)
    st.write('Average record size in memory	: ',uploaded_file.size/shape[0])
    preprocess.stats(data)
    preprocess.bi_graph(data)
    preprocess.heatmap(data)


   