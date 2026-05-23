import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Katalog Anggrek", layout="wide")

if os.path.exists("PENSILALL.JPG"):
    st.image("PENSILALL.JPG", use_container_width=True)

st.title("penyedia aneka pensil faber castell")
st.divider()

try:
    if os.path.exists("data_anggrek1.csv"):
        df = pd.read_csv("data_anggrek1.csv", sep=';')
        df['harga'] = df['harga'].astype(str).str.replace('Rp', '').str.replace('.', '').str.strip().astype(int)
        df = df.dropna(subset=['foto'])

        daftar_kategori = df['kategori'].unique()

        for kat in daftar_kategori:
            st.header(f"pensil jenis {kat.capitalize()}")
            data_per_kat = df[df['kategori'] == kat]
            cols = st.columns(4)

            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row['foto']).strip()
                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
                    st.subheader(row['nama'])
                    st.markdown(f"### **Rp {int(row['harga']):,}**")
                    st.markdown(f"**Status:** {row['status']}")
            st.divider()
    else:
        st.error("File 'data_anggrek1.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

st.write("")
st.write("")
st.divider()
st.subheader("Hubungi Kami")

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
**Alamat Galeri:** Jl.Gatot Subroto No.1 Senayan kecamatan Tanah Abang Jakarta Pusat 10270
DKI Jakarta, Indonesia
""")

with col_info2:
    no_hp = "6281380455784"
    pesan_wa = "Halo, saya tertarik memesan pensil faber castell di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"
    st.markdown("**WhatsApp:**")
    st.link_button("Pesan Sekarang via WhatsApp", link_wa)

st.caption("© 2026 Toko Pensil - Semua Hak Dilindungi")
