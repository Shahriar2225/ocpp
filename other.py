import streamlit as st
import pandas as pd
import time

st.set_page_config(layout='wide')

# Read and apply custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
st.markdown('### OCPP Simulation')

# Load the data
df = pd.read_csv('charge_2.csv')
last_index = len(df) - 1  # Initialize with last index for initial data display

# Initialize session state to keep track of the current index
if 'index' not in st.session_state:
    st.session_state.index = 0

def update_data():
    if st.session_state.index < last_index:
        st.session_state.index += 1  # Increment index only if not at the end of data
    else:
        st.session_state.index = 0  # Reset index to loop through data again

def display_data():
    index = st.session_state.index
    data = df.iloc[[index]]

    # Create placeholders for metrics (empty on first run)
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Row A (placeholders are automatically positioned)
    st.markdown('### Charger 01')
    with col1:
        st.subheader('Voltage')
        st.subheader(f'{data["Voltage"].values[0]} V')
    with col2:
        st.subheader('Current')
        st.subheader(f'{data["Current"].values[0]} A')
    with col3:
        st.subheader('SoC')
        st.subheader(f'{data["SoC"].values[0]} %')
    with col4:
        st.subheader('Temperature')
        st.subheader(f'{data["Temperature"].values[0]} C')
    with col5:
        st.subheader('Cost')
        st.subheader(f'${data["cost"].values[0]}')
    with col6:
        st.subheader('Status')
        st.subheader(f'{data["Status"].values[0]}')

# Main loop to update and display data
i = 0
while True:
    update_data()
    display_data()
    time.sleep(0.5)  # Add a delay to make updates visible
    if i == len(df)-1:
        break
    else:
        i=i+1
        st.experimental_rerun()
