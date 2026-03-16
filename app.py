import streamlit as st

st.title("🧪 Этнохимиялық виртуалды зертхана")
st.header("№2 зертханалық жұмыс: Сабын алу")

# Интерактивті сұрақтар
st.subheader("Зерттеу сұрақтары")
q1 = st.checkbox("Неге сабын алу үшін спирт қолданамыз?")
if q1:
    st.info("Май мен сілті бір-бірінде ерімейді, ал спирт ортақ еріткіш ретінде реакцияны жылдамдатады.") # [cite: 24]

# Тәжірибе жасау бөлімі
st.subheader("Виртуалды реактор")
oil_volume = st.slider("Май мөлшері (мл):", 0, 50, 30) # [cite: 13]
alkali_type = st.selectbox("Сілті түрі:", ["NaOH (Натрий гидроксиді)", "KOH (Калий гидроксиді)"]) # 

if st.button("Реакцияны бастау"):
    st.write(f"{oil_volume} мл май мен {alkali_type} қосылды...")
    st.video("https://www.example.com/saponification_video.mp4") # Мысал ретінде
    st.success("Құттықтаймыз! Сіз сабын алдыңыз.")
