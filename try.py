import streamlit as st
import pandas as pd
from datetime import datetime

st.title('My first app')

# IRD = 'C:\Personal Projects\Development\Web_app\web_application\iris_data.csv'
# df = pd.read_csv(IRD, parse_dates=['Class'])
# # st.write(df.loc[df['Class']=='versicolor'])
df = pd.read_csv (r'C:\Personal Projects\Development\Web_app\web_application\Tissue_data.csv',  encoding= 'unicode_escape')
# st.markdown("#### " +"What would you like to select?")

# selected_metrics = st.selectbox(
#     label="Choose...", options=['setosa','versicolor','virginica']
# )

#selecting category
st.title("Current searching")
Type_list = st.selectbox('type', df.Type.unique())
df = (df.loc[df['Type']== Type_list])


#selecting campus
st.title("Campus selection")
Campus_list = st.selectbox('campus', df.Campus.unique())
df = (df.loc[df['Campus']== Campus_list])

#slecting type of specimen
st.title("Select your Specimen type")
Class_list = st.selectbox('Specimen', df.Specimen.unique())
# Col_list = st.sidebar.selectbox("C", df.C.unique())
df = (df.loc[df['Specimen']== Class_list])

#selecting type of tissue
Tissue = df['Type of tissue'].unique()
tissues_SELECTED = st.multiselect('Select tissues', Tissue)
if tissues_SELECTED == []:
    pass 
else:
    df = df[df['Type of tissue'].isin(tissues_SELECTED)]
    
#selecting preparation type
P_type = df['Preperation'].unique()
type_SELECTED = st.multiselect('Select type', P_type)
if type_SELECTED == []:
    pass 
else:
    df = df[df['Preperation'].isin(type_SELECTED)]



# #selecting age range
# st.title("Age")
# P_type = df['Proc. Date'].unique()
# type(df['Proc. Date'][1])

# date_time_obj = datetime.strptime(df['Proc. Date'][1], '%m-%d-%y')


#selecting sex
S_type = df['Sex'].unique()
Sex_SELECTED = st.multiselect('Select sex', S_type)
if Sex_SELECTED == []:
    pass 
else:
    df = df[df['Sex'].isin(Sex_SELECTED)]
st.write(df)
