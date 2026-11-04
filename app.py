import streamlit as st
import pandas as pd
import joblib

model = joblib.load("predictive_maintenance_model.pkl")

st.set_page_config(page_title="Predictive Maintenance System", page_icon="⚙️")
st.title("Predictive Maintenance System")
st.write("Enter machine operating conditions to estimate machine failure risk.")

machine_type = st.selectbox("Machine Type", ["L", "M", "H"])
air_temperature = st.number_input("Air Temperature (K)", value=300.0, step=0.1)
process_temperature = st.number_input("Process Temperature (K)", value=310.0, step=0.1)
rotational_speed = st.number_input("Rotational Speed (rpm)", min_value=0, value=1500, step=10)
torque = st.number_input("Torque (Nm)", min_value=0.0, value=40.0, step=0.5)
tool_wear = st.number_input("Tool Wear (min)", min_value=0, value=100, step=1)

if st.button("Predict Failure Risk"):
    input_data = pd.DataFrame([{
        "Air temperature [K]": air_temperature,
        "Process temperature [K]": process_temperature,
        "Rotational speed [rpm]": rotational_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear,
        "Type_L": 1 if machine_type == "L" else 0,
        "Type_M": 1 if machine_type == "M" else 0
    }])

    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)
    probability = model.predict_proba(input_data)[0][1]
    st.metric("Estimated Failure Risk", f"{probability * 100:.2f}%")

    if probability >= 0.30:
        st.error("High Risk: The model indicates an elevated failure risk.")
    else:
        st.success("Low Risk: The model indicates a lower failure risk.")

    st.caption("This is a model estimate, not a guarantee of machine condition.")
