import streamlit as st

st.set_page_config(
    page_title="Senti News",
    page_icon="logo_icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# SAMPLE NEWS DATA
# =========================
news_data = [
    {
        "title": "Typhoon Signals Raised Across Luzon",
        "description": "PAGASA warns residents as heavy rainfall and strong winds continue to affect northern areas.",
        "category": "Weather",
        "sentiment": "Urgent/Advisory",
        "author": "Maria Santos",
        "date": "May 18, 2026"
    },
    {
        "title": "Philippine Economy Shows Growth",
        "description": "Business experts report stronger investments and increasing consumer confidence this quarter.",
        "category": "Business",
        "sentiment": "Cautionary/Critical",
        "author": "Carlos Reyes",
        "date": "May 18, 2026"
    },
    {
        "title": "National Team Wins Championship",
        "description": "Fans celebrate after a thrilling finals match that secured the country’s victory.",
        "category": "Sports",
        "sentiment": "Informative/Factual",
        "author": "Ana Cruz",
        "date": "May 17, 2026"
    },
    {
        "title": "International Leaders Meet for Summit",
        "description": "World leaders discuss global economic recovery and climate initiatives.",
        "category": "World",
        "sentiment": "Informative/Factual",
        "author": "James Lee",
        "date": "May 16, 2026"
    },
    {
        "title": "Popular Celebrity Announces New Film",
        "description": "The upcoming movie is expected to release later this year.",
        "category": "Showbiz",
        "sentiment": "Encouraging/Advantageous",
        "author": "Liza Gomez",
        "date": "May 15, 2026"
    },
    {
        "title": "Government Launches New Education Program",
        "description": "The initiative aims to improve digital literacy among students nationwide.",
        "category": "Nation",
        "sentiment": "Informative/Factual",
        "author": "Ramon Dela Cruz",
        "date": "May 14, 2026"
    }
]

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
html, body, [class*="css"] {font-family: 'Arial', sans-serif;}
.stApp {background-color: #001f5b;}

.main-container {
    background-color: #17356d;
    padding: 30px;
    border-radius: 25px;
    max-width: 1400px;
    margin: auto;
    border: 1px solid rgba(255,255,255,0.1);
}

.logo-text {font-size: 40px; font-weight: 800; color: white;}
.logo-highlight {color: #d4af37;}

.category-tabs {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-bottom: 25px;
}
.category-btn {
    background-color: #304b7d;
    padding: 10px 20px;
    border-radius: 25px; /* pill shape */
    color: white;
    border: 1px solid rgba(255,255,255,0.1);
    font-weight: 600;
    cursor: pointer;
}
.category-btn.active {
    background-color: #40598b; /* highlight active tab */
}

.news-card {
    background-color: #40598b;
    padding: 22px;
    border-radius: 22px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
}
.news-title {color: white; font-size: 24px; font-weight: 700; margin-bottom: 10px;}
.news-desc {color: #d9d9d9; font-size: 15px; margin-bottom: 18px;}

.tag {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 10px;
    margin-right: 8px;
    font-size: 12px;
    font-weight: 700;
}
.category-tag {background-color: #203b6f; color: white;}
.sentiment-positive {background-color: #2e8b57; color: white;}
.sentiment-negative {background-color: #b22222; color: white;}
.sentiment-neutral {background-color: #808080; color: white;}

.date-text {color: #d0d0d0; font-size: 13px;}
.author-text {color: #cfcfcf; font-size: 13px; margin-top: 5px;}

.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 15px;
}
.save-btn {
    background-color: #304b7d;
    padding: 6px 12px;
    border-radius: 10px;
    color: white;
    border: none;
    font-size: 13px;
    cursor: pointer;
}
.save-btn:hover {background-color: #203b6f;}

.profile-box {
    background-color: #304b7d;
    padding: 10px;
    border-radius: 50%;
    text-align: center;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# MAIN CONTAINER
# =========================
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# HEADER
header1, header2 = st.columns([8, 2])
with header1:
    st.markdown('<div class="logo-text">Senti <span class="logo-highlight">News</span></div>', unsafe_allow_html=True)
with header2:
    profile_option = st.selectbox("", ["Profile", "Saved", "Logout"])
    if profile_option == "Profile":
        st.switch_page("account.py")
    elif profile_option == "Saved":
        st.switch_page("save.py")
    elif profile_option == "Logout":
        st.session_state.clear()
        st.switch_page("login.py")

# =========================
# CATEGORY SECTION
# =========================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='color:white; margin-bottom:5px;'>Browse News Categories</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#cfcfcf; margin-bottom:20px;'>Stay updated with the latest headlines</p>", unsafe_allow_html=True)

categories = ["All", "Nation", "World", "Weather", "Business", "Sports", "Showbiz"]
selected_category = st.session_state.get("selected_category", "All")

tab_html = "<div class='category-tabs'>"
for cat in categories:
    active_class = "active" if selected_category == cat else ""
    tab_html += f"<div class='category-btn {active_class}'>{cat}</div>"
tab_html += "</div>"
st.markdown(tab_html, unsafe_allow_html=True)

selected_category = st.session_state.get("selected_category", "All")

# =========================
# NEWS SECTION
# =========================
st.markdown("<br>", unsafe_allow_html=True)
filtered_news = news_data if selected_category == "All" else [n for n in news_data if n["category"] == selected_category]

for idx, news in enumerate(filtered_news):
    if "Encouraging" in news["sentiment"] or "Positive" in news["sentiment"]:
        sentiment_class = "sentiment-positive"
    elif "Cautionary" in news["sentiment"] or "Negative" in news["sentiment"] or "Urgent" in news["sentiment"]:
        sentiment_class = "sentiment-negative"
    else:
        sentiment_class = "sentiment-neutral"

    st.markdown(f"""
    <div class="news-card">
        <div class="news-title">{news['title']}</div>
        <div class="news-desc">{news['description']}</div>
        <div style="margin-bottom:12px;">
            <span class="tag category-tag">{news['category']}</span>
            <span class="tag {sentiment_class}">{news['sentiment']}</span>
        </div>
        <div class="author-text">{news['author']}</div>
        <div class="card-footer">
            <div class="date-text">{news['date']}</div>
            <button class="save-btn"> Save</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("<div style='text-align:center; color:#cfcfcf; margin-top:30px;'>© 2026 Senti News • Real-Time News Powered by AI</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
