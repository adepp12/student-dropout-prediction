import pandas as pd

# dictionary categorical column
marital_status_map = {
    'Single': 1,
    'Married': 2,
    'Widower': 3,
    'Divorced': 4,
    'Facto union': 5,
    'Legally separated': 6
}

application_mode_map = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

course_map = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

previous_qualification_map = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle": 19,
    "Basic education 2nd cycle": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

parent_qualification_map = {
    "Secondary Education - 12th Year of Schooling or Equivalent": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "10th Year of Schooling": 14,
    "General Commerce Course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent": 19,
    "Technical-Professional Course": 22,
    "7th Year of Schooling": 26,
    "2nd Cycle of the General High School Course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th Year of Schooling": 30,
    "Unknown": 34,
    "Can't Read or Write": 35,
    "Can Read Without Having a 4th Year of Schooling": 36,
    "Basic Education 1st Cycle (4th/5th Year) or Equivalent": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent": 38,
    "Technological Specialization Course": 39,
    "Higher Education - Degree (1st Cycle)": 40,
    "Specialized Higher Studies Course": 41,
    "Professional Higher Technical Course": 42,
    "Higher Education - Master (2nd Cycle)": 43,
    "Higher Education - Doctorate (3rd Cycle)": 44
}

parents_occupation_map = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative Staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Armed Forces Officers": 101,
    "Armed Forces Sergeants": 102,
    "Other Armed Forces Personnel": 103,
    "Directors of Administrative and Commercial Services": 112,
    "Hotel, Catering, Trade and Other Services Directors": 114,
    "Specialists in the Physical Sciences, Mathematics, Engineering and Related Techniques": 121,
    "Health Professionals": 122,
    "Teachers": 123,
    "Specialists in Finance, Accounting, Administrative Organization, Public and Commercial Relations": 124,
    "Intermediate Level Science and Engineering Technicians and Professions": 131,
    "Technicians and Professionals, of Intermediate Level of Health": 132,
    "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services": 134,
    "Information and Communication Technology Technicians": 135,
    "Office Workers, Secretaries in General and Data Processing Operators": 141,
    "Data, Accounting, Statistical, Financial Services and Registry-Related Operators": 143,
    "Other Administrative Support Staff": 144,
    "Personal Service Workers": 151,
    "Sellers": 152,
    "Personal Care Workers and the Like": 153,
    "Protection and Security Services Personnel": 154,
    "Market-Oriented Farmers and Skilled Agricultural and Animal Production Workers": 161,
    "Farmers, Livestock Keepers, Fishermen, Hunters and Gatherers, Subsistence": 163,
    "Skilled Construction Workers and the Like, Except Electricians": 171,
    "Skilled Workers in Metallurgy, Metalworking and Similar": 172,
    "Skilled Workers in Electricity and Electronics": 174,
    "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts": 175,
    "Fixed Plant and Machine Operators": 181,
    "Assembly Workers": 182,
    "Vehicle Drivers and Mobile Equipment Operators": 183,
    "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry": 192,
    "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport": 193,
    "Meal Preparation Assistants": 194,
    "Street Vendors (Except Food) and Street Service Providers": 195
}

# binary column
binary_map = {"Yes": 1,"No": 0}
gender_map = {"Male": 1,"Female": 0}

# bnary mapping
binary_cols = ['Debtor', 'Tuition_fees_up_to_date',
               'Scholarship_holder']


def data_preprocessing(data):
    """
    Function for preprocessing input data from users.
    Mapping categorical to numerical values using the dictionary that has been defined..
    """
    data = data.copy()
    df = pd.DataFrame()

    # mapping kolom kategorikal
    df['Marital_status'] = data['Marital_status'].map(marital_status_map).fillna(-1)
    df['Application_mode'] = data['Application_mode'].map(application_mode_map).fillna(-1)
    df['Course'] = data['Course'].map(course_map).fillna(-1)
    df['Previous_qualification'] = data['Previous_qualification'].map(previous_qualification_map).fillna(-1)
    df['Previous_qualification_grade'] = data['Previous_qualification_grade']
    df['Mothers_qualification'] = data['Mothers_qualification'].map(parent_qualification_map).fillna(-1)
    df['Fathers_qualification'] = data['Fathers_qualification'].map(parent_qualification_map).fillna(-1)
    df['Mothers_occupation'] = data['Mothers_occupation'].map(parents_occupation_map).fillna(-1)
    df['Fathers_occupation'] = data['Fathers_occupation'].map(parents_occupation_map).fillna(-1)
    df['Admission_grade'] = data['Admission_grade']
    df['Gender'] = data['Gender'].map(gender_map).fillna(-1)
    df['Age_at_enrollment'] = data['Age_at_enrollment']
    df['Curricular_units_1st_sem_enrolled'] = data['Curricular_units_1st_sem_enrolled']
    df['Curricular_units_1st_sem_evaluations'] = data['Curricular_units_1st_sem_evaluations']
    df['Curricular_units_1st_sem_approved'] = data['Curricular_units_1st_sem_approved']
    df['Curricular_units_1st_sem_grade'] = data['Curricular_units_1st_sem_grade']
    df['Curricular_units_2nd_sem_enrolled'] = data['Curricular_units_2nd_sem_enrolled']
    df['Curricular_units_2nd_sem_evaluations'] = data['Curricular_units_2nd_sem_evaluations']
    df['Curricular_units_2nd_sem_approved'] = data['Curricular_units_2nd_sem_approved']
    df['Curricular_units_2nd_sem_grade'] = data['Curricular_units_2nd_sem_grade']

    # binary mapping
    for col in binary_cols:
        df[col] = data[col].map(binary_map).fillna(-1)

    column_order = [
        "Marital_status",
        "Application_mode",
        "Course",
        "Previous_qualification",
        "Previous_qualification_grade",
        "Mothers_qualification",
        "Fathers_qualification",
        "Mothers_occupation",
        "Fathers_occupation",
        "Admission_grade",
        "Debtor",
        "Tuition_fees_up_to_date",
        "Gender",
        "Scholarship_holder",
        "Age_at_enrollment",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_evaluations",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_evaluations",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade"
    ]
    
    df = df.reindex(columns=column_order)
    
    return df

#testing
# test_data_values = [[
#     'Single','1st phase - general contingent','Social Service','Secondary education',137.0,'Higher Education - Degree','Secondary Education - 12th Year of Schooling or Equivalent',
#     'Unskilled Workers','Unskilled Workers',129.3,'No','Yes','Female','Yes',21,6,8,6,13.875,6,7,6,14.142857142857142
# ]]

# # list of column names in order
# columns = [
#      "Marital_status", "Application_mode", "Course", "Previous_qualification", "Previous_qualification_grade",
#      "Mothers_qualification", "Fathers_qualification", "Mothers_occupation", "Fathers_occupation",
#      "Admission_grade", "Debtor", "Tuition_fees_up_to_date", "Gender", "Scholarship_holder",
#      "Age_at_enrollment", "Curricular_units_1st_sem_enrolled", "Curricular_units_1st_sem_evaluations",
#      "Curricular_units_1st_sem_approved", "Curricular_units_1st_sem_grade",
#      "Curricular_units_2nd_sem_enrolled", "Curricular_units_2nd_sem_evaluations",
#      "Curricular_units_2nd_sem_approved", "Curricular_units_2nd_sem_grade"
#  ]

# test_df = pd.DataFrame(test_data_values, columns=columns)

# try:
#     mapping_result = data_preprocessing(test_df)
#     print("Processing result:", mapping_result.T)
# except Exception as e:
#      print("Error:", e)