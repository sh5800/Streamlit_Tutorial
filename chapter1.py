import streamlit as st
st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

fav_chai =  st.selectbox("Your Favorite chai: ",["Masala Chai","Adrak Chai","Lemon Tea","Kesar Chai"])

st.write(f"Your choice {fav_chai}. Excellent Choice")

st.success("Your chai has been brewed")