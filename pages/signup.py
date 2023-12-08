import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from login import create_usertable,add_userdata
import sqlite3

#TO GET RID OF SIDEBAR
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
hide_sidebar_button_style = """
        <style>
        #sidebar-fblp2m {
            display: none;
        }
        </style>
        """
st.markdown(hide_sidebar_button_style, unsafe_allow_html=True)


def correct_null(s):
    if s is None or s.strip()=="":
        return True
    else:
        return False

def correct_username(name):
    if len(name)<3:
        return False
    if not name[0].isalpha():
        return False
    for c in name:
        if not c.isalpha():
            return False
    return True

def correct_password(passw):
    if len(passw) < 6:
        return False

    # Check that the username starts with a letter
    if not passw[0].isalpha():
        return False

    # Check that the username contains at least one number and one special character
    if not any(char.isdigit() for char in passw) or not any(char.isalpha() for char in passw) or not any(not char.isalnum() for char in passw):
        return False

    # If all checks pass, the username is valid
    return True




#page ni utk signup
usernameee = st.text_input("username::")
passworddd = st.text_input("password::", type="password")
password2 = st.text_input("password2:", type="password")

col1,col2 = st.columns([15,2])
with col1:
    back = st.button("back")
with col2:
    sign_up = st.button("sign up")

if back:
    switch_page("login")
if sign_up:
    if passworddd==password2:

        if correct_null(usernameee)==False and correct_null(passworddd)==False and correct_username(usernameee)==True and correct_password(passworddd):

            con =sqlite3.connect("database.db", check_same_thread=False)
            c = con.cursor()
            create_usertable()
            add_userdata(usernameee, passworddd, password2)
            switch_page("detection")
        else:
            st.warning("try again")
    else:
        st.warning("make sure the passwords are the same")