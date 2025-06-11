import streamlit as st
import pandas as pd
import joblib 

model = joblib.load("student_pass_model.pkl")

st.title("🎓 Student Pass Prediction App")
st.write("Fill in the student’s details to predict if they will **Pass or Fail**.")

G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)
studytime = st.selectbox("Weekly Study Time (hours)", [1, 2, 3, 4])
failures = st.selectbox("Number of Past Class Failures", [0, 1, 2, 3])
absences = st.slider("Number of Absences", 0, 100, 5)

if st.button("Predict"):
    input_data = pd.DataFrame([[G1, G2, studytime, failures, absences]],
                              columns=['G1', 'G2', 'studytime', 'failures', 'absences'])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The student is likely to **Pass**.")
    else:
        st.error("❌ The student is likely to **Fail**.")
