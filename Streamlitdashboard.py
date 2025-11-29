import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  

st.title("stream app for you ")
st.text("Welcome to our dashboard")
st.header("I am a header")
st.write("You can write ", 10+5)

name = st.text_input("Enter the name ")
age = st.number_input("Enter the age ")
st.write("Your name is: ", name , "Your age is :", age)
st.selectbox("Enter your course :",["BCA","BTECH","MCA"])
if st.button("Click me :"):
    st.success("Clicked button ")
file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File Upload Sucessfully")

data = {"Name":["TOM","JACK","POP","HARRY"], "Marks":[10,20,20,10]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({"Marks":[10,20,20,10]})

st.line_chart(data)
st.bar_chart(data)

subject = ["Python","c++","java"]  
marks = [20,10,5]

fig, ax = plt.subplots()
ax.pie(marks, labels=subject, autopct='%1.1f%%')
st.pyplot(fig)  
