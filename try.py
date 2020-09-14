import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Tissue Biorepository")

df = pd.read_csv (r'C:\Personal Projects\Development\Web_app\web_application\Tissue_data.csv',  encoding= 'unicode_escape')

#selecting category
st.sidebar.subheader("Type")
Type_list = st.sidebar.selectbox('', df.Type.unique())
df = (df.loc[df['Type']== Type_list])


#selecting campus
st.sidebar.subheader("Campus")
Campus_list = st.sidebar.selectbox('', df.Campus.unique())
df = (df.loc[df['Campus']== Campus_list])

#slecting type of specimen
st.sidebar.subheader("Specimen")
Class_list = st.sidebar.multiselect('', df.Specimen.unique())
# Col_list = st.sidebar.selectbox("C", df.C.unique())
if Class_list == []:
    pass 
else:
    df = df[df['Specimen'].isin(Class_list)]
# df = (df.loc[df['Specimen']== Class_list])

#selecting type of tissue
st.sidebar.subheader("Select tissues")
Tissue = df['Type of tissue'].unique()
tissues_SELECTED = st.sidebar.multiselect('', Tissue)
if tissues_SELECTED == []:
    pass 
else:
    df = df[df['Type of tissue'].isin(tissues_SELECTED)]
    
#selecting preparation type
st.sidebar.subheader("Select type")
P_type = df['Preperation'].unique()
type_SELECTED = st.sidebar.multiselect('', P_type)
if type_SELECTED == []:
    pass 
else:
    df = df[df['Preperation'].isin(type_SELECTED)]


#selecting sex
st.sidebar.subheader("Select sex")
S_type = df['Sex'].unique()
Sex_SELECTED = st.sidebar.multiselect('', S_type)
if Sex_SELECTED == []:
    pass 
else:
    df = df[df['Sex'].isin(Sex_SELECTED)]

#selecting age range
st.sidebar.subheader("Input Min age (years)")
Min_age = st.sidebar.text_input('', 0) 
st.sidebar.subheader("Input max age (years)")
Max_age = st.sidebar.text_input('', 200) 
df = df[(df['Age'] >= int(Min_age)) & (df['Age'] <= int(Max_age))]

#selecting patient race
st.sidebar.subheader("Select race")
R_type = df['Race'].unique()
Race_SELECTED = st.sidebar.multiselect('', R_type)
if Race_SELECTED == []:
    pass 
else:
    df = df[df['Race'].isin(Race_SELECTED)]


#selecting Ethnicity
st.sidebar.subheader("Select Ethnicity")
E_type = df['Ethnicity'].unique()
E_SELECTED = st.sidebar.multiselect('', E_type)
if E_SELECTED == []:
    pass 
else:
    df = df[df['Ethnicity'].isin(E_SELECTED)]


# buttons = st.sidebar.radio("Collection year range", ("Default", "within last year", "within last 3 years", "within last 5 years", "within last 10 years"))

st.sidebar.subheader("Select year range")
values = st.sidebar.slider('', 1990, 2020, (1990, 2020))
if (values[0] == 1990) & (values[1] == 2020):
    df = df
else :
    df = df[(df['Procurment Year'] >= (values[0])) & (df['Procurment Year'] <= values[1])]

# if buttons == 'Default':
#     pass

# if buttons == 'within last year':
#     df = df[df['Procurment Year'] >= 2019]
    

# if buttons == 'within last 3 years':
#     df = df[df['Procurment Year'] >= 2017]
    
# if buttons == 'within last 5 years':
#     df = df[df['Procurment Year'] >= 2015]

# if buttons == 'within last 10 years':
#     df = df[df['Procurment Year'] >= 2010]

st.subheader('Total Cases: ')
st.write(len(df))
st.write(df) 




st.markdown(
    """
<style>
.sidebar .sidebar-content {
    max-width: 100%!important;
    background-image: linear-gradient(#008000,#008000);
    color: white ;
}
</style>
""", unsafe_allow_html=True,
)


st.markdown("""
<style>
body {
    color: white;
    background-color: #008000;
    etc. 
}
</style>
    """, unsafe_allow_html=True)


# html_design = """
# <div style="background-color:{};">
# </div>
# """
# st.markdown(html_design.format(bgcolor2),unsafe_allow_html=True)


# st.markdown("""<div style=background-image: linear-gradient(#008000,#008000);></div>""",unsafe_allow_html=True)