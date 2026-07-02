import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

st.set_page_config(
    page_title="Charging Stations Dashboard",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# Find Excel File Automatically
# --------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

excel_files = glob.glob(
    os.path.join(
        BASE_DIR,
        "India-s-Energy-Transition-EV-Adoption-Analytics",
        "*.xlsx"
    )
)

if len(excel_files) == 0:
    st.error("❌ No Excel file found inside 'India-s-Energy-Transition-EV-Adoption-Analytics' folder.")
    st.stop()

FILE_PATH = excel_files[0]

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

charging = pd.read_excel(
    FILE_PATH,
    sheet_name="Charging_Stations"
)

# --------------------------------------------------
# Dashboard Title
# --------------------------------------------------

st.title("⚡ Charging Stations Dashboard")

st.markdown(
"""
Analysis of India's EV Charging Infrastructure
"""
)

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Stations",
    charging["Station_ID"].nunique()
)

col2.metric(
    "Total Chargers",
    int(charging["Chargers"].sum())
)

col3.metric(
    "Average Utilization",
    f"{charging['Utilization_%'].mean():.2f}%"
)

col4.metric(
    "Average Uptime",
    f"{charging['Uptime_%'].mean():.2f}%"
)

st.divider()

# --------------------------------------------------
# Chart 1
# --------------------------------------------------

st.subheader("Top 10 Cities by Charging Stations")

city = charging["City"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,5))

city.plot(kind="bar", ax=ax)

ax.set_xlabel("City")
ax.set_ylabel("Stations")
ax.set_title("Charging Stations by City")

plt.xticks(rotation=45)

st.pyplot(fig)

# --------------------------------------------------
# Chart 2
# --------------------------------------------------

st.subheader("Average Utilization by Charger Type")

util = charging.groupby("Type")["Utilization_%"].mean()

fig, ax = plt.subplots(figsize=(7,4))

util.plot(kind="bar", ax=ax)

ax.set_xlabel("Type")
ax.set_ylabel("Average Utilization (%)")
ax.set_title("Utilization by Charger Type")

st.pyplot(fig)

# --------------------------------------------------
# Chart 3
# --------------------------------------------------

st.subheader("Distribution of Chargers")

fig, ax = plt.subplots(figsize=(7,4))

charging["Chargers"].plot(
    kind="hist",
    bins=10,
    ax=ax
)

ax.set_xlabel("Chargers")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Chargers")

st.pyplot(fig)

st.divider()

# --------------------------------------------------
# Raw Data
# --------------------------------------------------

st.subheader("Charging Stations Data")

st.dataframe(charging, use_container_width=True)

st.divider()

# --------------------------------------------------
# Insights
# --------------------------------------------------

st.subheader("📈 Insights")

st.info(f"""
• Total charging stations available: **{charging['Station_ID'].nunique()}**

• Average charger utilization is **{charging['Utilization_%'].mean():.2f}%**

• Average uptime is **{charging['Uptime_%'].mean():.2f}%**

• Cities with more charging stations indicate stronger EV infrastructure.
""")

# --------------------------------------------------
# Recommendations
# --------------------------------------------------

st.subheader("💡 Recommendations")

st.success("""
✔ Increase charging stations in cities with fewer installations.

✔ Improve charger utilization through better planning.

✔ Maintain uptime above 95%.

✔ Expand fast charging infrastructure.

✔ Monitor charger usage regularly for efficient maintenance.
""")