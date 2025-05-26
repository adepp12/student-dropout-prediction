import joblib
import pandas as pd

model = joblib.load("model/gboost_model.joblib")
result_label = joblib.load("model/label_encoder.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): A dataframe containing all pre-processed data
 
    Returns:
        str: Prediction result (Dropout, Enrolled, or Graduate)
    """
    result = model.predict(data)
    final_result = result_label.inverse_transform(result)[0]
    return final_result

# testing
# test_data_values = [[
#     1, 1, 9500, 1, 147.0, 38, 19, 5, 8, 147.3,
#     0, 1, 0, 0, 18, 7, 7, 6, 13.966666666666669, 7,
#     7, 6, 13.966666666666669
# ]]

# # List of column names in order
# columns = [
#     "Marital_status", "Application_mode", "Course", "Previous_qualification", "Previous_qualification_grade",
#     "Mothers_qualification", "Fathers_qualification", "Mothers_occupation", "Fathers_occupation",
#     "Admission_grade", "Debtor", "Tuition_fees_up_to_date", "Gender", "Scholarship_holder",
#     "Age_at_enrollment", "Curricular_units_1st_sem_enrolled", "Curricular_units_1st_sem_evaluations",
#     "Curricular_units_1st_sem_approved", "Curricular_units_1st_sem_grade",
#     "Curricular_units_2nd_sem_enrolled", "Curricular_units_2nd_sem_evaluations",
#     "Curricular_units_2nd_sem_approved", "Curricular_units_2nd_sem_grade"
# ]

# test_df = pd.DataFrame(test_data_values, columns=columns)

# try:
#     test_result = prediction(test_df)
#     print("Prediction result:", test_result)
# except Exception as e:
#     print("Error:", e)