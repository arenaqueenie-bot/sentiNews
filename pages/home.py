import streamlit as st
from shared import fetch_top_news, analyze_sentiment

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Senti News", page_icon="📰", layout="wide")

# --- CLAUDE-INSPIRED CSS ---
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp { background-color: #ffffff; }
    
    /* Clean Card Design */
    .news-card {
        border: 1px solid #efefef;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 16px;
        background-color: #ffffff;
        transition: all 0.2s ease-in-out;
    }
    .news-card:hover {
        border-color: #bc9e5a;
        background-color: #fcfaf5; /* Very subtle orange tint on hover */
    }
    
    /* Typography */
    .article-title { 
        color: #001d4f; 
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 1.25rem; 
        font-weight: 600;
        margin-bottom: 8px;
    }
    .source-tag {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #666;
        margin-bottom: 12px;
    }
    .summary-text {
        color: #444;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 16px;
    }
    
    /* Sentiment Badges - Minimalist version */
    .sent-badge {
        display: inline-flex;
        align-items: center;
        padding: 2px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-left: 8px;
    }
    .pos { background-color: #e8f5e9; color: #2e7d32; border: 1px solid #c8e6c9; }
    .neu { background-color: #fff9eb; color: #bc9e5a; border: 1px solid #ffeeba; }
    .neg { background-color: #ffebee; color: #c62828; border: 1px solid #ffcdd2; }

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        border: 1px solid #001d4f;
        color: #001d4f;
        background-color: