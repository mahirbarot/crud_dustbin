import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate(r"serviceAccount.json")

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartdustbin-nuv-default-rtdb.firebaseio.com/'
})

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
    ('Add Dustbin', 'Remove Dustbin', 'View Details','View Complaints'))

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
    
elif option=='View Complaints':
    st.header("Server data:-")
    data=ref.child('complaints').child('complaints').get()
    st.header("Areas")
    area=[]
    for k,v in data.items():
        area.append(k)
        # for k2,v2 in v.items():
        #     print(k2)
        
    area=st.selectbox('Select Area to get details:',area)
    complaints=data=ref.child('complaints').child('complaints').child(area).get()
    # st.write(complaints)# 
    cnt=1
    if type(complaints)==list:
        for i in complaints:
            if type(i)==dict:
                st.header(f"complaint no {cnt}:")
                cnt=cnt+1
                for k2,v2 in i.items():
                    st.write(k2,":",v2)
    else:
        try:
            for i,(c,v) in enumerate(complaints.items()):
                st.header(f'complaint no {i+1}:')
                for i,(c1,v1) in enumerate(v.items()): # for i, (k, v) in enumerate(mydict.items()):
                    # st.write(v1)
                    # s=str(i)+" complaint"
                    # st.header(f"complaint no {cnt}:- ")
                    st.write(c1,':',v1)
        except TypeError:
            st.warning("TypeError: Dictionary settings of your data.")
                    
            
    
    
    
    # for c,v in complaints.items():
    #     # st.write(v)
    #     for i,(c1,v1) in enumerate(v.items()): # for i, (k, v) in enumerate(mydict.items()):
    #         # st.write(v1)
    #         # s=str(i)+" complaint"
    #         st.header(f"complaint no {cnt}:- ")
    #         cnt=int(cnt)+1
            
            
    #         for i,(c2,v2) in enumerate(v1.items()):
    #         # for c2,v2 in v1.items():
    #             st.write(c2,'=',v2)
    #     # for k,v in c.items():
    #     #     st.write(k)
    # # st.write(data)



