import streamlit as st
import pandas as pd
import joblib
from preprocessing import data_preprocessing, marital_status_map, application_mode_map, course_map, previous_qualification_map, parent_qualification_map, parents_occupation_map
from prediction import prediction

st.header('Student Dropout Prediction Application')
st.subheader('Jaya Jaya Maju Institute')
st.text('by: I Made Putra Utama')

data = pd.DataFrame()

# identitas mahasiswa
st.subheader("Student Identity")
col1, col2 = st.columns(2)
with col1:
    marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()), index=None, placeholder="Select status...")
    gender = st.selectbox("Gender", ["Male", "Female"], index=None, placeholder="Male or Female")
    course = st.selectbox("Course", list(course_map.keys()), index=None, placeholder="Select course...")

with col2:
    debtor = st.selectbox("Outstanding Debt", ["Yes", "No"], index=None, placeholder="Yes or No")
    tuition_up_to_date = st.selectbox("Tuition Fees are Up to Date", ["Yes", "No"], index=None, placeholder="Yes or No")
    scholarship = st.selectbox("Scholarship Holder", ["Yes", "No"], index=None, placeholder="Yes or No")

# data Pendaftaran
st.subheader("Enrollment Data")
age_at_enroll = st.number_input("Age at Enrollment", min_value=15, max_value=80, step=1)
application_mode = st.selectbox("Application Mode", list(application_mode_map.keys()), index=None, placeholder="Select application mode...")
admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0)
prev_qualification = st.selectbox("Previous Qualification", list(previous_qualification_map.keys()), index=None, placeholder="Select previous qualification...")
prev_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0)

# informasi orang Tua
st.subheader("Parent Information")
col1, col2 = st.columns(2)
with col1:
    mother_qual = st.selectbox("Mother's Qualification", list(parent_qualification_map.keys()), index=None, placeholder="Select mother's qualification...")
    father_qual = st.selectbox("Father's Qualification", list(parent_qualification_map.keys()), index=None, placeholder="Select father's qualification...")

with col2:
    mother_job = st.selectbox("Mother's Occupation", list(parents_occupation_map.keys()), index=None, placeholder="Select mother's occupation...")
    father_job = st.selectbox("Father's Occupation", list(parents_occupation_map.keys()), index=None, placeholder="Select father's occupation...")

# data akademik semester 1
st.subheader("1st Semester Academic Data")
col1, col2 = st.columns(2)
with col1:
    sem1_enrolled = st.number_input("Curricular Units Enrolled", min_value=0)
    sem1_eval = st.number_input("Curricular Units with Evaluation", min_value=0)
with col2:
    sem1_approved = st.number_input("Curricular Units Approved", min_value=0)
    sem1_grade = st.number_input("Grade", min_value=0.0, max_value=20.0)

# data akademik semester 2
st.subheader("2nd Semester Academic Data")
col1, col2 = st.columns(2)
with col1:
    sem2_enrolled = st.number_input("Curricular Units Enrolled", min_value=0, key="sem2_enrolled")
    sem2_eval = st.number_input("Curricular Units with Evaluation", min_value=0, key="sem2_eval")
with col2:
    sem2_approved = st.number_input("Curricular Units Approved", min_value=0, key="sem2_approved")
    sem2_grade = st.number_input("Grade", min_value=0.0, max_value=20.0, key="sem2_grade")

input_data = {
    "Marital_status": marital_status,
    "Application_mode": application_mode,
    "Course": course,
    "Previous_qualification": prev_qualification,
    "Previous_qualification_grade": prev_qualification_grade,
    "Mothers_qualification": mother_qual,
    "Fathers_qualification": father_qual,
    "Mothers_occupation": mother_job,
    "Fathers_occupation": father_job,
    "Admission_grade": admission_grade,
    "Debtor": debtor,
    "Tuition_fees_up_to_date": tuition_up_to_date,
    "Gender": gender,
    "Scholarship_holder": scholarship,
    "Age_at_enrollment": age_at_enroll,
    "Curricular_units_1st_sem_enrolled": sem1_enrolled,
    "Curricular_units_1st_sem_evaluations": sem1_eval,
    "Curricular_units_1st_sem_approved": sem1_approved,
    "Curricular_units_1st_sem_grade": sem1_grade,
    "Curricular_units_2nd_sem_enrolled": sem2_enrolled,
    "Curricular_units_2nd_sem_evaluations": sem2_eval,
    "Curricular_units_2nd_sem_approved": sem2_approved,
    "Curricular_units_2nd_sem_grade": sem2_grade
}

# buat DataFrame baru dari dictionary
data2 = pd.DataFrame([input_data])

with st.expander("View the Raw Data"):
    st.dataframe(data=data2, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data2)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Prediction Result: {}".format(prediction(new_data)))