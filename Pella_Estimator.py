#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd
get_ipython().system('pip install joblib')
import joblib

# Load the trained model
model = joblib.load(open("random_forest_price_model.pkl", "rb"))

st.title("Pella Windows & Doors Price Estimator")

# User input fields
category = st.selectbox("Category", ["Window", "Door"])
type_ = st.text_input("Type", "Fixed Frame")
line = st.text_input("Line", "Lifestyle")
exterior_finish = st.text_input("Exterior Finish", "Enduraclad Black")
interior_finish = st.text_input("Interior Finish", "Unfinished")
width = st.number_input("Width", min_value=1, max_value=200, value=95)
height = st.number_input("Height", min_value=1, max_value=200, value=71)
glass_type = st.text_input("Glass Type", "Insulated Dual Tempered")
number_of_lites = st.number_input("Number of Lites", min_value=1, max_value=20, value=6)
screen = st.selectbox("Screen", ["Yes", "No"])
number_of_panels = st.number_input("Number of Panels", min_value=1, max_value=10, value=1)

if st.button("Predict Price"):
    user_input = pd.DataFrame([{
        'category': category,
        'type': type_,
        'line': line,
        'exterior_color_/_finish': exterior_finish,
        'interior_color_/_finish': interior_finish,
        'width': width,
        'height': height,
        'glass_type': glass_type,
        'number_of_lites': number_of_lites,
        'screen': screen,
        'number_of_panels': number_of_panels
    }])
    prediction = model.predict(user_input)[0]
    st.success(f"Estimated Price: ${prediction:.2f}")


# In[3]:





# In[9]:


get_ipython().system('jupyter nbconvert --to script Pella_Estimator.ipynb')


# In[ ]:




