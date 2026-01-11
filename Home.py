import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="DataVisionX – Automated EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

# Theme + header
from theme import init_theme, apply_theme
from header import render_header

# Initialize theme, apply global CSS, then draw header
init_theme()
apply_theme()
render_header()

# Professional styling
st.markdown(
    """
    <style>
        html {
            scroll-behavior: smooth;
        }

        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --bg-dark: #0f172a;
            --bg-card: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --accent: #ec4899;
        }
        
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1a1f3a 100%);
            color: var(--text-primary);
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInFromLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes slideInFromRight {
            from {
                opacity: 0;
                transform: translateX(30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .hero-section {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);
            border-radius: 1.5rem;
            border: 1px solid rgba(99, 102, 241, 0.2);
            margin-bottom: 2rem;
            margin-top: -3rem;
            animation: fadeInUp 0.8s ease-out;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 900;
            margin: 0;
            background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: fadeInUp 1s ease-out 0.1s both;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
            animation: fadeInUp 1s ease-out 0.2s both;
        }
        
        .step-card {
            background: linear-gradient(135deg, var(--bg-card) 0%, #293548 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 1rem;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            animation: fadeInUp 0.6s ease-out backwards;
        }
        
        .step-card:nth-child(1) {
            animation-delay: 0.3s;
        }
        
        .step-card:nth-child(2) {
            animation-delay: 0.4s;
        }
        
        .step-card:nth-child(3) {
            animation-delay: 0.5s;
        }
        
        .step-card:nth-child(4) {
            animation-delay: 0.6s;
        }
        
        .step-number {
            display: inline-block;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
            border-radius: 50%;
            line-height: 50px;
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: white;
        }
        
        .step-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .step-title {
            font-size: 1.3rem;
            font-weight: 700;
            margin: 0.5rem 0;
            color: var(--text-primary);
        }
        
        .step-description {
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .feature-box {
            background: var(--bg-card);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 0.8rem;
            padding: 1.5rem;
            transition: all 0.3s ease;
            animation: fadeInUp 0.6s ease-out backwards;
        }
        
        .feature-box:nth-child(1) {
            animation-delay: 0.7s;
        }
        
        .feature-box:nth-child(2) {
            animation-delay: 0.75s;
        }
        
        .feature-box:nth-child(3) {
            animation-delay: 0.8s;
        }
        
        .feature-box:nth-child(4) {
            animation-delay: 0.85s;
        }
        
        .feature-box:nth-child(5) {
            animation-delay: 0.9s;
        }
        
        .feature-box:nth-child(6) {
            animation-delay: 0.95s;
        }
        
        .feature-box:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
            background: linear-gradient(135deg, var(--bg-card) 0%, #293548 100%);
        }
        
        .feature-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .feature-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 0.5rem 0;
        }
        
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: 600;
            margin-top: 1rem;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: none;
            cursor: pointer;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
        }
        
        .divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
            margin: 2rem 0;
            animation: slideInFromLeft 0.8s ease-out 0.6s both;
        }
        
        @keyframes formSlideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .form-section {
            animation: fadeInUp 0.8s ease-out 1s both;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            transform: scale(1.01);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
            transition: all 0.2s ease;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <h1 class="hero-title">DataVisionX</h1>
        <p class="hero-subtitle">Automated Exploratory Data Analysis. Instant insights, zero hassle.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# Smooth scroll JavaScript for hash navigation
st.markdown(
    """
    <script>
    function scrollToElement(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            element.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    }

    // Check if there's a hash on page load
    if (window.location.hash) {
        const anchor = window.location.hash.substring(1);
        setTimeout(() => scrollToElement(anchor), 100);
    }

    // Listen for hash changes
    window.addEventListener('hashchange', () => {
        const anchor = window.location.hash.substring(1);
        if (anchor) scrollToElement(anchor);
    });
    </script>
    """,
    unsafe_allow_html=True,
)

# About section anchor
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("## About DataVisionX")
st.markdown("""
DataVisionX is an all-in-one platform designed to simplify data preprocessing. It automatically handles data cleaning by removing missing values, fixing inconsistencies, and preparing your dataset for Exploratory Data Analysis (EDA) and machine learning workflows. By streamlining the preparation stage, DataVisionX enables users to concentrate on uncovering insights and building strong predictive models without spending time on tedious manual cleaning tasks.
""")

st.markdown("---")

# How It Works section anchor
st.markdown('<div id="howitworks"></div>', unsafe_allow_html=True)
st.markdown("## How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-icon">📤</div>
            <div class="step-title">Upload Data</div>
            <div class="step-description">Upload your CSV or Excel file in one click</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-icon">🔍</div>
            <div class="step-title">Explore</div>
            <div class="step-description">Get instant visualizations and data insights</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-icon">📊</div>
            <div class="step-title">Analyze</div>
            <div class="step-description">Discover patterns and actionable insights</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">4</div>
            <div class="step-icon">📥</div>
            <div class="step-title">Export</div>
            <div class="step-description">Download reports and cleaned datasets</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Key Features
st.markdown("## Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Fast Analysis</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Process large datasets instantly with automated analysis</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Rich Visualizations</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Beautiful, interactive charts and heatmaps for deeper insights</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">💾</div>
            <div class="feature-title">Easy Export</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Download reports, insights, and cleaned data in one go</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">✅</div>
            <div class="feature-title">Data Quality Checks</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Automatic detection of missing values, outliers, and duplicates</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Smart Insights</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Rule-based recommendations tailored to your data</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">📅</div>
            <div class="feature-title">Time Series Ready</div>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">Analyze trends and seasonality in temporal data</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Get Started section anchor (used by "Try Our Model" button)
st.markdown('<div id="UploadandOverview"></div>', unsafe_allow_html=True)
st.markdown("## Get Started Now")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1rem;">
                Ready to unlock insights from your data? Start uploading now.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info("Use the sidebar to navigate to **Upload & Overview** and start your analysis journey!")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Leave a Review
st.markdown('<div style="animation: fadeInUp 0.8s ease-out 1s both;"></div>', unsafe_allow_html=True)
st.markdown("## Leave a Review")
st.markdown("We value your feedback! Share your experience with DataVisionX.")

review_col1, review_col2 = st.columns(2)
with review_col1:
    review_name = st.text_input("Name", placeholder="Your name", key="review_name")
    review_email = st.text_input("Email", placeholder="your.email@example.com", key="review_email")

with review_col2:
    review_rating = st.selectbox("Rating", options=["⭐⭐⭐⭐⭐ Excellent", "⭐⭐⭐⭐ Good", "⭐⭐⭐ Average", "⭐⭐ Poor"], key="review_rating")

review_message = st.text_area("Your Review", placeholder="Share your thoughts about DataVisionX...", height=120, key="review_message")

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Submit Review", use_container_width=True, key="submit_review"):
        if review_name and review_email and review_message:
            st.success(f"Thank you {review_name}! Your review has been submitted successfully. We appreciate your feedback!")
        else:
            st.error("Please fill in all fields before submitting.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Contact Us section anchor
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div style="animation: fadeInUp 0.8s ease-out 1.1s both;"></div>', unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("If you'd like to reach out directly, you can email us at **ayanbargir6@gmail.com**")

contact_subject = st.text_input("Subject", placeholder="Subject", key="contact_subject")
contact_message = st.text_area("Message", placeholder="Write your message here...", height=140, key="contact_message")

if st.button("Contact via Email", key="submit_contact"):
    if contact_subject and contact_message:
        mailto = f"mailto:ayanbargir6@gmail.com?subject={urllib.parse.quote(contact_subject)}&body={urllib.parse.quote(contact_message)}"
        st.markdown(f"[Open email client to send message]({mailto})")
        st.success("A new email draft should open in your default mail client.")
    else:
        st.error("Please provide both a subject and a message before contacting.")

# Login anchor (for header Login button)
st.markdown('<div id="Login"></div>', unsafe_allow_html=True)