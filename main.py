import streamlit as st

name=st.text_input("Enter your name:")
fname=st.text_input("Enter your Father name:")
adress=st.text_input("Enter your text:")
classdata=st.selectbox("Enter your class",(1,2,3,4,5))

button=st.button("Done")
if button:
    st.markdown(f"""
    Name:{name}
    Father name:{fname}
    Adress:{adress}
    Class={classdata}""")