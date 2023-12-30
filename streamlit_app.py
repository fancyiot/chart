import streamlit as st
st.set_page_config(page_title='First app', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
st.title("Welcome, Streamlit App!")
st.sidebar.text("# Menu options...")
with st.container():
    st.markdown("<div class='motivational-container'>", unsafe_allow_html=True)
    st.success(''' Unlock the code to your dreams; every line, every challenge, and every bug is a step closer to the masterpiece you're creating. 
    
    Embrace the syntax of resilience, debug your doubts, and program your success with passion and persistence. In the realm of code, you're not just creating software; you're crafting the future. 
    
    Keep coding, keep conquering!''', icon="👩‍💻")
st.snow()
