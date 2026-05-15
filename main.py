import streamlit as st
from supabase import create_client, Client

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Senti News | News That Finds You First",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the sidebar for the landing page
)

# --- SUPABASE INITIALIZATION ---
# We use @st.cache_resource so Streamlit doesn't open a new connection on every click
@st.cache_resource
def init_connection():
    # It's best practice to hide your keys in Streamlit's secrets manager!
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

try:
    supabase: Client = init_connection()
    # If you want to test the connection, you can uncomment the line below:
    # st.toast("Successfully connected to Supabase!") 
except Exception as e:
    st.error(f"Failed to connect to Supabase. Check your secrets.toml file. Error: {e}")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 0rem;}

    .brand-title { color: #001d4f; text-align: center; font-size: 4.5rem; font-weight: 800; margin-bottom: 0px; }
    .tagline { color: #bc9e5a; text-align: center; font-size: 1.5rem; font-style: italic; margin-top: -10px; margin-bottom: 30px; }
    .description { text-align: center; color: #4a4a4a; font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.6; margin-bottom: 40px; }
    
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; padding: 0.5rem 1rem; border: 2px solid #001d4f; transition: all 0.3s ease; }
    
    .footer { margin-top: 100px; padding-top: 40px; border-top: 1px solid #e0e0e0; color: #4a4a4a; }
    .footer h4 { color: #001d4f; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVBAR ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1, 6, 1, 1])
with nav_col1:
    st.markdown("<h3 style='color: #001d4f; margin-top: 0;'>Senti News</h3>", unsafe_allow_html=True)
with nav_col3:
    if st.button("Login", key="nav_login"):
        st.switch_page("pages/login.py")
with nav_col4:
    if st.button("Register", type="primary", key="nav_reg"):
        st.switch_page("pages/register.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- HERO SECTION ---
logo_col1, logo_col2, logo_col3 = st.columns([3, 1, 3])
with logo_col2:
    st.image("assets/logo_icon.png", use_container_width=True)


st.markdown("<h1 class='brand-title'>Senti News</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>“News That Finds You First.”</p>", unsafe_allow_html=True)

st.markdown("""
<div class='description'>
    The Senti News is a modern web application that brings together real-time news from multiple trusted sources into one easy-to-use platform. Designed for convenience and efficiency, it allows users to explore the latest headlines, filter articles by category, and stay updated on important local and global events. Simple, organized, and intelligent.
</div>
""", unsafe_allow_html=True)

btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([2, 1, 1, 2])
with btn_col2:
    if st.button("Get Started", type="primary", use_container_width=True):
        st.switch_page("pages/register.py")
with btn_col3:
    if st.button("Sign In", use_container_width=True):
        st.switch_page("pages/login.py")

# --- FOOTER ---
st.markdown("<div class='footer'></div>", unsafe_allow_html=True)
foot_col1, foot_col2, foot_col3 = st.columns(3)

with foot_col1:
    st.markdown("<h4>About Senti News</h4>", unsafe_allow_html=True)
    st.markdown("Your trusted source for news from around the world, curated to keep you informed and engaged.")
with foot_col2:
    st.markdown("<h4>Contact Us</h4>", unsafe_allow_html=True)
    st.markdown("✉️ contact@sentinews.com<br>📞 +6 (938) 123-4567<br>📍 38 Pasig City, 1602", unsafe_allow_html=True)
with foot_col3:
    st.markdown("<h4>Quick Links</h4>", unsafe_allow_html=True)
    st.markdown("Privacy Policy<br>Terms of Service<br>FAQ", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #888;'>© 2026 Senti News. All rights reserved.</p>", unsafe_allow_html=True)