import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Tissue Biorepository")

df = pd.read_csv (r'C:\Personal Projects\Development\Web_app\web_application\Tissue_data.csv',  encoding= 'unicode_escape')

#selecting category
st.sidebar.title("Current searching")
Type_list = st.sidebar.selectbox('type', df.Type.unique())
df = (df.loc[df['Type']== Type_list])


#selecting campus
st.sidebar.title("Campus selection")
Campus_list = st.sidebar.selectbox('campus', df.Campus.unique())
df = (df.loc[df['Campus']== Campus_list])

#slecting type of specimen
st.sidebar.title("Select your details")
Class_list = st.sidebar.multiselect('Specimen', df.Specimen.unique())
# Col_list = st.sidebar.selectbox("C", df.C.unique())
if Class_list == []:
    pass 
else:
    df = df[df['Specimen'].isin(Class_list)]
# df = (df.loc[df['Specimen']== Class_list])

#selecting type of tissue
Tissue = df['Type of tissue'].unique()
tissues_SELECTED = st.sidebar.multiselect('Select tissues', Tissue)
if tissues_SELECTED == []:
    pass 
else:
    df = df[df['Type of tissue'].isin(tissues_SELECTED)]
    
#selecting preparation type
P_type = df['Preperation'].unique()
type_SELECTED = st.sidebar.multiselect('Select type', P_type)
if type_SELECTED == []:
    pass 
else:
    df = df[df['Preperation'].isin(type_SELECTED)]


#selecting sex
S_type = df['Sex'].unique()
Sex_SELECTED = st.sidebar.multiselect('Select sex', S_type)
if Sex_SELECTED == []:
    pass 
else:
    df = df[df['Sex'].isin(Sex_SELECTED)]

#selecting age range
Min_age = st.sidebar.text_input('Input min age (years)', 0) 
Max_age = st.sidebar.text_input('Input max age (years)', 200) 
df = df[(df['Age'] >= int(Min_age)) & (df['Age'] <= int(Max_age))]

#selecting patient race
R_type = df['Race'].unique()
Race_SELECTED = st.sidebar.multiselect('Select race', R_type)
if Race_SELECTED == []:
    pass 
else:
    df = df[df['Race'].isin(Race_SELECTED)]


#selecting Ethnicity
E_type = df['Ethnicity'].unique()
E_SELECTED = st.sidebar.multiselect('Select Ethnicity', E_type)
if E_SELECTED == []:
    pass 
else:
    df = df[df['Ethnicity'].isin(E_SELECTED)]


# buttons = st.sidebar.radio("Collection year range", ("Default", "within last year", "within last 3 years", "within last 5 years", "within last 10 years"))


values = st.sidebar.slider('Select year range', 1990, 2020, (1990, 2020))
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