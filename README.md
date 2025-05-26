## Student Dropout Prediction Application

### About this Project
This project is a final project as a graduation requirement from the [Data Science - Dicoding Indonesia class](https://www.dicoding.com/academies/590-belajar-penerapan-data-science) (May 2025). The main focus of this project is to build a prediction model to determine student status (Dropout, Enrolled, or Graduate) based on available data. The machine learning model was developed using the Gradient Boosting algorithm and achieved 75% accuracy on the training data. 

Dataset used: [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv) 

Running the app
* Activate virtual env
    ```
    # Windows command prompt
    .venv\Scripts\activate.bat

    # Windows PowerShell
    .venv\Scripts\Activate.ps1

    # macOS and Linux
    source .venv/bin/activate
    ````
* Install dependencies
     ```
    pip install -r requirements.txt
    ```
* Run the prediction application
    ```
    streamlit run app.py
    ```
* Ctrl+C to stop the Streamlit server
* Deactivate virtual env
    ```
    deactive
    ```

### Acknowledgement
I would like to thank [IDCamp (Indosat Ooredoo Hutchison Digital Camp)](https://idcamp.ioh.co.id/) for the digital training scholarship opportunity organized through [Dicoding Indonesia](https://www.dicoding.com/). This training is very useful in improving my competence in the field of Data Science and allows the preparation of this final project as a form of implementation of the learning that has been obtained.