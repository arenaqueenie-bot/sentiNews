import streamlit as st

st.set_page_config(page_title="Saved Articles", page_icon="💾", layout="wide")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.saved-container {
    background-color: #17356d;
    padding: 40px;
    border-radius: 25px;
    max-width: 900px;
    margin: auto;
    text-align: center;
    color: white;
}
.saved-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 10px;
}
.saved-subtitle {
    font-size: 16px;
    color: #cfcfcf;
    margin-bottom: 30px;
}
.empty-box {
    background-color: #304b7d;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
}
.empty-text {
    font-size: 18px;
    color: #d9d9d9;
    margin-bottom: 10px;
}
.browse-btn {
    background-color: #d4af37;
    padding: 10px 20px;
    border-radius: 12px;
    color: black;
    font-weight: 600;
    text-decoration: none;
}
.browse-btn:hover {
    background-color: #b9972f;
}
.back-link {
    color: #d4af37;
    text-decoration: none;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 20px;
}
.back-link:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SAVED PAGE CONTENT
# =========================
st.markdown('<div class="saved-container">', unsafe_allow_html=True)

# Back to Home link
st.markdown('<a href="/" class="back-link">⬅ Back to Home</a>', unsafe_allow_html=True)

# Title + subtitle
st.markdown('<div class="saved-title">Saved Articles</div>', unsafe_allow_html=True)
st.markdown('<div class="saved-subtitle">0 articles saved</div>', unsafe_allow_html=True)

# Empty state box
st.markdown("""
<div class="empty-box">
    <div class="empty-text">No saved articles yet</div>
    <div class="empty-text">Start saving articles by clicking the 💾 Save button on any article.</div>
    <a href="/" class="browse-btn">Browse Articles</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
