import streamlit as st

# Беттің баптаулары
st.set_page_config(page_title="Виртуалды зертхана", layout="centered")

# CSS арқылы колба анимациясын жасау
def flask_animation(color, bubbles=False):
    bubble_html = ""
    if bubbles:
        bubble_html = '<div class="bubbles"></div>'
    
    html_code = f"""
    <style>
    .flask-container {{
        display: flex; justify-content: center; align-items: center; height: 200px;
    }}
    .flask {{
        position: relative; width: 100px; height: 120px;
        background: rgba(255, 255, 255, 0.1);
        border: 4px solid #333; border-radius: 0 0 50px 50px;
        overflow: hidden;
    }}
    .flask::before {{
        content: ""; position: absolute; top: -50px; left: 50%;
        transform: translateX(-50%); width: 40px; height: 60px;
        border: 4px solid #333; border-bottom: none;
    }}
    .liquid {{
        position: absolute; bottom: 0; left: 0; width: 100%; height: 60%;
        background: {color}; transition: all 1s ease;
    }}
    .bubbles {{
        position: absolute; bottom: 10px; left: 10%; width: 80%; height: 100%;
        background-image: radial-gradient(circle, white 20%, transparent 20%);
        background-size: 15px 15px; animation: move 2s linear infinite;
    }}
    @keyframes move {{
        0% {{ transform: translateY(0); }}
        100% {{ transform: translateY(-50px); opacity: 0; }}
    }}
    </style>
    <div class="flask-container">
        <div class="flask">
            <div class="liquid"></div>
            {bubble_html}
        </div>
    </div>
    """
    st.components.v1.html(html_code, height=220)

# Тақырыбы [cite: 2]
st.title("🧼 Табиғи майлардан сабын алу")

if 'step' not in st.session_state:
    st.session_state.step = 1

# Жұмыс барысы 4 кезеңге бөлінген [cite: 9]
# 1-КЕЗЕҢ
if st.session_state.step == 1:
    st.header("1-кезең: Сілті ерітіндісін дайындау")
    st.write("10 г NaOH-ты 20 мл суда ерітіңіз[cite: 11].")
    flask_animation("#E0E0E0") # Мөлдір сұйықтық
    
    st.divider()
    q1 = st.radio("Сұрақ: Сілтіні суда еріткенде не байқалады? [cite: 11]", 
                  ["Ерітінді суып кетеді", "Ерітінді жылынады (экзотермиялық)", "Ешқандай өзгеріс болмайды"])
    
    if st.button("Келесі кезең"):
        if "жылынады" in q1:
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Қате жауап!")

# 2-КЕЗЕҢ
elif st.session_state.step == 2:
    st.header("2-кезең: Гидролиз реакциялары")
    st.write("Майға 10 мл спирт және сілті ерітіндісін қосыңыз[cite: 13, 14].")
    flask_animation("#FFD700") # Май түсі (алтын)
    
    st.divider()
    q2 = st.radio("Сұрақ: Неге сабын алу үшін спирт қолданамыз? [cite: 23]", 
                  ["Иіс беру үшін", "Ортақ еріткіш ретінде реакцияны жылдамдату үшін [cite: 24]", "Сабынды қатыру үшін"])
    
    if st.button("Келесі кезең"):
        if "жылдамдату" in q2:
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("Қате!")

# 3-КЕЗЕҢ
elif st.session_state.step == 3:
    st.header("3-кезең: Су моншасында қыздыру")
    st.write("30-40 минут баяу қайнатыңыз[cite: 16].")
    flask_animation("#F4A460", bubbles=True) # Қайнап жатқан қоспа
    
    st.divider()
    q3 = st.radio("Сұрақ: Сабындану реакциясы дегеніміз не? [cite: 21]", 
                  ["Майдың жануы", "Майдың сілтімен әрекеттесіп, сабын мен глицеринге ыдырауы [cite: 22]", "Майдың булануы"])
    
    if st.button("Келесі кезең"):
        if "сабын мен глицерин" in q3:
            st.session_state.step = 4
            st.rerun()
        else:
            st.error("Дұрыс емес!")

# 4-КЕЗЕҢ
elif st.session_state.step == 4:
    st.header("4-кезең: Сабынды тұндыру (Тұздау)")
    st.write("Қоспаға ас тұзының (NaCl) қаныққан ерітіндісін қосыңыз[cite: 18].")
    flask_animation("#FFFFFF", bubbles=False) # Сабынның бөлінуі (ақ түс)
    
    st.divider()
    q4 = st.radio("Сұрақ: Неге тұз (NaCl) қосқанда сабын бөлініп шығады? [cite: 25]", 
                  ["Сабын еріп кетеді", "Тұздау әсерінен сабын бетке қалқып шығады [cite: 26]", "Тұз майды бұзады"])
    
    if st.button("Аяқтау"):
        if "Тұздау әсерінен" in q4:
            st.balloons()
            st.success("Тәжірибе сәтті аяқталды! Сен сабын алдың! 🧼")
            if st.button("Басынан бастау"):
                st.session_state.step = 1
                st.rerun()
