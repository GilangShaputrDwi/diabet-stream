import pickle
import pandas as pd
import streamlit as st

# Memuat model

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul Website

st.markdown("""
## Prediksi Penyakit Stroke

Oleh : Muhammad Gilang Dwi Saputra 21.11.4233
""")

# Menambahkan gambar

st.image('diabet.jpg')

st.markdown("""
    ## Tentang Kegunaan Aplikasi Prediksi Penyakit Diabetes 

    Aplikasi prediksi penyakit diabetes ini bertujuan untuk membantu dalam mendeteksi risiko diabetes pada pasien berdasarkan beberapa parameter medis. Dengan menggunakan algoritma pembelajaran mesin yang telah dilatih dengan dataset medis, aplikasi ini dapat memberikan hasil prediksi apakah seorang pasien kemungkinan besar menderita diabetes atau tidak.
    """)

# Dropdown menu for additional information

st.markdown("**<h3 style='text-align: center;'>PILIH INFORMASI TAMBAHAN</h3>**",
            unsafe_allow_html=True)
option = st.selectbox('', ('Pilih Kategori', 'Tabel',
                      'Cara Kerja Aplikasi', 'Manfaat Aplikasi'))

if option == 'Tabel':
    st.markdown("## Parameter yang Digunakan untuk Prediksi")
    data = {
        "Parameter": [
            "Jumlah Kehamilan (Pregnancies)",
            "Glukosa (Glucose)",
            "Tekanan Darah (BloodPressure)",
            "Ketebalan Kulit (SkinThickness)",
            "Insulin",
            "Indeks Massa Tubuh (BMI)",
            "Fungsi Riwayat Keluarga Diabetes (DiabetesPedigreeFunction)",
            "Usia (Age)"
        ],
        "Deskripsi": [
            "Jumlah kehamilan yang dialami oleh pasien.",
            "Tingkat glukosa dalam darah setelah berpuasa.",
            "Tekanan darah diastolik (mm Hg).",
            "Ketebalan lipatan kulit triseps (mm).",
            "Tingkat insulin serum dua jam (mu U/ml).",
            "Indeks massa tubuh (berat badan dalam kg/(tinggi badan dalam meter)^2).",
            "Fungsi yang menunjukkan riwayat keluarga diabetes.",
            "Usia pasien."
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)

elif option == 'Cara Kerja Aplikasi':
    st.markdown("""
    ## Cara Kerja Aplikasi

    1. **Input Data Pasien** : Pengguna memasukkan nilai parameter-parameter medis yang diperlukan ke dalam aplikasi.
    2. **Prediksi** : Aplikasi menggunakan model pembelajaran mesin untuk memprediksi risiko diabetes berdasarkan data yang dimasukkan.
    3. **Hasil Prediksi** : Aplikasi menampilkan hasil prediksi apakah pasien kemungkinan besar menderita diabetes atau tidak.
    """)

elif option == 'Manfaat Aplikasi':
    st.markdown("""
    ## Manfaat Aplikasi

    1. **Deteksi Dini** : Membantu dalam mendeteksi risiko diabetes sejak dini, sehingga langkah-langkah pencegahan dapat diambil lebih awal.
    2. **Pengambilan Keputusan** : Membantu tenaga medis dalam pengambilan keputusan yang lebih baik terkait diagnosis dan perawatan pasien.
    3. **Kesadaran Kesehatan** : Meningkatkan kesadaran pasien terhadap faktor risiko diabetes dan pentingnya menjaga gaya hidup sehat.
    """)

# Membagi Kolom

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input(
        'Silakan Isi Dengan Jumlah Kehamilan Anda Sebelumnya')

with col2:
    Glucose = st.text_input('Masukan Nilai Glukosa Anda')

with col1:
    BloodPressure = st.text_input('Masukan Tekanan Darah Anda')

with col2:
    SkinThickness = st.text_input(
        'Masukan Ketebalan Lipatan Kulit Trisep (mm)')

with col1:
    Insulin = st.text_input('Masukan Insulin Anda')

with col2:
    BMI = st.text_input('Masukan Indeks Masa Tubuh Anda')

with col1:
    DiabetesPedigreeFunction = st.text_input('Masukan DPF Anda')

with col2:
    Age = st.text_input('Masukan Usia Anda')


# Code Untuk Prediksi

diab_diag = ''

# Tombol Prediksi

if st.button('Prediksi Diabetes'):
    diab_predictions = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age]]
    )

    if diab_predictions[0] == 1:
        diab_diag = 'Pasien Terkena Diabetes'
    else:
        diab_diag = 'Pasien Tidak Terkena Diabetes'

    st.success(diab_diag)
