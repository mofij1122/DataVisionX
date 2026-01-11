import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # [web:17][web:69]
try:
    import altair as alt
except Exception:
    alt = None

st.set_page_config(page_title="Time Series – DataVisionX", page_icon="⏱", layout="wide")

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
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Time Series Explorer</div>', unsafe_allow_html=True)
st.write("Analyze trends, seasonality, and moving averages for date‑based data.")

if "df" not in st.session_state:
    st.warning("No dataset found. Please upload a file in 'Upload & Overview' first.")
    st.stop()

df: pd.DataFrame = st.session_state["df"].copy()

# Detect potential datetime columns
auto_date_cols = [
    c for c in df.columns
    if pd.api.types.is_datetime64_any_dtype(df[c])
]

if not auto_date_cols:
    # Try to parse any column that looks like date
    for c in df.columns:
        try:
            parsed = pd.to_datetime(df[c])
            df[c] = parsed
            auto_date_cols.append(c)
        except Exception:
            continue

if not auto_date_cols:
    st.error("No suitable date/time column detected. Please ensure your dataset has a date column.")
    st.stop()

date_col = st.selectbox("Select date column", auto_date_cols)
df = df.sort_values(by=date_col)

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
if not numeric_cols:
    st.error("No numeric columns available for time‑series analysis.")
    st.stop()

value_col = st.selectbox("Select value column", numeric_cols)

freq = st.selectbox(
    "Resample frequency",
    options=["D", "W", "M"],
    format_func=lambda x: {"D": "Daily", "W": "Weekly", "M": "Monthly"}[x],
)

window = st.slider("Moving average window (periods)", 1, 60, 7)

df_ts = df[[date_col, value_col]].dropna()
df_ts = df_ts.set_index(date_col).resample(freq).mean()  # [web:74]

if alt is not None:
    try:
        df_plot = df_ts.reset_index().rename(columns={date_col: 'date'})
        df_plot['rolling'] = df_plot[value_col].rolling(window).mean()

        # Create interactive selection for hover effects
        hover = alt.selection_single(on='mouseover', empty='none', nearest=True)

        chart_actual = alt.Chart(df_plot).mark_line(color='#4f46e5', size=2.5, point=alt.OverlayMarkDef(filled=True, size=50)).encode(
            x=alt.X('date:T', title='Date'),
            y=alt.Y(f'{value_col}:Q', title=value_col),
            tooltip=['date:T', f'{value_col}:Q'],
            opacity=alt.condition(hover, alt.value(1), alt.value(0.7))
        ).add_selection(hover)

        chart_ma = alt.Chart(df_plot).mark_line(color='#ff4b9f', size=2.5, strokeDash=[5, 5]).encode(
            x='date:T',
            y=alt.Y('rolling:Q', title=f'Rolling mean ({window})'),
            tooltip=['date:T', alt.Tooltip('rolling:Q', format='.2f')],
            opacity=alt.condition(hover, alt.value(1), alt.value(0.5))
        ).add_selection(hover)

        combined = alt.layer(chart_actual, chart_ma).resolve_scale(y='shared').properties(height=420)
        brush = alt.selection(type='interval', encodings=['x'])
        upper = combined.add_selection(brush).properties(height=120)
        lower = combined.encode(opacity=alt.condition(brush, alt.value(1), alt.value(0.3))).properties(height=360)

        st.altair_chart(alt.vconcat(lower, upper), use_container_width=True)
    except Exception:
        alt = None

if alt is None:
    sns.set_style("darkgrid")
    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#05061a")
    ax.set_facecolor("#05061a")

    ax.plot(df_ts.index, df_ts[value_col], label="Actual", color="#4f46e5")
    ax.plot(df_ts.index, df_ts[value_col].rolling(window).mean(), label=f"Rolling mean ({window})", color="#ff4b9f")

    ax.set_title(f"{value_col} over time ({freq})")
    ax.set_xlabel("Date")
    ax.set_ylabel(value_col)
    ax.legend()

    st.pyplot(fig)  # [web:25][web:23]

st.write("")

st.subheader("Seasonality view")
group_choice = st.selectbox(
    "Group by",
    ["Month", "Day of week"],
)

if group_choice == "Month":
    temp = df_ts.copy()
    temp["month"] = temp.index.month
    seasonal = temp.groupby("month")[value_col].mean()
    x_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    idx = range(1, 13)
else:
    temp = df_ts.copy()
    temp["dow"] = temp.index.dayofweek
    seasonal = temp.groupby("dow")[value_col].mean()
    x_labels = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    idx = range(0, 7)

fig2, ax2 = plt.subplots(figsize=(7, 3))
fig2.patch.set_facecolor("#05061a")
ax2.set_facecolor("#05061a")
sns.barplot(x=list(idx), y=seasonal.values, ax=ax2, color="#22c55e")  # [web:66][web:69]
ax2.set_xticklabels(x_labels)
ax2.set_title(f"Average {value_col} by {group_choice.lower()}")

st.pyplot(fig2)