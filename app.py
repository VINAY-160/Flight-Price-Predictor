import streamlit as st
import pandas as pd
import pickle

# =====================================================

# PAGE CONFIG

# =====================================================

st.set_page_config(
page_title="Flight Fare Prediction",
page_icon="✈️",
layout="wide"
)

# =====================================================

# LOAD MODEL

# =====================================================

with open("flight_price_model.pkl", "rb") as f:
    loaded = pickle.load(f)

model = loaded["model"] if isinstance(loaded, dict) else loaded

# =====================================================

# HEADER

# =====================================================

st.title("✈️ Flight Fare Prediction System")
st.markdown(
"""
Predict airline ticket prices using a Machine Learning model trained on historical flight data.

This application uses features such as journey date, departure time,
arrival time, flight duration, number of stops, airline, source, and destination.
"""
)

st.divider()

# =====================================================

# FEATURE GUIDE

# =====================================================

with st.expander("📘 Feature Guide"):
    st.markdown("""

### Feature Explanations

| Feature            | Description              | Typical Range       |
| ------------------ | ------------------------ | ------------------- |
| Journey Month      | Month of travel          | 1 - 12              |
| Journey Day        | Day of month             | 1 - 31              |
| Journey Weekday    | Day of week              | 0(Mon) - 6(Sun)     |
| Departure Hour     | Flight departure hour    | 0 - 23              |
| Departure Minute   | Flight departure minute  | 0 - 59              |
| Arrival Hour       | Flight arrival hour      | 0 - 23              |
| Arrival Minute     | Flight arrival minute    | 0 - 59              |
| Duration Total Min | Total flight duration    | 30 - 3000           |
| Stops              | Number of stops          | 0 - 4               |
| Airline Enc        | Encoded airline value    | Depends on training |
| Source Enc         | Encoded source city      | Depends on training |
| Destination Enc    | Encoded destination city | Depends on training |
| """)                                      
# =====================================================

# INPUTS

# =====================================================

left, right = st.columns(2)

with left:


    st.subheader("📅 Journey Details")

journey_month = st.selectbox(
    "Journey Month",
    range(1,13),
    help="Month in which the journey occurs."
)

journey_day = st.selectbox(
    "Journey Day",
    range(1,32),
    help="Day of month."
)

journey_weekday = st.selectbox(
    "Journey Weekday",
    range(0,7),
    help="0=Monday, 6=Sunday"
)

st.subheader("🛫 Departure")

dep_hour = st.slider(
    "Departure Hour",
    0,
    23,
    10
)

dep_minute = st.slider(
    "Departure Minute",
    0,
    59,
    30
)

stops = st.selectbox(
    "Number of Stops",
    [0,1,2,3,4]
)


with right:


    st.subheader("🛬 Arrival")

arrival_hour = st.slider(
    "Arrival Hour",
    0,
    23,
    13
)

arrival_minute = st.slider(
    "Arrival Minute",
    0,
    59,
    15
)

duration_total_min = st.number_input(
    "Duration (Minutes)",
    min_value=30,
    max_value=3000,
    value=180,
    help="Total travel duration."
)

st.subheader("🔢 Encoded Features")

airline_enc = st.number_input(
    "Airline Encoded Value",
    min_value=0,
    max_value=50,
    value=0,
    help="Encoded airline used during model training."
)

source_enc = st.number_input(
    "Source Encoded Value",
    min_value=0,
    max_value=50,
    value=0,
    help="Encoded source city."
)

destination_enc = st.number_input(
    "Destination Encoded Value",
    min_value=0,
    max_value=50,
    value=0,
    help="Encoded destination city."
)


st.divider()

# =====================================================

# PREDICTION

# =====================================================

if st.button("🚀 Predict Flight Fare", use_container_width=True):


    input_df = pd.DataFrame([{
    'Journey_Month': journey_month,
    'Journey_Day': journey_day,
    'Journey_Weekday': journey_weekday,
    'Dep_Hour': dep_hour,
    'Dep_Minute': dep_minute,
    'Arrival_Hour': arrival_hour,
    'Arrival_Minute': arrival_minute,
    'Duration_Total_Min': duration_total_min,
    'Stops': stops,
    'Airline_enc': airline_enc,
    'Source_enc': source_enc,
    'Destination_enc': destination_enc
}])

prediction = model.predict(input_df)[0]

st.success(
    f"💰 Predicted Flight Fare: ₹ {prediction:,.2f}"
)

st.subheader("Input Summary")
st.dataframe(input_df)


st.divider()

st.caption(
"Built using Machine Learning, Streamlit, Pandas and Scikit-Learn"
)
