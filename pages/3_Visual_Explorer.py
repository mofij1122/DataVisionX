import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # [web:17][web:64]

st.set_page_config(page_title="Visual Explorer – DataVisionX", page_icon="📊", layout="wide")

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
        .hint-text {
            font-size: 13px;
            color: #c5c6ff;
        }
        .card-small {
            padding: 0.9rem 1.1rem;
            border-radius: 0.7rem;
            background: #11122e;
            border: 1px solid #2a2b5f;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Visual Explorer</div>', unsafe_allow_html=True)
st.write("Create interactive charts by choosing columns and chart type.")

if "df" not in st.session_state:
    st.warning("No dataset found. Please upload a file in 'Upload & Overview' first.")
    st.stop()

df: pd.DataFrame = st.session_state["df"]

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

with st.expander("Column summary", expanded=False):
    st.write("Numeric columns:", numeric_cols)
    st.write("Categorical columns:", categorical_cols)

controls_col, chart_col = st.columns([0.9, 2])

with controls_col:
    st.markdown('<div class="section-title">Chart settings</div>', unsafe_allow_html=True)

    chart_type = st.selectbox(
        "Chart type",
        ["Histogram", "Bar", "Box", "Scatter", "Line", "Correlation heatmap"],
        help="Select the kind of visualization you want to generate.",
    )

    x_col = st.selectbox(
        "X-axis column",
        options=df.columns,
        index=0,
    )

    y_col = None
    if chart_type in ["Scatter", "Line", "Box", "Bar"]:
        y_options = [c for c in df.columns if c != x_col]
        if y_options:
            y_col = st.selectbox(
                "Y-axis column (optional)",
                options=["(none)"] + y_options,
                index=0,
                help="Select a second column when relevant (e.g., scatter, line).",
            )
            if y_col == "(none)":
                y_col = None

    st.markdown('<div class="hint-text">Optional filters</div>', unsafe_allow_html=True)

    filter_col = st.selectbox(
        "Filter by column (optional)",
        options=["(none)"] + df.columns.tolist(),
        index=0,
    )

    filtered_df = df.copy()
    if filter_col != "(none)":
        if pd.api.types.is_numeric_dtype(df[filter_col]):
            min_val, max_val = float(df[filter_col].min()), float(df[filter_col].max())
            selected_range = st.slider(
                f"Select range for {filter_col}",
                min_val,
                max_val,
                (min_val, max_val),
            )
            filtered_df = filtered_df[
                (filtered_df[filter_col] >= selected_range[0])
                & (filtered_df[filter_col] <= selected_range[1])
            ]
        else:
            unique_vals = sorted(df[filter_col].dropna().unique().tolist())
            selected_vals = st.multiselect(
                f"Select values for {filter_col}",
                options=unique_vals,
                default=unique_vals,
            )
            if selected_vals:
                filtered_df = filtered_df[filtered_df[filter_col].isin(selected_vals)]

    st.markdown(
        '<p class="hint-text">Tip: Use filters to drill down into specific segments of your data.</p>',
        unsafe_allow_html=True,
    )

with chart_col:
    if filtered_df.empty:
        st.error("No data left after applying filters. Adjust filters and try again.")
    else:
        sns.set_style("darkgrid")
        fig, ax = plt.subplots(figsize=(8, 4))
        fig.patch.set_facecolor("#05061a")
        ax.set_facecolor("#05061a")

        if chart_type == "Histogram":
            if not pd.api.types.is_numeric_dtype(filtered_df[x_col]):
                st.error("Histogram requires a numeric X column.")
            else:
                sns.histplot(filtered_df[x_col].dropna(), kde=True, ax=ax, color="#ff4b9f")  # [web:66][web:69]
                ax.set_title(f"Histogram of {x_col}")
        elif chart_type == "Bar":
            if y_col and pd.api.types.is_numeric_dtype(filtered_df[y_col]):
                grouped = filtered_df.groupby(x_col)[y_col].mean().reset_index()
                sns.barplot(data=grouped, x=x_col, y=y_col, ax=ax, color="#4f46e5")  # [web:66]
                ax.set_title(f"Average {y_col} by {x_col}")
                plt.xticks(rotation=45)
            else:
                counts = filtered_df[x_col].value_counts().reset_index()
                counts.columns = [x_col, "count"]
                sns.barplot(data=counts, x=x_col, y="count", ax=ax, color="#4f46e5")
                ax.set_title(f"Count of {x_col}")
                plt.xticks(rotation=45)
        elif chart_type == "Box":
            if not pd.api.types.is_numeric_dtype(filtered_df[x_col]) and y_col and pd.api.types.is_numeric_dtype(filtered_df[y_col]):
                sns.boxplot(data=filtered_df, x=x_col, y=y_col, ax=ax)
                ax.set_title(f"Boxplot of {y_col} by {x_col}")
                plt.xticks(rotation=45)
            elif pd.api.types.is_numeric_dtype(filtered_df[x_col]):
                sns.boxplot(data=filtered_df[x_col], ax=ax)
                ax.set_title(f"Boxplot of {x_col}")
            else:
                st.error("Boxplot needs at least one numeric column.")
        elif chart_type == "Scatter":
            if y_col is None:
                st.error("Scatter plot requires both X and Y columns.")
            elif not (
                pd.api.types.is_numeric_dtype(filtered_df[x_col])
                and pd.api.types.is_numeric_dtype(filtered_df[y_col])
            ):
                st.error("Scatter plot requires numeric X and Y columns.")
            else:
                sns.scatterplot(data=filtered_df, x=x_col, y=y_col, ax=ax, color="#22c55e")  # [web:58][web:64]
                ax