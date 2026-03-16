import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("🧪 Этнохимиялық виртуалды зертхана")

if 'step' not in st.session_state:
    st.session_state.step = 1

# --- HTML + CSS + JS Анимация блогы ---
def run_animation(step_type, color):
    html_code = f"""
    <div id="canvas" style="width:100%; height:350px; position:relative; background:#f8f9fa; border-radius:15px; overflow:hidden; border:2px solid #ddd;">
        <div id="main-flask" style="position:absolute; bottom:50px; left:50%; transform:translateX(-50%); width:100px; height:130px; border:4px solid #333; border-radius: 0 0 50px 50px; background:rgba(255,255,255,0.7); z-index:10;">
            <div id="liquid" style="position:absolute; bottom:0; width:100%; height:0%; background:{color}; transition: height 2s ease-in-out;"></div>
        </div>
        
        <div id="left-flask" style="position:absolute; top:50px; left:-100px; width:50px; height:70px; border:3px solid #555; background:#eee; border-radius:5px; transition: all 1.5s ease;"></div>
        
        <div id="right-flask" style="position:absolute; top:50px; right:-100px; width:50px; height:70px; border:3px solid #555; background:#888; border-radius:5px; transition: all 1.5s ease;"></div>
    </div>

    <script>
        setTimeout(() => {{
            const left = document.getElementById('left-flask');
            const right = document.getElementById('right-flask');
            const liquid = document.getElementById('liquid');
            
            // Заттарды ортаға әкелу және құю
            left.style.left = '38%';
            left.style.transform = 'rotate(45deg)';
            
            setTimeout(() => {{
                right.style.right = '38%';
                right.style.transform = 'rotate(-45deg)';
                
                setTimeout(() => {{
                    liquid.style.height = '60%';
                    left.style.opacity = '0';
                    right.style.opacity = '0';
                }}, 1000);
            }}, 1000);
        }}, 500);
    </script>
    """
    components.html(html_code, height=360)

# --- Зертханалық жұмыс кезеңдері ---

# 1-кезең: Сілті дайындау
if st.session_state.step == 1:
    st.header("1-кезең: Сілті ерітіндісін дайындау [cite: 10]")
    st.write("10 г NaOH-ты 20 мл суда ерітіңіз. [cite: 11]")
    
    if st.button("Реакцияны бастау"):
        run_animation("pour", "#3498db")
        st.info("Экзотермиялық реакция: Ерітінді жылынады. [cite: 11]")
        
        st.divider()
        st.subheader("Сұрақ:")
        ans = st.radio("Сабындану реакциясы дегеніміз не? [cite: 21]", 
                      ["Майдың жануы", "Майдың сілтімен әрекеттесіп, сабын мен глицеринге ыдырауы [cite: 22]"])
        
        if st.button("Келесі кезең"):
            if "сілтімен" in ans:
                st.session_state.step = 2
                st.rerun()

# 2-кезең: Гидролиз
elif st.session_state.step == 2:
    st.header("2-кезең: Гидролиз реакциялары [cite: 12]")
    st.write("30 мл май мен 10 мл спиртке сілтіні қосыңыз. [cite: 13, 14]")
    
    if st.button("Араластыру"):
        run_animation("pour", "#f1c40f")
        
        st.divider()
        st.subheader("Сұрақ:")
        ans = st.radio("Неге сабын алу үшін спирт қолданамыз? [cite: 23]", 
                      ["Иіс беру үшін", "Ортақ еріткіш ретінде реакцияны жылдамдатады [cite: 24]"])
        
        if st.button("Келесі кезең"):
            if "еріткіш" in ans:
                st.session_state.step = 3
                st.rerun()

# 3-кезең: Қыздыру
elif st.session_state.step == 3:
    st.header("3-кезең: Су моншасында қыздыру [cite: 15]")
    st.warning("⚠️ Көзілдірік киіңіз! [cite: 16]")
    
    if st.button("Қыздыруды бастау"):
        st.write("Қоспа 30-40 минут баяу қайнатылуда... [cite: 16]")
        # Қайнау анимациясы (көпіршіктер)
        st.session_state.step = 4
        st.rerun()

# 4-кезең: Тұздау
elif st.session_state.step == 4:
    st.header("4-кезең: Сабынды тұндыру (Тұздау) [cite: 17]")
    st.write("Қоспаға ас тұзының (NaCl) қаныққан ерітіндісін қосыңыз. [cite: 18]")
    
    if st.button("Тұзды қосу"):
        run_animation("salt", "#ffffff")
        st.success("Сабын бетке қалқып шықты! [cite: 18]")
        
        st.divider()
        st.subheader("Сұрақ:")
        ans = st.radio("Неге тұз (NaCl) қосқанда сабын бөлініп шығады? [cite: 25]", 
                      ["Сабын еріп кетеді", "Тұздау әсері: ерігіштігі төмендегендіктен [cite: 26]"])
        
        if st.button("Аяқтау"):
            if "Тұздау" in ans:
                st.balloons()
                st.success("Тәжірибе аяқталды!")
                if st.button("Басынан бастау"):
                    st.session_state.step = 1
                    st.rerun()
