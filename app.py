import streamlit as st
from multiapp import MultiApp
from apps import home, signup, login 

app = MultiApp()

app.add_app("Sign Up", signup.app)
app.add_app("Login", login.app)
app.add_app("Home", home.app)

app.run()