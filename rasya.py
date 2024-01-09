import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_velocity(amplitudo, frekuensi, densitas, modulus):
    try:
        kecepatan = np.sqrt(modulus / densitas) 
        x = np.linspace(0 , modulus2 , 500)
        y = amplitudo * np.sin(2 * np.pi * frekuensi * x) * np.cos(2 * np.pi * kecepatan * x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Grafik Gelombang Longitudinal")
        ax.set_xlabel("Posisi (m)")
        ax.set_ylabel("Amplitudo (V)")
        st.pyplot(fig)
    except ValueError:
        st.write("Masukkan angka untuk semua input")

st.title("KALKULATOR GELOMBANG LONGITUDINAL")
st.write("by: Muhammad Rasya Alvareza NRP: 11-2021-021")
st.write("Dosen: Ir. Rustamaji, M.T")
st.write("Gelombang Longitudinal adalah gelombang dengan perpindahan media berada dalam arah yang sama atau berlawan dengan arah propagasi gelombang")
st.write("Densitas adalah suatu parameter fisik yang menunjukkan jumlah partikel dalam satu kubik meter suatu medium")
st.write("Modulus elastisitas, juga dikenal sebagai modulus Young, adalah ukuran kuantitatif yang menunjukkan tingkat ketahanan suatu bahan terhadap deformasi, khususnya regangan linier")
amplitudo = st.number_input('Amplitudo (A):')
frekuensi = st.number_input('Frekuensi (Hz):')
densitas = st.number_input('Densitas (kg/m^3):')
modulus = st.number_input('Modulus Elastisitas (Nm-2):')
modulus2 = st.number_input('Posisi (m):')

if st.button('Buat Grafik Gelombang'):
    calculate_velocity(amplitudo, frekuensi, densitas, modulus)