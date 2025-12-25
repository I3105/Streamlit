import streamlit as st

st.title("BMI Calculator 🏃‍♂️")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (meters)", min_value=0.5, step=0.01)

if st.button("Calculate"):
    bmi = weight / (height ** 2)
    st.write(f"**Your BMI is:** {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")

