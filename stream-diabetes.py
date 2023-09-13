import pickle
import streamlit as st

from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="main menu",
    options=["Home","Diagnosa","info diabetes"],
    icons=["house", "book", "newspaper"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    st.title(f"Selamat Datang Di web prediksi diabetes ")
    st.write('Web ini Dibuat oleh Basyach Aryodito T.H bertujuan untuk memberikan prediksi tentang kemungkinan seseorang menderita diabetes. '
              'Dengan menggunakan data dan model yang telah dilatih sebelumnya, web ini dibuat guna menyelesaikan tugas skripsi  '
            )
if selected == "Diagnosa" :
    
# membaca model
        diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

        st.title('Prediksi Diabetes')

        #membagi kolom
        col1, col2 =st.columns(2)

        with col1 :
           Pregnancies = st.text_input ('input nilai Pregnancies')
        with col2 :
            Glucose = st.text_input ('input nilai Glucose')
        with col1 :
            BloodPressure = st.text_input ('input nilai BloodPressure')
        with col2 :
            SkinThickness = st.text_input ('input nilai SkinThickness')
        with col1 :
            Insulin = st.text_input ('input nilai Insulin')
        with col2 :
            BMI = st.text_input ('input nilai BMI')
        with col1 :
            DiabetesPedigreeFunction = st.text_input ('input nilai DiabetesPedigreeFunction')
        with col2 :
            Age = st.text_input ('input nilai Age')
# code prediksi
        diab_diagnosis = ''
        diab_prediction = ''

#membuat tombol untuk prediksi
        
        if st.button('Test prediksi Diabetes') :
            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
            if(diab_prediction[0] == 1):
                diab_diagnosis = 'pasien Positif Diabetes'
            else :
                diab_diagnosis = 'pasien Negatif Diabetes'
            st.success(diab_diagnosis)       

if selected == "info diabetes":
    st.title('Info Diabetes')
    st.write('Diabetes adalah kondisi medis yang ditandai dengan tingginya kadar glukosa (gula) dalam darah. '
              'Ini terjadi ketika tubuh tidak dapat memproduksi atau menggunakan hormon insulin dengan efektif. '
              'Diabetes dapat memiliki dampak serius pada kesehatan dan membutuhkan perawatan dan manajemen yang tepat.')

    st.markdown('## Gejala Diabetes')
    st.write('- Rasa haus yang berlebihan')
    st.write('- Sering buang air kecil')
    st.write('- Penurunan berat badan yang tidak dapat dijelaskan')
    st.write('- Kelelahan dan kelemahan')
    st.write('- Infeksi berulang')
    st.write('- Luka yang sulit sembuh')

    st.markdown('## Faktor Risiko')
    st.write('Beberapa faktor yang dapat meningkatkan risiko terkena diabetes meliputi:')
    st.write('- Riwayat keluarga diabetes')
    st.write('- Kegemukan atau obesitas')
    st.write('- Gaya hidup tidak sehat, seperti pola makan tidak sehat dan kurangnya aktivitas fisik')
    st.write('- Usia lebih dari 45 tahun')
    st.write('- Tekanan darah tinggi')
    st.write('- Kolesterol tinggi')
