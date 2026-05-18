import streamlit as st, time
from shared import init_supabase

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Register | Senti News",
    page_icon="assets/logo_icon.png",
    layout="wide"
)
supabase = init_supabase()
st.session_state.setdefault("user", None)

# ---------- CSS ----------
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden}
.stApp{
    background:#001d4f;
    color:white;
    font-family:Inter,sans-serif;
}
.brand-title{font-size:60px;font-weight:900;line-height:1}
.brand-sub,.sub{color:#bc9e5a}
.title{text-align:center;font-size:38px;font-weight:800}
.footer{text-align:center;margin-top:20px;color:rgba(255,255,255,.6)}

[data-testid="stVerticalBlock"]:has(.register-card){
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.15);
    backdrop-filter:blur(14px);
    border-radius:28px;
    padding:45px;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
}

.stTextInput input{
    background:rgba(255,255,255,.95);
    color:#001d4f;
    border:none;
    border-radius:14px;
    padding:15px;
}

.stButton>button,.stFormSubmitButton>button{
    width:100%;
    padding:14px;
    border-radius:14px;
    border:2px solid #bc9e5a;
    background:transparent;
    color:white;
    font-weight:700;
    transition:.3s;
}

.stButton>button:hover,.stFormSubmitButton>button:hover{
    background:#bc9e5a;
    color:#001d4f;
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
            Create your personalized AI-powered news experience
        </div>
    </div>
    """, unsafe_allow_html=True)

with center:
    st.markdown("<div class='register-card'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c2:
        st.image("assets/profile.png")

    st.markdown("""
    <div class='title'>Create Account</div>
    <div class='sub'>Join Senti News today</div>
    """, unsafe_allow_html=True)

    with st.form("register"):

        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Create a password")
        confirm = st.text_input("Confirm Password", type="password")

        # Password strength
        if password:
            strength = (
                ("Weak", "#ff6b6b") if len(password) < 6 else
                ("Medium", "#ffd166") if len(password) < 10 else
                ("Strong", "#06d6a0")
            )
            st.markdown(
                f"<p style='color:{strength[1]}'>{strength[0]} Password</p>",
                unsafe_allow_html=True
            )

        if st.form_submit_button("Register"):

            if not all([full_name, email, password, confirm]):
                st.warning("Please fill in all fields.")

            elif password != confirm:
                st.error("Passwords do not match.")

            elif len(password) < 6:
                st.warning("Password must be at least 6 characters.")

            else:
                try:
                    with st.spinner("Creating account..."):

                        res = supabase.auth.sign_up({
                            "email": email,
                            "password": password,
                            "options": {
                                "data": {"full_name": full_name}
                            }
                        })

                    if res.user:
                        st.success("Account created successfully!")
                        time.sleep(1.5)
                        st.switch_page("pages/login.py")

                    else:
                        st.error("Registration failed.")

                except Exception as e:
                    st.error(e)

    st.markdown(
        "<div style='text-align:center;margin-top:18px'>Already have an account?</div>",
        unsafe_allow_html=True
    )
    

    col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("Log In Now"):
        st.switch_page("pages/login.py")

    st.markdown("<div class='footer'>© 2026 Senti News</div>", unsafe_allow_html=True)