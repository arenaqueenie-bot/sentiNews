import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Account | Senti News", page_icon="👤", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .profile-header { color: #001d4f; margin-bottom: 0px; }
    .profile-sub { color: #bc9e5a; font-style: italic; margin-top: -10px; margin-bottom: 20px; }
    
    div.stButton > button:first-child {
        background-color: #001d4f; 
        color: white; 
        border-radius: 8px; 
        font-weight: bold; 
        width: 100%;
    }
    div.stButton > button:first-child:hover { background-color: #bc9e5a; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color: #001d4f; text-align: center;'>Senti News</h2>", unsafe_allow_html=True)
    st.divider()
    
    if st.button("⬅️ Back to News Feed", use_container_width=True):
        st.switch_page("pages/home.py")
        
    st.write("")
    if st.button("Log Out", type="primary", use_container_width=True):
        st.switch_page("main.py")

# --- MAIN CONTENT ---
st.markdown("<h1 class='profile-header'>Account Settings</h1>", unsafe_allow_html=True)
st.markdown("<p class='profile-sub'>Manage your Senti News profile and preferences.</p>", unsafe_allow_html=True)

# Mock User Data (We'll replace this when we connect a database)
user_data = {
    "name": "Queenie",
    "email": "queenie@sentinews.com",
    "username": "queenie_dev"
}

# --- TABS FOR ORGANIZATION ---
tab1, tab2 = st.tabs(["Profile Details", "Preferences"])

with tab1:
    st.subheader("Personal Information")
    with st.form("profile_form", clear_on_submit=False):
        st.text_input("Full Name", value=user_data["name"])
        st.text_input("Email Address", value=user_data["email"])
        # We disable the username field because usernames usually can't be changed!
        st.text_input("Username", value=user_data["username"], disabled=True)
        
        st.write("")
        if st.form_submit_button("Update Profile"):
            st.success("Profile updated successfully!")
            
    st.divider()
    st.subheader("Change Password")
    with st.form("password_form", clear_on_submit=True):
        st.text_input("Current Password", type="password")
        st.text_input("New Password", type="password")
        st.text_input("Confirm New Password", type="password")
        
        if st.form_submit_button("Update Password"):
            st.success("Password updated securely!")

with tab2:
    st.subheader("News Preferences")
    st.write("Customize what you see on your dashboard.")
    
    st.selectbox("Default News Category", ["Top Headlines", "Technology", "Business", "Politics", "Entertainment"])
    st.toggle("Enable Email Notifications for Breaking News", value=True)
    st.toggle("Show Sentiment Badges on Articles", value=True)
    
    st.write("")
    # Standard button for the preferences tab outside of a form
    if st.button("Save Preferences"):
        st.success("Preferences saved!")