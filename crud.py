import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate(r"C:\Users\mahir\Desktop\ai_end\mini_project\serviceAccount.json")

# Initialize the Firebase app
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://smartdustbin-nuv-default-rtdb.firebaseio.com/'
# })

st.set_page_config(
        page_title="mini project",
        page_icon="house_buildings",
        layout='centered',
    )

ref = db.reference('/')
ref2 =db.reference('/')

st.title("Dustbin management portal.")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('4.png',width=120)

with col3:
    st.write(' ')
    


option = st.selectbox(
    'What task you want to perfrom?',
    ('Add Dustbin', 'Remove Dustbin', 'View Details'))

if option=='Add Dustbin':
    st.header("fill the details to add:")
    area = st.text_input('Area')
    area=area.lower()
    area=area.capitalize()
    dustbin_id = st.text_input('Dustbin ID')
    capacity = st.text_input('Capacity')
    
    data={'area':area,'dustbin_id':dustbin_id,'capacity':capacity,'cords':'(413.567,453.677)','authority':'VMC','status':0}
    if st.button('Submit'):
        ref.child('information').child(area).child(dustbin_id).set(data)
        st.success('Data added successfully!')
    
elif option=='Remove Dustbin':
    st.header("fill the details to remove:")
    area = st.text_input('Area')
    area=area.lower()
    area=area.capitalize()
    dustbin_id = st.text_input('Dustbin ID')
    
    if st.button('Submit'):
        ref.child('information').child(area).child(dustbin_id).delete()
        st.success('Data removed successfully!')
        
elif option=='View Details':
    st.header("Server data:-")
    data=ref.child('information').get()
    st.write(data)
    



