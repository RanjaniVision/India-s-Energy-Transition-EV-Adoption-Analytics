import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="India EV Adoption Analytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)
# -------------------------
# Custom Theme
# -------------------------

st.markdown("""
<style>

.stApp{
    background-color:#071329;
}

h1,h2,h3{
    color:white;
}

p{
    color:#d9d9d9;
}

[data-testid="stMetric"]{
    background:#0F2744;
    border-radius:15px;
    padding:20px;
    border:1px solid #1D4E89;
    text-align:center;
}

.sidebar .sidebar-content{
    background:#06111F;
}

</style>
""",unsafe_allow_html=True)
# -------------------------
# Load Dataset
# -------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = os.path.join(
    BASE_DIR,
    "Dataset",
    "Indian-EV.xlsx"
)
@st.cache_data
def load_data():

    states = pd.read_excel(FILE_PATH, sheet_name="State_Master")

    ev = pd.read_excel(FILE_PATH, sheet_name="EV_Registrations")

    fuel = pd.read_excel(FILE_PATH, sheet_name="Fuel_Prices")

    charging = pd.read_excel(FILE_PATH, sheet_name="Charging_Stations")

    renewable = pd.read_excel(FILE_PATH, sheet_name="Renewable_Energy")

    renewable["Renewable_MW"] = (
        renewable["Solar_MW"]
        + renewable["Wind_MW"]
        + renewable["Hydro_MW"]
    )

    renewable = renewable[
        ["State_ID", "Month", "Renewable_MW"]
    ]

    charging_summary = charging.groupby("State_ID").agg({
        "Chargers":"sum",
        "Utilization_%":"mean",
        "Uptime_%":"mean"
    }).reset_index()

    df = ev.merge(states,on="State_ID")

    df = df.merge(
        fuel,
        on=["State_ID","Month"]
    )

    df = df.merge(
        renewable,
        on=["State_ID","Month"]
    )

    df = df.merge(
        charging_summary,
        on="State_ID"
    )

    return df,charging,ev,fuel,renewable

df, charging, ev, fuel, renewable = load_data()
# Title
# -------------------------

st.title("⚡ India EV Adoption Analytics Dashboard")

st.markdown("""
<h3 style="color:#FFFFFF; font-weight:bold;">
Sustainable Transportation & Energy Transition
</h3>

<p style="color:#FFFFFF; font-size:18px;">
This dashboard analyzes:
</p>

<ul style="color:#FFFFFF; font-size:17px;">
    <li>EV Adoption</li>
    <li>Charging Infrastructure</li>
    <li>Fuel Prices</li>
    <li>Renewable Energy</li>
    <li>State-wise Performance</li>
</ul>
""", unsafe_allow_html=True)
# ==========================
# SIDEBAR FILTERS
# ==========================

st.sidebar.header("🔍 Dashboard Filters")

states = ["All"] + sorted(df["State"].dropna().unique().tolist())

selected_state = st.sidebar.selectbox(
    "State",
    states
)

months = ["All"] + sorted(df["Month"].astype(str).unique().tolist())

selected_month = st.sidebar.selectbox(
    "Month",
    months
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]

if selected_month != "All":
    filtered_df = filtered_df[
        filtered_df["Month"].astype(str) == selected_month
    ]
    # ==========================================
# FILTER CHARGING DATA
# ==========================================

filtered_charging = charging.copy()

if selected_state != "All":

    state_ids = filtered_df["State_ID"].unique()

    filtered_charging = charging[
        charging["State_ID"].isin(state_ids)
    ]
# ============================================================
# KPI CARDS
# ============================================================

st.markdown("## 📊 Dashboard Overview")

col1, col2, col3, col4, col5, col6 = st.columns(6)

# Total EVs
try:
    total_ev =filtered_df["Total_EV"].sum()
except:
    total_ev = len(ev)

# Charging Stations
try:
    total_station = filtered_charging["Station_ID"].nunique()
except:
    total_station = len(charging)

# Total Chargers
try:
    total_chargers = filtered_charging["Chargers"].sum()
except:
    total_chargers = 0

# Utilization
try:
    avg_utilization = filtered_charging["Utilization_%"].mean()
except:
    avg_utilization = 0

# Uptime
try:
    avg_uptime = filtered_charging["Uptime_%"].mean()
except:
    avg_uptime = 0

# States
try:
    total_states = df["State"].nunique()
except:
    total_states = charging["State"].nunique()

col1.metric(
    "🚗 Total EVs",
    f"{int(total_ev):,}"
)

