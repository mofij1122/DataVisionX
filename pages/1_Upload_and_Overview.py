import streamlit as st
import pandas as pd  # [web:46][web:49]

st.set_page_config(page_title="Upload & Overview – DataVisionX", page_icon="📂", layout="wide")

from header import render_header
render_header()

st.markdown(
    """
    <style>
        .main {
            background-color: #05061a;
            color: #f5f5ff;
        }
        .section-title {
            font-size: 24px;
            font-weight: 700;
            margin-top: 0.5rem;
            color: #ffffff;
        }
        .card-small {
            padding: 0.9rem 1.1rem;
            border-radius: 0.7rem;
            background: #11122e;
            border: 1px solid #2a2b5f;
            text-align: left;
        }
        .metric-label {
            font-size: 13px;
            color: #c5c6ff;
        }
        .metric-value {
            font-size: 22px;
            font-weight: 700;
            color: #ff4b9f;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Upload Dataset & Overview</div>', unsafe_allow_html=True)
st.write("Upload a CSV or Excel file to start automated EDA.")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx", "xls"],
    help="Supported formats: .csv, .xlsx, .xls",  # [web:46]
)

if uploaded_file is not None:
    # Try reading as CSV, then as Excel
    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        df = pd.read_excel(uploaded_file)  # [web:43][web:49]

    st.session_state["df"] = df

    st.write("")
    st.markdown('<div class="section-title">Dataset Snapshot</div>', unsafe_allow_html=True)
    st.dataframe(df.head(), use_container_width=True)

    n_rows, n_cols = df.shape
    total_cells = n_rows * n_cols if n_rows and n_cols else 0
    missing_cells = df.isna().sum().sum()
    missing_pct = (missing_cells / total_cells * 100) if total_cells else 0

    if missing_pct < 5:
        quality = "Excellent"
        quality_color = "#22c55e"
    elif missing_pct < 20:
        quality = "Good"
        quality_color = "#eab308"
    else:
        quality = "Needs Attention"
        quality_color = "#f97316"

    col_a, col_b, col_c, col_d = st.columns(4)

    with col_a:
        st.markdown(
            f"""
            <div class="card-small">
                <div class="metric-label">Rows</div>
                <div class="metric-value">{n_rows}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_b:
        st.markdown(
            f"""
            <div class="card-small">
                <div class="metric-label">Columns</div>
                <div class="metric-value">{n_cols}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c:
        st.markdown(
            f"""
            <div class="card-small">
                <div class="metric-label">Missing Cells (%)</div>
                <div class="metric-value">{missing_pct:.1f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_d:
        st.markdown(
            f"""
            <div class="card-small">
                <div class="metric-label">Data Quality</div>
                <div class="metric-value" style="color:{quality_color};">{quality}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    with st.expander("View column details"):
        col_info = pd.DataFrame(
            {
                "Column": df.columns,
                "Type": df.dtypes.astype(str),
                "Missing %": df.isna().mean().values * 100,
            }
        )
        st.dataframe(col_info, use_container_width=True)

else:
    st.info("No file uploaded yet. Use the uploader above to select a CSV or Excel file.")