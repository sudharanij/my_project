import streamlit as st

st.title("My First Project :blush:")


btn_click = st.button("Click here!")

if btn_click == True:
    st.text("Let's connect on Linkedin")
    st.subheader("https://www.linkedin.com/in/sudharani-jukanti-698a0523a")
    st.text("Thank you for connecting...")
    st.balloons()