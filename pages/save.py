import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Reading List | Senti News", page_icon="🔖", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Card Styling */
    .news-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ffffff;
        transition: box-shadow 0.3s ease;
        border-left: 5px solid #bc9e5a; /* Gray Orange Accent for saved items */
    }
    .news-card:hover {
        box-shadow: 0 4px 12px rgba(188, 158, 90, 0.2);
    }
    
    /* Typography */
    .article-title { color: #001d4f; margin-top: 0; margin-bottom: 5px; }
    .source-text { color: gray; font-size: 0.9rem; margin-bottom: 15px; }
    .summary-text { color: #333333; font-size: 1.05rem; }
    .read-more { color: #bc9e5a; text-decoration: none; font-weight: bold; }
    
    /* Sentiment Tags */
    .sent-badge {
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        color: white;
    }
    .sent-positive { background-color: #2e7d32; } 
    .sent-neutral { background-color: #bc9e5a; }  
    .sent-negative { background-color: #c62828; } 
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
st.markdown("<h1 style='color: #001d4f;'>My Reading List 🔖</h1>", unsafe_allow_html=True)
st.write("Catch up on the articles you've saved for later.")
st.divider()

# --- MOCK SAVED DATA ---
# In the future, this will be fetched from a database based on the logged-in user
mock_saved_articles = [
    {
        "title": "New Climate Policy Debated in Assembly", 
        "source": "Daily Planet", 
        "sentiment": "Neutral", 
        "summary": "Lawmakers spent the weekend debating the specifics of the new carbon emission reduction targets. Both sides presented extensive economic forecasts.",
        "date_saved": "2026-05-15"
    }
]

if not mock_saved_articles:
    st.info("Your reading list is currently empty. Go to the news feed to save some articles!")
else:
    # --- RENDER SAVED ARTICLES ---
    for article in mock_saved_articles:
        if article['sentiment'] == "Positive":
            badge_class = "sent-positive"
            icon = "📈"
        elif article['sentiment'] == "Negative":
            badge_class = "sent-negative"
            icon = "📉"
        else:
            badge_class = "sent-neutral"
            icon = "⚖️"

        card_html = f"""
        <div class="news-card">
            <h3 class="article-title">{article['title']}</h3>
            <div class="source-text">
                {article['source']} • 
                <span class="sent-badge {badge_class}">{icon} {article['sentiment']}</span>
                <span style="float: right; color: #888;">Saved on: {article['date_saved']}</span>
            </div>
            <p class="summary-text">{article['summary']}</p>
            <a href="#" class="read-more">Read Full Article →</a>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Remove button
        col1, col2 = st.columns([8, 1])
        with col2:
            st.button("🗑️ Remove", key=f"remove_{article['title']}")