import streamlit as st

st.title('welcome to streamlit')

# input

M1 = st.text_input('ENTER YOUR INPUT')
st.markdown(M1)

m2 = st.text_area('ENTER YOUR INPUT')
st.markdown(m2)

st.warning('please Enter your input')

st.success('updated successfully')

m3 = st.selectbox('please select',['python','java','SQL'])
st.markdown(m3)

m4 = st.multiselect('please select',['python','java','SQL'])
st.markdown(m4)

st.radio('please select',['python','java','SQL'])

st.sidebar.text_input('ENTER YOUR NAME')
st.sidebar.selectbox('please select',['python','java','SQL'])
st.sidebar.radio('please select',['python','java','SQL'])
