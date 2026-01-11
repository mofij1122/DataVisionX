import streamlit as st
from theme import init_theme, get_theme, toggle_theme


def render_header() -> None:
    init_theme()
    theme = get_theme()

    # Theme-based colors
    if theme == "dark":
        bg_color = "rgba(15, 23, 42, 0.96)"
        border_color = "rgba(99, 102, 241, 0.45)"
        text_color = "#e5e7eb"
        secondary = "#cbd5e1"
    else:
        bg_color = "rgba(248, 250, 252, 0.98)"
        border_color = "rgba(148, 163, 184, 0.8)"
        text_color = "#0f172a"
        secondary = "#475569"

    # CSS
    st.markdown(
        f"""
        <style>
        /* Hide default Streamlit header */
        [data-testid="stHeader"] {{
            display: none !important;
        }}

        /* Fixed custom header */
        .dvx-header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background: {bg_color};
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid {border_color};
            padding: 0.65rem 1.75rem;
            box-shadow: 0 4px 24px rgba(15, 23, 42, 0.75);
        }}

        .dvx-header-inner {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .dvx-left {{
            display: flex;
            align-items: center;
            gap: 0.9rem;
        }}

        .dvx-menu {{
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: rgba(99,102,241,0.09);
            border: 1px solid rgba(99,102,241,0.45);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: {text_color};
            font-size: 1.35rem;
            transition: all 0.25s ease;
        }}

        .dvx-menu:hover {{
            transform: scale(1.05);
            background: rgba(99,102,241,0.2);
        }}

        .dvx-logo {{
            display: flex;
            align-items: center;
            gap: 0.55rem;
        }}

        .dvx-logo-icon {{
            font-size: 1.9rem;
        }}

        .dvx-logo-text {{
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            cursor: pointer;
        }}

        .dvx-nav {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .dvx-nav a {{
            padding: 0.55rem 1.0rem;
            border-radius: 999px;
            font-size: 0.95rem;
            font-weight: 500;
            color: {secondary};
            text-decoration: none;
            transition: all 0.22s ease;
            cursor: pointer;
        }}

        .dvx-nav a:hover {{
            color: {text_color};
            background: rgba(99,102,241,0.18);
            transform: translateY(-1px);
        }}

        .dvx-cta {{
            background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899) !important;
            color: #ffffff !important;
            box-shadow: 0 4px 18px rgba(99,102,241,0.55);
            font-weight: 600 !important;
        }}

        .dvx-right {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .dvx-theme {{
            width: 40px;
            height: 40px;
            border-radius: 12px;
            background: rgba(148,163,184,0.16);
            border: 1px solid rgba(148,163,184,0.55);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            color: {text_color};
            cursor: pointer;
            transition: all 0.25s ease;
        }}

        .dvx-theme:hover {{
            transform: rotate(18deg) scale(1.08);
            background: rgba(129,140,248,0.22);
        }}

        .dvx-login {{
            padding: 0.5rem 1.15rem;
            border-radius: 999px;
            border: 2px solid rgba(129,140,248,0.7);
            color: {text_color};
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.22s ease;
            cursor: pointer;
        }}

        .dvx-login:hover {{
            background: rgba(129,140,248,0.22);
            box-shadow: 0 4px 18px rgba(129,140,248,0.6);
            transform: translateY(-1px);
        }}

        /* Push content below fixed header */
        .main .block-container {{
            padding-top: 5.2rem !important;
        }}

        /* Hide navigation helper buttons */
        .dvx-nav-buttons {{
            position: absolute !important;
            visibility: hidden !important;
            pointer-events: none !important;
            width: 0 !important;
            height: 0 !important;
            overflow: hidden !important;
            opacity: 0 !important;
        }}

        /* Mobile */
        @media (max-width: 960px) {{
            .dvx-nav {{
                display: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # HTML with proper IDs for JavaScript
    st.markdown(
        """
        <div class="dvx-header">
            <div class="dvx-header-inner">
                <div class="dvx-left">
                    <div class="dvx-menu" onclick="const sidebar = document.querySelector('[data-testid=\\'collapsedControl\\']'); if(sidebar) sidebar.click();">
                        &#9776;
                    </div>
                    <div class="dvx-logo" id="home-link">
                        <span class="dvx-logo-icon">📊</span>
                        <span class="dvx-logo-text">DataVisionX</span>
                    </div>
                </div>
                <nav class="dvx-nav">
                    <a href="#about" id="about-link">About Us</a>
                    <a href="#howitworks" id="howitworks-link">How it works</a>
                    <a class="dvx-cta" id="upload-link">Try Our Model</a>
                </nav>
                <div class="dvx-right">
                    <div class="dvx-theme" id="theme-toggle-icon">🌓</div>
                    <a class="dvx-login" id="login-link">Login</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Hidden navigation buttons in a container with CSS class
    st.markdown('<div class="dvx-nav-buttons">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("theme", key="theme_toggle_btn", help="Toggle theme"):
            toggle_theme()
            st.rerun()
    
    with col2:
        if st.button("upload", key="upload_nav_btn", help="Go to Upload"):
            st.switch_page("pages/1_Upload_and_Overview.py")
    
    with col3:
        if st.button("login", key="login_nav_btn", help="Go to Login"):
            st.switch_page("pages/6_Login.py")
    
    with col4:
        if st.button("home", key="home_nav_btn", help="Go to Home"):
            st.switch_page("Home.py")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # JavaScript to trigger hidden buttons
    st.markdown(
        """
        <script>
        setTimeout(function() {
            // Theme toggle
            const themeIcon = document.getElementById('theme-toggle-icon');
            if (themeIcon) {
                themeIcon.addEventListener('click', function() {
                    const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
                    buttons.forEach(btn => {
                        if (btn.textContent.includes('theme') || btn.title === 'Toggle theme') {
                            btn.click();
                        }
                    });
                });
            }
            
            // Upload page
            const uploadLink = document.getElementById('upload-link');
            if (uploadLink) {
                uploadLink.addEventListener('click', function(e) {
                    e.preventDefault();
                    const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
                    buttons.forEach(btn => {
                        if (btn.textContent.includes('upload') || btn.title === 'Go to Upload') {
                            btn.click();
                        }
                    });
                });
            }
            
            // Login page
            const loginLink = document.getElementById('login-link');
            if (loginLink) {
                loginLink.addEventListener('click', function(e) {
                    e.preventDefault();
                    const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
                    buttons.forEach(btn => {
                        if (btn.textContent.includes('login') || btn.title === 'Go to Login') {
                            btn.click();
                        }
                    });
                });
            }
            
            // Home page
            const homeLink = document.getElementById('home-link');
            if (homeLink) {
                homeLink.addEventListener('click', function() {
                    const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
                    buttons.forEach(btn => {
                        if (btn.textContent.includes('home') || btn.title === 'Go to Home') {
                            btn.click();
                        }
                    });
                });
            }
        }, 300);
        </script>
        """,
        unsafe_allow_html=True,
    )