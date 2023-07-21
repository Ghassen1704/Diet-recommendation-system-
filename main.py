import streamlit as st 
from Weight_Gain import Weight_Gain
from Weight_Loss import Weight_Loss
from Healthy import Healthy
st.title("WELCOME TO DIET PREDICTION SYSTEM")
st.write("""### We need some information !""") 
age = st.slider("Enter your age", 5,90,30)
weight = st.slider("Enter your weight",30,200,80)
height = st.slider("Enter your height",1.0,2.8,1.7)
bmi = weight/(pow(height,2))
ok=st.selectbox("Type",("Weight Loss","Weight Gain","Healthy") )
if ok=="Weight Loss":
    Weight_Loss(age,weight,height,bmi)

elif ok=="Weight Gain":
    Weight_Gain(age,weight,height,bmi)
else:
    Healthy(age,weight,height,bmi)