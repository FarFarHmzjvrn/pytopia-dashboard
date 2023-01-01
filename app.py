import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image




# Login
login_option = st.sidebar.radio('Login/Singup', ('Login', 'Singup'))
if login_option == 'Login':
    with st.sidebar.form("login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("signup"):
        st.write("Singup Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Singup")
        if submitted:
            pass

# Banner
banner = Image.open('./data/banner.webp', )
st.image(banner)
st.title(':zap: Pytopia Dashboard')


#Metrics
col1, col2 = st.columns(2)
col1.metric(label="Pytopia Telegram Members", value="4800", delta="+100")
col2.metric(label="Pytopia Website Members", value="2102", delta="+10")


#Statistics
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)


#User Info
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')

# Questions
with st.expander('Q / A'):
    query = st.text_input('Search:')

    # select top 10 from messages
    for msg in Message.objects.all().order_by('-date'):
        if not msg.text or msg.text[-1] not in '؟?':
            continue

        if query and query not in msg.text:
            continue

        col1, col2 = st.columns([1, 4])
        col1.write(f'**{msg.user.username}**')
        col2.write(msg.text.replace(query, f'**{query}**'))

    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')
