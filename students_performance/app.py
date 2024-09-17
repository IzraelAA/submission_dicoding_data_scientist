import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model/random_forest_model.joblib')

# Pastikan model adalah RandomForestClassifier atau classifier lainnya
assert hasattr(model, 'predict'), "Model yang dimuat tidak memiliki method 'predict'"

# Fungsi untuk input dari user
def user_input_features():
    age_at_enrollment = st.sidebar.slider('Usia Saat Pendaftaran', 17, 60, 25)
    scholarship_holder = st.sidebar.selectbox('Penerima Beasiswa?', ['Ya', 'Tidak'])
    curricular_units_1st_sem_approved = st.sidebar.slider('Jumlah Unit Mata Kuliah Semester 1 (Disetujui)', 0, 10, 5)
    curricular_units_1st_sem_credited = st.sidebar.slider('Jumlah Unit Mata Kuliah Semester 1 (Dikreditkan)', 0, 10, 5)
    curricular_units_1st_sem_enrolled = st.sidebar.slider('Jumlah Unit Mata Kuliah Semester 1 (Terdaftar)', 0, 10, 5) 
    previous_qualification_grade = st.sidebar.slider('Nilai Kualifikasi Sebelumnya', 0, 100, 50)
    tuition_fees_up_to_date = st.sidebar.selectbox('Biaya Pendidikan Terupdate?', ['Ya', 'Tidak']) 
    gender = st.sidebar.selectbox('Jenis Kelamin', ['Pria', 'Wanita'])

    # Mengonversi pilihan ke format yang sesuai dengan model
    scholarship_encoded = 1 if scholarship_holder == 'Ya' else 0
    tuition_fees_encoded = 1 if tuition_fees_up_to_date == 'Ya' else 0
    gender_encoded = 1 if gender == 'Wanita' else 0

    # Membuat DataFrame dengan fitur yang relevan
    data = {
        'Age_at_enrollment': age_at_enrollment,
        'Scholarship_holder': scholarship_encoded,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled, 
        'Previous_qualification_grade': previous_qualification_grade,
        'Tuition_fees_up_to_date': tuition_fees_encoded, 
        'Gender': gender_encoded
    }
    
    return pd.DataFrame(data, index=[0])

# Mendapatkan input dari pengguna
input_data = user_input_features()

# Melakukan prediksi jika tombol ditekan
if st.button('Prediksi Risiko Dropout'):
    try:
        # Melakukan prediksi
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)

        # Menampilkan hasil prediksi
        if prediction[0] == 1:
            st.error(f"Siswa ini berisiko dropout. Probabilitas dropout: {prediction_proba[0][1]:.2f}")
        else:
            st.success(f"Siswa ini diprediksi lulus. Probabilitas kelulusan: {prediction_proba[0][0]:.2f}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
