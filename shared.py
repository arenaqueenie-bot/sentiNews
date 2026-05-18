import requests
import streamlit as st
from textblob import TextBlob
from supabase import create_client, Client

# --- SUPABASE CONNECTION ---
@st.cache_resource
def init_supabase() -> Client:
    """Initializes and caches the Supabase connection."""
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

# ... [Keep your existing fetch_top_news and analyze_sentiment functions below] ...
