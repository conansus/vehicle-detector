#changes
#tambah sqlite database kat login and signup, buang sidebar button, add signup page, add login page, 
#page and button navigation dah ada dan betul
#login(no null or space) 
#signup dah ada format for username and password and structure for both user credentials

#weakness
#duplicate user details
#no detection history
#no hashing

#nnti nak buang video 
#disable sidebar alif
from streamlit_extras.switch_page_button import switch_page

# External packages
import streamlit as st

#ni utk import sqlite3
import sqlite3

#TO GET RID OF SIDEBAR
st.set_page_config(page_title  = "Object Detection using YOLO and Faster RCNN",page_icon="🤖", initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
hide_sidebar_button_style = """
        <style>
        #sidebar-fblp2m {
            display: none;
        }
        </style>
        """
st.markdown(hide_sidebar_button_style, unsafe_allow_html=True)




#initialise and connect database
con = sqlite3.connect("database.db", check_same_thread=False) #ni kena connect 
c = con.cursor() #ni utk execute command

#set active user to true or false

#ni functions dlm database
def create_usertable():
    c.execute("CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT, password2 TEXT)")
        
def add_userdata(username, password, password2):
    c.execute("INSERT INTO userstable(username,password, password2) VALUES(?,?,?)", (username, password, password2))
    con.commit()

def login_user(username, password):
    c.execute("SELECT * FROM userstable WHERE username = ? AND password = ?", (username, password))
    data = c.fetchall()
    return data

def view_all_users():
     c.execute("SELECT * FROM userstable")
     data = c.fetchall()
     return data

def nullornot(s):
    if s is None or s.strip()=="":
        return True
    else:
        return False

#user login
username = st.text_input("username:")
password = st.text_input("password:", type="password")


col1,col2 = st.columns([15,2])
with col2:
    login = st.button("login")
with col1:
    signup = st.button("signup")

if login:
    if nullornot(username)==False and nullornot(password)==False:
        #ni nk verify with database
        create_usertable()
        result = login_user(username, password)
        if result:
            st.success(f"logged in as {username}")
            switch_page("detection")
        else:
            st.warning("please try again")

    else:
        st.warning("do not leave blank space")

if signup:
    switch_page("signup")

import pandas as pd
#user_result = view_all_users()
#db = pd.DataFrame(user_result,columns = ["username","password","password2"])
#st.dataframe(db)

