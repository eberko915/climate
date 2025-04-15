# Import libraries

import streamlit as st
import pandas as pd
from src.parametric_triggers import detect_streak_trigger
from src.claim_classifier import classify_claims


st.set_page_config(page_title="Insurance Claim Analysis", page_icon=":guardsman:", layout="wide")

st.title("Insurance Claim Analysis")

# -- Upload Data --

st.sidebar.header("Upload Data")
climate_file = st.sidebar.file_uploader("Upload Climate Data CSV", type=["csv"])
claims_file = st.sidebar.file_uploader("Upload Claims Data CSV", type=["csv"])

# -- Trigger Settings --

st.sidebar.header("Payout Rule Settings")
trigger_column = st.sidebar.selectbox("Trigger Type", ["temp_3day_avg", "precip_3day_avg"])
threshold = st.sidebar.slider("Trigger Threshold", min_value=0.0, max_value=50.0, value=30.0)
min_streak = st.sidebar.slider("Minimum Streak Days", min_value=1, max_value=10, value=3)

## -- Main Functionality --

if climate_file and claims_file:
    climate_df = pd.read_csv(climate_file, parse_dates=['date'])
    claims_df = pd.read_csv(claims_file, parse_dates=['date'])

    # Recompute rolling averages for relevant element

    if trigger_column == "temp_3day_avg":
        climate_df['trigger_column'] = climate_df['temperature_c'].rolling(window=3).mean()
    else:
        climate_df['trigger_column'] = climate_df['precipitation_mm'].rolling(window=3).mean()

    # Detect streaks in the climate data

    climate_df = detect_streak_trigger(climate_df, 'trigger_column', threshold, min_streak)
    climate_df = climate_df.rename(columns={'triggered': 'climate_triggered'})

    # Claims using rule-based classifier
    claims_df = classify_claims(claims_df, text_column='claim_text')

    # Merge climate and claims data
    merged = pd.merge(claims_df, climate_df, on=['location', 'date'], how='left')
    merged['insurance_decision'] = merged['payout_triggered'] & merged['climate_triggered']

    # Display results
    st.subheader("Payout decision")
    merged['insurance_decision_display'] = merged['insurance_decision'].apply(lambda x: "$$$" if x else "No")
    st.dataframe(merged[['location', 'date', 'claim_text', 'payout_triggered', 'climate_triggered', 'insurance_decision_display']])

else:
    st.warning("Please upload both climate and claims data files.")