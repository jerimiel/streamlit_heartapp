import streamlit as st
import pandas as pd
import pickle
import numpy as np
import time

loaded_model = pickle.load(open('model.pkl','rb'))
data = pd.read_csv('heart.csv')


app_mode = st.sidebar.selectbox("Select page",["Home","Prediction"])

if app_mode == "Home":
    st.title("Heart disease dataset")
    st.markdown("Dataset :")
    st.write(data)
    df = data['HeartDisease'].value_counts()
    st.markdown("Class counts")
    st.bar_chart(df)
if app_mode == "Prediction":
    age = st.sidebar.number_input("Age")
    sex = st.sidebar.selectbox("Select gender",["F","M"])
    chest = st.sidebar.selectbox("Chest Pain type",["ASY","ATA","NAP","TA"])
    bp = st.sidebar.slider("Resting BP",0,180)
    cholesterol = st.sidebar.number_input("Cholesterol")
    fastingbs = st.sidebar.text_input("Fasting BS",0,1)
    ecg = st.sidebar.selectbox("Resting ECG",["LVH","Normal","ST"])
    hr = st.sidebar.number_input("Max HR")
    exercise = st.sidebar.checkbox("Exercise Angina(Y/N)")
    oldpeak = st.sidebar.number_input("Oldpeak")
    slope = st.sidebar.selectbox("ST Slope",['Down', 'Flat', 'Up'])
    
    numerical = [age,bp,cholesterol,fastingbs,hr,oldpeak]
    
    gender = [0,0]
    if sex == "F":
        gender[0] = 1
    elif sex == "M":
        gender[1] = 1
        
    pain = [0,0,0,0]
    if chest == "ASA":
        pain = [1,0,0,0]
    elif chest == "ATA":
        pain = [0,1,0,0]
    elif chest == "NAP":
        pain = [0,0,1,0]
    elif chest == "TA":
        pain = [0,0,0,1]
        
    resting = [0,0,0]
    if ecg == "LVH":
        resting = [1,0,0]
    elif ecg == "Normal":
        resting = [0,1,0]
    elif ecg == "ST":
        resting = [0,0,1]
    
    angina = [0,0]
    if exercise == True:
        angina = [0,1]
    else:
        angina = [1,0]
        
    stlope = [0,0,0]
    if slope == "Down":
        stlope = [1,0,0]
    elif slope == "Flat":
        stlope = [0,1,0]
    elif slope == "Up":
        stlope = [0,0,1]
        
    values = numerical + gender + pain + resting + angina + stlope
    values = np.array(values)
    values = values.reshape(1,-1)
if st.button("Predict"):
    with st.spinner("Predicting..."):
        time.sleep(3)
    pred = int(loaded_model.predict(values))
    if pred == 1:
        st.error("I'm sorry but you will need a check up")
    elif pred == 0:
        st.success("Congratulations you're healthy")
        st.balloons()
    
    
    