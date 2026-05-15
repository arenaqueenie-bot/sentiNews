import streamlit as st
import time
from shared import init_supabase

st.set_page_config(page_title="Login | Senti News", page_icon="📰", layout="centered")

supabase = init_supabase()

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;}
    div.stButton > button:first-child {background-color: #001d4f; color: white; border: None; width: 100%; border-radius: 8px; padding: 0.5rem; font-weight: bold;}
    div.stButton > button:first-child:hover {background-color: #bc9e5a;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #001d4f; margin-bottom: 0;'>Welcome Back</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bc9e5a; font-style: italic; margin-top: -10px;'>Log in to your Senti News account</p><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        
        st.write("") 
        submit_button = st.form_submit_button("Sign In")

        if submit_button:
            if email and password:
                try:
                    # --- AUTHENTICATE WITH SUPABASE ---
                    response = supabase.auth.sign_in_with_password({
                        "email": email,
                        "password": password
                    })
                    
                    # Store the user's session data locally so the dashboard knows who is logged in
                    st.session_state["user"] = response.user
                    
                    st.success("Successfully logged in! Redirecting to dashboard...")
                    time.sleep(1) # Quick pause so they see the success message
                    st.switch_page("pages/home.py")
                    
                except Exception as e:
                    st.error("Login failed. Please check your email and password.")
            else:
                st.warning("Please enter both email and password.")

    st.markdown("<br><p style='text-align: center; margin-bottom: 0;'>Don't have an account?</p>", unsafe_allow_html=True)
    if st.button("Create an Account"):
        st.switch_page("pages/register.py")