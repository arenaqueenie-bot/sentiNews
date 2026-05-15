import streamlit as st
from shared import init_supabase

st.set_page_config(page_title="Register | Senti News", page_icon="📰", layout="centered")

# Initialize database
supabase = init_supabase()

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;}
    div.stButton > button:first-child {background-color: #001d4f; color: white; border: None; width: 100%; border-radius: 8px; padding: 0.5rem; font-weight: bold;}
    div.stButton > button:first-child:hover {background-color: #bc9e5a;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #001d4f; margin-bottom: 0;'>Join Senti News</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bc9e5a; font-style: italic; margin-top: -10px;'>Create an account to get your personalized news feed.</p><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.form("register_form", clear_on_submit=False):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        st.write("")
        submit_button = st.form_submit_button("Register")

        if submit_button:
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif not all([full_name, email, username, password]):
                st.warning("Please fill out all fields.")
            else:
                try:
                    # --- SEND TO SUPABASE ---
                    response = supabase.auth.sign_up({
                        "email": email,
                        "password": password,
                        "options": {
                            "data": {
                                "full_name": full_name,
                                "username": username
                            }
                        }
                    })
                    st.success("Account created successfully! You can now log in.")
                except Exception as e:
                    # Catch errors like "Email already exists" or "Password too weak"
                    st.error(f"Registration failed: {e}")

    st.markdown("<br><p style='text-align: center; margin-bottom: 0;'>Already have an account?</p>", unsafe_allow_html=True)
    if st.button("Log In"):
        st.switch_page("pages/login.py")