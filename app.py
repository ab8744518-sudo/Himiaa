import streamlit as st
import time

# Тақырып және стиль
st.set_page_config(page_title="Этнохимиялық виртуалды зертхана", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #f0f2f6; }
    .stProgress > div > div > div > div { background-color: #4CAF50; }
    .eb-container { border: 2px solid #e6e9ef; padding: 20px; border-radius: 15px; background-color: #fdfdfd; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 Табиғи майлардан сабын алу")
st.caption("Зертханалық жұмыс №2 [cite: 1, 2]")

# Прогресс бары
if 'step' not in st.session_state:
    st.session_state.step = 1

progress_bar = st.progress((st.session_state.step - 1) / 4)

# ---------------------------------------------------------
# 1-КЕЗЕҢ: СІЛТІ
# ---------------------------------------------------------
if st.session_state.step == 1:
    st.header("1-кезең: Сілті ерітіндісін дайындау [cite: 10]")
    st.markdown("""
    <div style="text-align: center; font-size: 70px;"> ⚗️ 💧 </div>
    """, unsafe_allow_html=True)
    st.write("10 г натрий гидроксидін (NaOH) 20 мл тазартылған суда мұқият ерітіңіз[cite: 11].")
    
    if st.button("Сілтіні суға қосу"):
        with st.status("Ерітінді дайындалуда..."):
            time.sleep(1.5)
            st.write("🔥 Реакция жылынады, бұл экзотермиялық реакция[cite: 11].")
            time.sleep(1)
        st.success("Ерітінді дайын!")
        
        st.divider()
        st.subheader("❓ Бақылау сұрағы:")
        ans1 = st.radio("Сілтіні суға қосқанда неге жылу бөлінеді?", 
                        ["Бұл эндотермиялық реакция", "Бұл экзотермиялық реакция [cite: 11]", "Сілті суып жатыр"])
        
        if st.button("Келесі кезеңге өту"):
            if "экзотермиялық" in ans1:
                st.session_state.step = 2
                st.rerun()
            else:
                st.error("Қате жауап! Қайта ойланып көріңіз.")

# ---------------------------------------------------------
# 2-КЕЗЕҢ: ГИДРОЛИЗ
# ---------------------------------------------------------
elif st.session_state.step == 2:
    st.header("2-кезең: Гидролиз реакциялары [cite: 12]")
    st.markdown("""
    <div style="text-align: center; font-size: 70px;"> 🧴 + 🧪 </div>
    """, unsafe_allow_html=True)
    st.write("Шыны стаканға 30 мл өсімдік майын және 10 мл спирт құйыңыз[cite: 13].")
    
    if st.button("Компоненттерді араластыру"):
        st.balloons()
        st.info("Сілті ерітіндісін ақырындап құйып, шыны таяқшамен үздіксіз араластырыңыз[cite: 14].")
        
        st.divider()
        st.subheader("❓ Бақылау сұрағы:")
        ans2 = st.radio("Неге сабын алу үшін спирт қолданамыз? [cite: 23]", 
                        ["Май мен сілті араласуы үшін ортақ еріткіш [cite: 24]", "Сабынға иіс беру үшін", "Майды қатыру үшін"])
        
        if st.button("Келесі кезеңге өту"):
            if "ортақ еріткіш" in ans2:
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("Жауап дұрыс емес!")

# ---------------------------------------------------------
# 3-КЕЗЕҢ: ҚЫЗДЫРУ
# ---------------------------------------------------------
elif st.session_state.step == 3:
    st.header("3-кезең: Су моншасында қыздыру [cite: 15]")
    st.markdown("""
    <div style="text-align: center; font-size: 70px;"> ♨️ 🌡️ </div>
    """, unsafe_allow_html=True)
    st.warning("⚠️ Қауіпсіздік: Көзілдірік киіп алыңыз! ")
    
    temp = st.slider("Температураны көтеріңіз (°C)", 0, 100, 0)
    if temp >= 80:
        st.write("✨ Ерітінді су моншасында 30-40 минут баяу қайнауда... ")
        
        st.divider()
        st.subheader("❓ Бақылау сұрағы:")
        ans3 = st.radio("Сабындану реакциясы дегеніміз не? [cite: 21]", 
                        ["Майдың еруі", "Майдың сілтімен әрекеттесіп, сабын мен глицеринге ыдырауы [cite: 22]", "Майдың сумен қосылуы"])
        
        if st.button("Келесі кезеңге өту"):
            if "сабын мен глицерин" in ans3:
                st.session_state.step = 4
                st.rerun()
            else:
                st.error("Қате!")

# ---------------------------------------------------------
# 4-КЕЗЕҢ: ТҰЗДАУ
# ---------------------------------------------------------
elif st.session_state.step == 4:
    st.header("4-кезең: Сабынды тұндыру (Тұздау) [cite: 17]")
    st.markdown("""
    <div style="text-align: center; font-size: 70px;"> 🧂 🧼 </div>
    """, unsafe_allow_html=True)
    st.write("Қоспаға ас тұзының (NaCl) қаныққан ерітіндісін қосыңыз[cite: 18].")
    
    if st.button("Тұзды қосу"):
        st.toast("Сабын бетке қалқып шығуда...")
        time.sleep(1)
        st.success("Сабын сұйықтықтың бетіне қалқып шықты! [cite: 18]")
        
        st.divider()
        st.subheader("❓ Соңғы сұрақ:")
        ans4 = st.radio("Неге тұз (NaCl) қосқанда сабын бөлініп шығады? [cite: 25]", 
                        ["Сабын еріп кетеді", "Тұздау әсері: судағы ерігіштігі төмендегендіктен [cite: 26]", "Тұз майды ыдыратады"])
        
        if st.button("Тәжірибені аяқтау"):
            if "Тұздау әсері" in ans4:
                st.balloons()
                st.header("🎉 Құттықтаймыз! Сабын алынды.")
                if st.button("Басынан бастау"):
                    st.session_state.step = 1
                    st.rerun()
            else:
                st.error("Дұрыс жауапты таңдаңыз!")
