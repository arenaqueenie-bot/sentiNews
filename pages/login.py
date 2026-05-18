import streamlit as st
import time
from shared import init_supabase

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Login | Senti News",
    page_icon="assets/logo_icon.png",
    layout="wide"
)

supabase = init_supabase()
st.session_state.setdefault("user", None)

# ---------- CSS ----------
st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden;}

.stApp{
    background:#001d4f;
    color:white;
    font-family:Inter,sans-serif;
}

.brand-title{font-size:60px;font-weight:900;line-height:1;}
.brand-sub,.sub{color:#bc9e5a;}

[data-testid="stVerticalBlock"]:has(.login-card){
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.15);
    backdrop-filter:blur(14px);
    border-radius:28px;
    padding:45px;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
}

.title{
    text-align:center;
    font-size:38px;
    font-weight:800;
}

.stTextInput input{
    background:white;
    color:#001d4f;
    border:none;
    border-radius:14px;
    padding:15px;
    font-weight:600;
}

.stTextInput input:focus{
    border:2px solid #bc9e5a !important;
    box-shadow:0 0 0 4px rgba(188,158,90,.25);
}

.stButton>button,
.stFormSubmitButton>button{
    width:200px;
    padding:14px;
    border-radius:14px;
    border:2px solid #bc9e5a;
    background:transparent;
    color:white;
    font-weight:700;
    transition:.3s;
}

.stButton>button:hover,
.stFormSubmitButton>button:hover{
    background:#bc9e5a;
    color:#001d4f;
}

.footer{
    text-align:center;
    margin-top:20px;
    color:rgba(255,255,255,.6);
}
</style>
""", unsafe_allow_html=True)

# ---------- LAYOUT ----------
left, center, right = st.columns([1.2, 1.5, 1])

# ---------- LEFT ----------
with left:
    st.image("assets/logo_icon.png", width=300)
    st.markdown("""
    <div style='padding-top:20px'>
        <div class='brand-title'>Senti News</div>
        <div class='brand-sub'>
            AI-powered sentiment analysis for modern news readers
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- LOGIN ----------
with center:
    st.markdown("<div class='login-card'></div>", unsafe_allow_html=True)

    with st.container():
        _, logo, _ = st.columns(3)
        with logo:
            st.image("assets/profile.png")

        st.markdown("""
        <div class='title'>Welcome Back</div>
        <div class='sub' style='text-align:center;margin-bottom:25px'>
            Log in to your account
        </div>
        """, unsafe_allow_html=True)

        with st.form("login"):
            email = st.text_input("Email Address", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")

         
            st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

            if st.form_submit_button("Sign In"):
                if not all([email, password]):
                    st.warning("Please fill in all fields.")
                else:
                    try:
                        with st.spinner("Signing in..."):
                            res = supabase.auth.sign_in_with_password({
                                "email": email,
                                "password": password
                            })
                        st.session_state["user"] = {
                            "id": res.user.id,
                            "email": res.user.email
                        }
                        st.success("Login successful!")
                        time.sleep(1)
                        st.switch_page("pages/home.py")
                    except:
                        st.error("Invalid email or password.")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align:center;margin-top:18px'>
            Don’t have an account?
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
                    
    col1, col2, col3 = st.columns([1,2,1])
with col2:
        if st.button("Create Account Now"):
            st.switch_page("pages/register.py")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            "<div class='footer'>© 2026 Senti News</div>",
            unsafe_allow_html=True
        )

# ---------- RIGHT ----------
with right:
    st.empty()