col2.metric(
    "⚡ Stations",
    total_station
)

col3.metric(
    "🔌 Chargers",
    f"{int(total_chargers):,}"
)

col4.metric(
    "📈 Utilization",
    f"{avg_utilization:.1f}%"
)

col5.metric(
    "🟢 Uptime",
    f"{avg_uptime:.1f}%"
)

col6.metric(
    "🏙 States",
    total_states
)

st.divider()
# ============================================================
# EV ADOPTION BY STATE
# ============================================================

st.subheader("🚗 EV Adoption by State")

try:

    ev_state = (
    filtered_df.groupby("State")["Total_EV"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

    fig = px.bar(
        x=ev_state.values,
        y=ev_state.index,
        orientation="h",
        color=ev_state.values,
        color_continuous_scale="Viridis",
        labels={
            "x":"Total EVs",
            "y":"State"
        },
        title="Top 10 States by EV Adoption"
    )

    fig.update_layout(
        plot_bgcolor="#071329",
        paper_bgcolor="#071329",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

except:

    st.warning("EV_Adoption sheet or EV_Count column not available.")
# ============================================================
# CHARGING STATIONS
# ============================================================

st.subheader("⚡ Top Cities by Charging Stations")

city = filtered_charging["City"].value_counts().head(10)

fig = px.bar(
    x=city.index,
    y=city.values,
    color=city.values,
    color_continuous_scale="Electric",
    labels={
        "x":"City",
        "y":"Stations"
    }
)

fig.update_layout(
    plot_bgcolor="#071329",
    paper_bgcolor="#071329",
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)
# ==========================================================
# CHARTS SECTION
# ==========================================================

col1, col2 = st.columns(2)

# -------------------------
# Charger Type Distribution
# -------------------------

with col1:

    st.subheader("🔌 Charger Type Distribution")

    type_chart = filtered_charging["Type"].value_counts()

    fig = px.pie(
        values=type_chart.values,
        names=type_chart.index,
        hole=0.6,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        paper_bgcolor="#071329",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

## -------------------------
# Charger Distribution
# -------------------------

with col2:

    st.subheader("⚡ Chargers Distribution")

    fig = px.histogram(
        filtered_charging,
        x="Chargers",
        nbins=20,
        color_discrete_sequence=["#00E676"]
    )

    fig.update_layout(
        paper_bgcolor="#071329",
        plot_bgcolor="#071329",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Scatter Plot
# ==========================================================

st.subheader("📈 Utilization vs Uptime")

fig = px.scatter(

    filtered_charging,

    x="Utilization_%",

    y="Uptime_%",

    color="Type",

    size="Chargers",

    hover_name="City"

)

fig.update_layout(
    paper_bgcolor="#071329",
    plot_bgcolor="#071329",
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)
# ==========================================================
# DATA TABLE
# ==========================================================

st.divider()

st.subheader("📋 Charging Station Dataset")

st.dataframe(
    filtered_charging,
    use_container_width=True,
    height=400
)

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

csv = filtered_charging.to_csv(index=False)

st.download_button(

    "⬇ Download Filtered Dataset",

    csv,

    "Charging_Stations.csv",

    "text/csv"

)

# ==========================================================
# AI INSIGHTS
# ==========================================================

st.divider()

st.subheader("🤖 AI Insights")

highest_city = filtered_charging["City"].value_counts().idxmax()
highest_station = filtered_charging["City"].value_counts().max()
avg_util = charging["Utilization_%"].mean()

avg_up = charging["Uptime_%"].mean()

st.success(f"""

### Key Insights

🚗 **Highest Charging Infrastructure:** {highest_city}

⚡ **Charging Stations:** {highest_station}

📈 **Average Utilization:** {avg_util:.2f} %

🟢 **Average Uptime:** {avg_up:.2f} %

🔋 Higher charging infrastructure indicates stronger EV ecosystem.

📍 States with low charging availability should receive priority investment.

""")

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.subheader("💡 Recommendations")

st.info("""

✅ Increase charging stations in low-coverage regions.

✅ Expand DC Fast Charging corridors.

✅ Improve charger uptime above 95%.

✅ Use predictive maintenance for charging stations.

✅ Integrate renewable energy with charging infrastructure.

✅ Encourage EV adoption through government incentives.

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<center>

### ⚡ India EV Adoption Analytics Dashboard

Developed by **Ranjani G**

Python | Streamlit | Plotly 

</center>
""",
unsafe_allow_html=True
)