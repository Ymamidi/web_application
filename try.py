import streamlit as st
import pandas as pd

st.title('My first app')

# IRD = 'C:\Personal Projects\Development\Web_app\web_application\iris_data.csv'
# df = pd.read_csv(IRD, parse_dates=['Class'])
# # st.write(df.loc[df['Class']=='versicolor'])
df = pd.read_csv (r'C:\Personal Projects\Development\Web_app\web_application\iris_data.csv')
# st.markdown("#### " +"What would you like to select?")

# selected_metrics = st.selectbox(
#     label="Choose...", options=['setosa','versicolor','virginica']
# )


st.sidebar.title("Select your Class type")
State_list = st.sidebar.selectbox('Class', df.Class.unique())
st.write(df.loc[df['Class']==State_list])

