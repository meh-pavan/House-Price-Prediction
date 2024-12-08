# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:07:38 2024

@author: PAVAN
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model 

house_model = pickle.load(open('House_Price_Prediction.sav', 'rb'))


#House Price Prediction


#page title
st.title('House Price Prediction Using ML')


#inputs for prediction
Total_Square_Feet = st.text_input('How Many Square Feets ?')
Rooms = st.text_input('How Many Rooms ?')


#code for Prediction
House_pred = ''

if st.button("House Price Prediction"):
    try:
        # Convert inputs to numeric values
        Total_Square_Feet = float(Total_Square_Feet)
        Rooms = float(Rooms)
        
        # Make prediction
        House_pred = house_model.predict([[Total_Square_Feet, Rooms]])
        
        # Display the result
        st.success(f"Your House Can Be Sold At Price(in $) :  {int(House_pred[0])}")
    except ValueError:
        st.error("Please enter valid numeric values for both fields.")