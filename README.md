# 🚗 India EV Adoption & Energy Transition Analytics

An end-to-end Data Analytics project that analyzes India's Electric Vehicle (EV) ecosystem using EV registrations, charging infrastructure, fuel prices, renewable energy, and government subsidy data. The project provides business insights through an interactive Streamlit dashboard to support data-driven decision making for sustainable transportation.

---

## 📌 Business Problem

India is accelerating the adoption of Electric Vehicles (EVs) to reduce fossil fuel dependence and achieve sustainability goals. However, uneven EV adoption, limited charging infrastructure, rising fuel prices, and varying renewable energy capacity make planning and investment decisions challenging.

This project analyzes these factors to identify adoption trends, infrastructure gaps, and investment priorities across different states.

---

## 🎯 Project Objectives

- Analyze EV adoption across Indian states.
- Monitor EV growth trends over time.
- Evaluate charging infrastructure readiness.
- Understand the impact of fuel prices on EV adoption.
- Identify states that require priority investment.
- Support data-driven policy and infrastructure planning.

---

## 📂 Dataset

The project uses six related datasets:

- State Master
- EV Registrations
- Fuel Prices
- Charging Stations
- Renewable Energy
- Government Subsidies

---

## 📊 Dashboard Highlights

### Executive KPIs

- 🚗 Total EV Registrations
- 🔌 Total Charging Stations
- ⛽ Average Petrol Price
- ⛽ Average Diesel Price
- 🌱 Average Renewable Energy Share
- 📈 Monthly EV Growth Rate

---

## 📈 Business Analysis

The dashboard answers the following business questions:

- Which states have the highest EV adoption?
- How has EV adoption changed over time?
- Is the existing charging infrastructure sufficient?
- How do fuel prices influence EV adoption?
- Which states should be prioritized for future investment?

---

## 💡 Key Insights

- EV adoption has steadily increased across India.
- EV adoption varies significantly between states.
- Some states require additional charging infrastructure to support future demand.
- Rising fuel prices are associated with increased EV adoption.
- Renewable energy capacity differs across states, influencing sustainable EV expansion.
- Data-driven investment planning can improve India's EV ecosystem.

---

## 📂 Dataset Structure

The project uses an Excel workbook containing six related datasets. Each sheet represents a different aspect of India's EV ecosystem.

| Dataset | Description | Key Columns |
|----------|-------------|-------------|
| **State_Master** | Master information about Indian states used for mapping and analysis. | `State_ID`, `State`, `Region`, `Population` |
| **EV_Registrations** | Monthly Electric Vehicle registrations categorized by vehicle type. | `Record_ID`, `Month`, `State_ID`, `EV_2W`, `EV_3W`, `EV_4W`, `EV_Buses`, `Total_EV` |
| **Fuel_Prices** | Monthly petrol and diesel prices across states. | `Record_ID`, `Month`, `State_ID`, `Petrol_Price`, `Diesel_Price` |
| **Charging_Stations** | Charging infrastructure details including charger count and utilization. | `Station_ID`, `State_ID`, `Chargers`, `Utilization_%`, `Uptime_%` |
| **Renewable_Energy** | Renewable energy generation and environmental impact by state. | `Record_ID`, `Month`, `State_ID`, `Solar_MW`, `Wind_MW`, `Hydro_MW`, `Renewable_Share_%`, `Estimated_CO2_Reduction_tonnes` |
| **Government_Subsidies** | Government EV subsidy schemes, beneficiaries, and allocated budgets. | `Scheme_ID`, `State_ID`, `Subsidy_INR`, `Beneficiaries`, `Budget_Cr` |

---

## ✅ Business Recommendations

- Expand charging infrastructure in high-demand states.
- Strengthen EV adoption in lower-performing regions.
- Continue financial incentives and awareness programs.
- Promote renewable-powered charging stations.
- Prioritize future investments using data-driven insights.

---

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

---

## 📌 Project Outcome

This project transforms raw government datasets into an interactive business dashboard that helps policymakers monitor EV adoption, evaluate infrastructure readiness, understand fuel price impacts, and prioritize investments for a sustainable transportation future.

---

## 👨‍💻 Author

**RANJANI.G**

Data Analyst | Python|EDA | Streamlit
