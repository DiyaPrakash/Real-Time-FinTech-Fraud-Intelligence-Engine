import streamlit as st
import requests
import random
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Fraud Dashboard", layout="wide")

st.title("💳 Real-Time Fraud Detection Dashboard")

# -----------------------------
# Session Memory
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Helper Functions
# -----------------------------
def create_features(amount, risk):
    txn = {
        "Time": random.uniform(0, 172800),
        "Amount": amount
    }

    if risk == "Low Risk":
        rng = (-1, 1)
    elif risk == "Medium Risk":
        rng = (-3, 3)
    else:
        rng = (-6, 6)

    for i in range(1, 29):
        txn[f"V{i}"] = random.uniform(*rng)

    return txn


def random_transaction():
    return create_features(random.uniform(1, 2000), "Medium Risk")


def call_api(txn):
    try:
        response = requests.post(API_URL, json=txn)
        return response.json()
    except:
        return {"error": "API not reachable"}

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns(2)

# =============================
# MANUAL INPUT
# =============================
with col1:
    st.subheader("Manual Transaction Input")

    amount_input = st.number_input(
        "Transaction Amount",
        min_value=1.0,
        max_value=10000.0,
        value=100.0
    )

    risk_level = st.selectbox(
        "Risk Profile",
        ["Low Risk", "Medium Risk", "High Risk"]
    )

    if st.button("Submit Transaction"):
        txn = create_features(amount_input, risk_level)
        result = call_api(txn)

        if "fraud_probability" in result:

            prob = result["fraud_probability"]
            pred = result["prediction"]

            st.write(f"Fraud Probability: {prob:.4f}")

            if pred == "FRAUD":
                st.error("🚨 FRAUD DETECTED")
            else:
                st.success("✅ LEGIT TRANSACTION")

            # -----------------------------
            # SHAP / Top Features
            # -----------------------------
            if "top_features" in result:
                st.subheader("Top Influencing Features")

                shap_df = pd.DataFrame(
                    result["top_features"].items(),
                    columns=["Feature", "Impact"]
                )

                st.bar_chart(shap_df.set_index("Feature"))

            # -----------------------------
            # Store History
            # -----------------------------
            st.session_state.history.append({
                "Amount": round(amount_input, 2),
                "Risk": risk_level,
                "Fraud Probability": round(prob, 4),
                "Prediction": pred
            })

        else:
            st.warning(result["error"])

# =============================
# RANDOM GENERATOR
# =============================
with col2:
    st.subheader("Auto Generate Transaction")

    if st.button("Generate Random"):
        txn = random_transaction()
        result = call_api(txn)

        if "fraud_probability" in result:

            prob = result["fraud_probability"]
            pred = result["prediction"]

            st.write(f"Amount: {txn['Amount']:.2f}")
            st.write(f"Fraud Probability: {prob:.4f}")

            if pred == "FRAUD":
                st.error("🚨 FRAUD DETECTED")
            else:
                st.success("✅ LEGIT TRANSACTION")

            # -----------------------------
            # SHAP / Top Features
            # -----------------------------
            if "top_features" in result:
                st.subheader("Top Influencing Features")

                shap_df = pd.DataFrame(
                    result["top_features"].items(),
                    columns=["Feature", "Impact"]
                )

                st.bar_chart(shap_df.set_index("Feature"))

            # -----------------------------
            # Store History
            # -----------------------------
            st.session_state.history.append({
                "Amount": round(txn["Amount"], 2),
                "Risk": "Auto",
                "Fraud Probability": round(prob, 4),
                "Prediction": pred
            })

        else:
            st.warning(result["error"])

# =============================
# HISTORY TABLE
# =============================
st.subheader("📊 Transaction History")

if st.button("Clear History"):
    st.session_state.history = []

if st.session_state.history:
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history, use_container_width=True)
else:
    st.write("No transactions yet.")
