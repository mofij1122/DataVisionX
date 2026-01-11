import streamlit as st

st.set_page_config(
    page_title="Login - DataVisionX",
    page_icon="🔐",
    layout="centered"
)

# Apply theme
from theme import init_theme, apply_theme
from header import render_header

init_theme()
apply_theme()  # Changed from apply_theme_css()
render_header()

# Custom styling for login page
st.markdown("""
<style>
.login-container {
    max-width: 450px;
    margin: 2rem auto;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
}

.login-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.login-subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

.stButton > button {
    width: 100%;
    padding: 0.75rem;
    font-size: 1.1rem;
    margin-top: 1rem;
}

.divider {
    text-align: center;
    margin: 1.5rem 0;
    color: #64748b;
    position: relative;
}

.divider::before,
.divider::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 40%;
    height: 1px;
    background: rgba(99, 102, 241, 0.2);
}

.divider::before { left: 0; }
.divider::after { right: 0; }

.signup-link {
    text-align: center;
    margin-top: 1.5rem;
    color: #cbd5e1;
}

.signup-link a {
    color: #6366f1;
    font-weight: 600;
    text-decoration: none;
}

.signup-link a:hover {
    color: #ec4899;
}
</style>
""", unsafe_allow_html=True)

# Login Container
st.markdown('<div class="login-container">', unsafe_allow_html=True)

st.markdown("""
<div class="login-title">Welcome Back</div>
<div class="login-subtitle">Sign in to continue to DataVisionX</div>
""", unsafe_allow_html=True)

# Login Form
with st.form("login_form"):
    email = st.text_input("Email", placeholder="your@email.com", key="login_email")
    password = st.text_input("Password", type="password", placeholder="••••••••", key="login_password")

    col1, col2 = st.columns(2)
    with col1:
        remember = st.checkbox("Remember me")
    with col2:
        st.markdown('<div style="text-align: right; margin-top: 0.5rem;"><a href="#" style="color: #6366f1; text-decoration: none; font-size: 0.9rem;">Forgot password?</a></div>', unsafe_allow_html=True)

    submit = st.form_submit_button("Sign In")

    if submit:
        if email and password:
            # Add your authentication logic here
            st.success("✓ Login successful!")
            st.balloons()
            # Redirect to main page
            st.switch_page("Home.py")
        else:
            st.error("Please enter both email and password")

st.markdown('<div class="divider">OR</div>', unsafe_allow_html=True)

# Social Login
col1, col2 = st.columns(2)
with col1:
    if st.button("🔵 Google", use_container_width=True, type="secondary"):
        st.info("Google login coming soon!")

with col2:
    if st.button("⚫ GitHub", use_container_width=True, type="secondary"):
        st.info("GitHub login coming soon!")

# Signup Link
st.markdown("""
<div class="signup-link">
    Don't have an account? <a href="#">Sign up</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #64748b; font-size: 0.85rem;">
    By signing in, you agree to our <a href="#" style="color: #6366f1;">Terms</a> and <a href="#" style="color: #6366f1;">Privacy Policy</a>
</div>
""", unsafe_allow_html=True)