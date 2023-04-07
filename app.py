import streamlit as st
import pandas as pd
import preprocess 
html_temp = """
    <div id="top-header"><center><u><i>
        <h1>Data Wizard</h1></i></u>
 </center>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
html_temp1 = """<b><hr></b>"""


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    col=data.columns
    st.markdown(html_temp1, unsafe_allow_html=True)
    st.subheader('Dataset statistics')
    shape=data.shape
    col1, col2 = st.columns(2)

    with col1:
        st.write('Number of variables : ',shape[1])
        st.write('Number of observations : ',shape[0])
        st.write('Missing cells	: ',preprocess.missing_cell(data))
        st.write('Missing cells (%) : ',preprocess.missing_cell_per(data))
    with col2:
        st.write('Duplicate rows : ',preprocess.duplicate(data))
        st.write('Duplicate rows (%) : ',round(preprocess.duplicate(data)*100/shape[0],2))
        st.write('Total size in memory : ',uploaded_file.size)
        st.write('Average record size in memory	: ',round(uploaded_file.size/shape[0],2))
    st.markdown(html_temp1, unsafe_allow_html=True)
    preprocess.stats(data)
    st.markdown(html_temp1, unsafe_allow_html=True)
    preprocess.bi_graph(data)
    st.markdown(html_temp1, unsafe_allow_html=True)
    preprocess.heatmap(data)
    st.markdown(html_temp1, unsafe_allow_html=True)
    preprocess.duplicate_row(data)
    st.markdown(html_temp1, unsafe_allow_html=True)
    preprocess.sample(data)
    st.markdown(html_temp1, unsafe_allow_html=True)


   
