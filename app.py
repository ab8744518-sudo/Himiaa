import streamlit as st

st.set_page_config(layout="wide")
st.title("🧼 Виртуалды зертхана: Сабын алу")

# Кезеңдерді басқару
if 'step' not in st.session_state:
    st.session_state.step = 1

# CSS Анимация стилі
st.markdown("""
<style>
    .stage-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        position: relative;
        overflow: hidden;
        background: #f0f2f6;
        border-radius: 15px;
    }
    .main-flask {
        width: 100px; height: 120px;
        border: 4px solid #333; border-radius: 0 0 50px 50px;
        position: relative; background: rgba(255,255,255,0.5);
        z-index: 2;
    }
    .liquid {
        position: absolute; bottom: 0; width: 100%; height: 0%;
        transition: height 2s, background 1s;
    }
    .side-flask {
        position: absolute; width: 60px; height: 80px;
        border: 3px solid #333; border-radius: 10px;
        opacity: 0;
    }
    /* Анимация эффектілері */
    @keyframes pour-left {
        0% { left: -100px; opacity: 0; transform: rotate(0deg); }
        50% { left: 30%; opacity: 1; transform: rotate(45deg); }
        100% { left: 30%; opacity: 0; transform: rotate(45deg); }
    }
    @keyframes pour-right {
        0% { right: -100px; opacity: 0; transform: rotate(0deg); }
        50% { right: 30%; opacity: 1; transform: rotate(-45deg); }
        100% { right: 30%; opacity: 0; transform: rotate(-45deg); }
    }
    .animate-left { animation: pour-left 3s forwards; }
    .animate-right { animation: pour-right 3s forwards; }
</style>
""", unsafe_allow_html=True)

def render_lab(liquid_height, liquid_color, show_anim=False):
    anim_class_l = "animate-left" if show_anim else ""
    anim_class_r = "animate-right" if show_anim else ""
    
    html_code = f"""
    <div class="stage-container">
        <div class="side-flask {anim_class_l}" style="background: #ddd; left: 30%;"></div>
        <div class="main-flask">
            <div class="liquid" style="height: {liquid_height}%; background: {liquid_color};"></div>
        </div>
        <div class="side-flask {anim_class_r}" style="background: #888; right: 30%;"></div>
    </div>
    """
    st.components.v1.html(html_code, height=320)

# --- КЕЗЕҢДЕР ---
if st.session_state.step == 1:
    st.header("1-кезең: Сілті ерітіндісін дайындау") [cite: 10]
    st.write("10 г NaOH-ты 20 мл суға қосыңыз.") [cite: 11]
    
    col1, col2 = st.columns([1, 3])
    with col1:
        start = st.button("Реакцияны бастау")
    
    render_lab(40 if start else 0, "#3498db", show_anim=start)
    
    if start:
        st.info("Экзотермиялық реакция жүріп жатыр... Ерітінді жылынады.") [cite: 11]
        st.divider()
        ans = st.radio("Сұрақ: Сабындану реакциясы дегеніміз не?", ["Майдың жануы", "Майдың сілтімен әрекеттесіп, сабын мен глицеринге ыдырауы"]) [cite: 21, 22]
        if st.button("Келесі кезең") and "сілтімен" in ans:
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("2-кезең: Гидролиз (Май + Спирт + Сілті)") [cite: 12]
    st.write("Май мен спиртке сілтіні қосыңыз.") [cite: 13, 14]
    
    start = st.button("Араластыру")
    render_lab(60 if start else 40, "#f1c40f", show_anim=start)
    
    if start:
        st.divider()
        ans = st.radio("Сұрақ: Неге сабын алу үшін спирт қолданамыз?", ["Иіс үшін", "Май мен сілті араласуы үшін ортақ еріткіш"]) [cite: 23, 24]
        if st.button("Келесі кезең") and "ортақ еріткіш" in ans:
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.header("3-кезең: Су моншасында қыздыру") [cite: 15]
    st.write("Қоспаны 30-40 минут баяу қайнатыңыз.") [cite: 16]
    
    start = st.button("Қыздыруды қосу")
    # Қайнау анимациясы үшін сұйықтық түсін өзгерту
    render_lab(60, "#e67e22" if start else "#f1c40f", show_anim=False)
    
    if start:
        st.warning("⚠️ Қауіпсіздік: Көзілдірік киюді ұмытпаңыз!") [cite: 16]
        if st.button("Келесі кезең"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.header("4-кезең: Тұздау (Сабынды бөлу)") [cite: 17, 19]
    st.write("Қоспаға ас тұзын (NaCl) қосыңыз.") [cite: 18]
    
    start = st.button("Тұзды қосу")
    render_lab(70 if start else 60, "#ffffff" if start else "#e67e22", show_anim=start)
    
    if start:
        st.success("Сабын бетке қалқып шықты!") [cite: 18]
        st.divider()
        ans = st.radio("Сұрақ: Неге тұз қосқанда сабын бөлінеді?", ["Ерігіштігі төмендегендіктен (Тұздау)", "Тұз майды жеп қояды"]) [cite: 25, 26]
        if st.button("Аяқтау") and "Тұздау" in ans:
            st.balloons()
            st.header("🎉 Зертханалық жұмыс аяқталды!")
            if st.button("Басынан бастау"):
                st.session_state.step = 1
                st.rerun()
