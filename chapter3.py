import streamlit as st

st.title("Chai Taste Poll")

col1,col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://media.istockphoto.com/id/1297483389/photo/masala-tea-chai.jpg?s=2048x2048&w=is&k=20&c=PDKzb92QYAOUa6RWZOxT13e-vZ-cZWbIwETq9CeRSm8=",width=100)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/31141291/pexels-photo-31141291.jpeg",width=100)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")    

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai",["Masala","Kesar","Adrak"]) 

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
""")


st.markdown('### Welcome to Chai App')
st.markdown('> Blockquote')