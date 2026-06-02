import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="🏆"
)

with st.sidebar:
    st.image(r"C:\Users\advan\Downloads\pjbl.jpeg", width=80)

    st.title("Bangun Datar")

    pilihan = st.selectbox(
        "Pilih bangun datar",
        [
            "Persegi",
            "Persegi Panjang",
            "Lingkaran",
            "Segitiga",
            "Jajar Genjang"
        ]
    )

    st.caption("Dibuat oleh Zivana Oktaviani👀💕")

match pilihan:

    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")

        sisi = st.number_input("Masukkan sisi")

        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi

            st.success(
                f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.snow()
            st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")

        panjang = st.number_input("Masukkan panjang")
        lebar = st.number_input("Masukkan lebar")

        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)

            st.success(
                f"Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")

        jari_jari = st.number_input("Masukkan jari-jari")

        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari

            st.success(
                f"Luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` segitiga")

        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi

            st.success(
                f"Luas segitiga adalah {luas:.2f}"
            )

            st.balloons()

    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `luas` dan `keliling` jajar genjang")

        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisi_miring = st.number_input("Masukkan sisi miring")

        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi_miring)

            st.success(
                f"Luas jajar genjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()