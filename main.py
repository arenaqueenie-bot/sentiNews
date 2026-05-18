import os
import streamlit as st
from supabase import create_client, Client

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Senti News | News That Finds You First",
    page_icon="assets/logo_icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- SUPABASE ----------
@st.cache_resource
def init_connection():
    try:
        return create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_KEY"]
        )
    except:
        return None

supabase: Client | None = init_connection()

# ---------- CSS ----------
st.markdown("""
<style>
#MainMenu,footer{visibility:hidden;}

.stApp{
    background:#001d4f;
    color:white;
    font-family:Inter,sans-serif;
}

.block-container{
    max-width:1400px;
    padding-top:1.5rem;
}

.stButton>button{
    width:100%;
    padding:14px;
    border-radius:14px;
    border:2px solid #bc9e5a;
    background:transparent;
    color:white;
    font-weight:700;
    transition:.3s;
}

.stButton>button:hover{
    background:#bc9e5a;
    color:#001d4f;
}

[data-testid="stVerticalBlock"]:has(.hero-marker),
[data-testid="stVerticalBlock"]:has(.side-marker),
[data-testid="stVerticalBlock"]:has(.feature-marker){
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.15);
    backdrop-filter:blur(16px);
    box-shadow:0 12px 35px rgba(0,0,0,.35);
}

[data-testid="stVerticalBlock"]:has(.hero-marker),
[data-testid="stVerticalBlock"]:has(.side-marker){
    border-radius:28px;
    padding:40px;
}

[data-testid="stVerticalBlock"]:has(.feature-marker){
    border-radius:24px;
    padding:28px;
    transition:.3s;
}

[data-testid="stVerticalBlock"]:has(.feature-marker):hover{
    transform:translateY(-4px);
    border-color:#bc9e5a;
}

.brand{font-size:36px;font-weight:900;}
.brand span,
.hero-title span,
.hero-label{color:#bc9e5a;}

.hero-label{
    font-size:14px;
    font-weight:700;
    letter-spacing:2px;
}

.hero-title{
    font-size:72px;
    font-weight:900;
    line-height:1;
}

.hero-text{
    color:rgba(255,255,255,.82);
    font-size:18px;
    line-height:1.8;
}

.section-title{
    font-size:34px;
    font-weight:800;
}

.footer{
    text-align:center;
    color:rgba(255,255,255,.6);
    margin-top:50px;
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVBAR ----------
nav1, _, nav3, nav4 = st.columns([5, 4, 1.2, 1.2])

with nav1:
    st.markdown(
        "<div class='brand'>Senti <span>News</span></div>",
        unsafe_allow_html=True
    )

with nav3:
    if st.button("Sign In"):
        st.switch_page("pages/login.py")

with nav4:
    if st.button("Register"):
        st.switch_page("pages/register.py")

st.write("")

# ---------- HERO ----------
left, right = st.columns([1.5, 1])

with left:

    st.markdown("<div class='hero-marker'></div>", unsafe_allow_html=True)

    with st.container():

        st.markdown("""
        <div class='hero-label'>
            INTELLIGENT NEWS DELIVERED IN REAL TIME
        </div>

        <div class='hero-title'>
            Senti <span>News</span>
        </div>

        <div class='hero-text'>
            Stay updated with real-time news powered by intelligent
            sentiment analysis and personalized recommendations.
            Fast. Clean. Focused. Built for the modern reader.
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        b1, b2 = st.columns(2)

        with b1:
            if st.button("Get Started"):
                st.switch_page("pages/register.py")



with right:

    st.markdown("<div class='side-marker'></div>", unsafe_allow_html=True)

    with st.container():

        _, logo, _ = st.columns(3)

        with logo:
            if os.path.exists("assets/logo_icon.png"):
                st.image("assets/logo_icon.png", width=180)

        st.markdown("""
        <p style='color:#bc9e5a;font-size:13px;
        font-weight:700;letter-spacing:2px'>
            WHY SENTI NEWS?
        </p>
        """, unsafe_allow_html=True)

        st.subheader("Real-Time News That Finds You First")

        st.write("""
        Senti News delivers real-time news from trusted global
        and local sources in one intelligent, personalized feed
        powered by AI sentiment analysis.
        """)

st.write("")
st.write("")

# ---------- FEATURES ----------
st.markdown("""
<div class='section-title'>
    Why Readers Choose Senti News
</div>
""", unsafe_allow_html=True)

features = [
    ("Real-Time Updates",
     "Live news as events unfold worldwide, delivered instantly."),

    ("Smart Personalization",
     "AI-powered feed tailored to your interests."),

    ("Global & Local",
     "Coverage from international headlines to local stories.")
]

for col, (title, desc) in zip(st.columns(3), features):

    with col:

        st.markdown(
            "<div class='feature-marker'></div>",
            unsafe_allow_html=True
        )

        with st.container():
            st.subheader(title)
            st.write(desc)

# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
    © 2026 Senti News • News That Finds You First
</div>
""", unsafe_allow_html=True)