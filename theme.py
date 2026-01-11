import streamlit as st


def init_theme(default: str = "dark") -> None:
    """Ensure theme is stored in session_state."""
    if "theme" not in st.session_state:
        st.session_state["theme"] = default


def get_theme() -> str:
    """Return current theme ('dark' or 'light')."""
    return st.session_state.get("theme", "dark")


def toggle_theme() -> None:
    """Flip between dark and light."""
    init_theme()
    current = get_theme()
    st.session_state["theme"] = "light" if current == "dark" else "dark"


def apply_theme_css() -> None:
    """Backward‑compat; safe no‑op."""
    pass


def apply_theme() -> None:
    """Apply global colors based on theme."""
    init_theme()
    theme = get_theme()

    if theme == "dark":
        st.markdown(
            """
            <style>
            :root {
                --primary: #6366f1;
                --primary-dark: #4f46e5;
                --bg-dark: #020617;
                --bg-card: #111827;
                --text-primary: #e5e7eb;
                --text-secondary: #9ca3af;
                --accent: #ec4899;
            }
            body {
                background: radial-gradient(circle at top, #111827 0, #020617 55%, #000000 100%);
                color: var(--text-primary);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            :root {
                --primary: #4f46e5;
                --primary-dark: #312e81;
                --bg-dark: #f9fafb;
                --bg-card: #ffffff;
                --text-primary: #0f172a;
                --text-secondary: #4b5563;
                --accent: #db2777;
            }
            body {
                background: radial-gradient(circle at top, #e5e7eb 0, #f9fafb 55%, #ffffff 100%);
                color: var(--text-primary);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )