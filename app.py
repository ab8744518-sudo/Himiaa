import streamlit as st
import pandas as pd
import random

# Настройка страницы
st.set_page_config(
    page_title="Химия 10 - Органикалық химия",
    page_icon="🧪",
    layout="wide"
)

# CSS стили
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E86AB;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .lesson-box {
        background-color: #F0F7FF;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 10px 0;
    }
    .question-box {
        background-color: #FFF8E1;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #FFA000;
    }
    .correct-answer {
        color: #2E7D32;
        font-weight: bold;
    }
    .wrong-answer {
        color: #C62828;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Главный заголовок
st.markdown('<h1 class="main-title">🧪 Органикалық химия - 10 сынып</h1>', unsafe_allow_html=True)
st.markdown("### 34 сабақ | Әр сабақта 19 сұрақтан тест")

# Данные уроков
lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы"},
    {"id": 5, "title": "Фенолдар", "topic": "Ароматтық спирттер"},
    {"id": 6, "title": "Альдегидтер", "topic": "Карбонил тобы"},
    {"id": 7, "title": "Кетондар", "topic": "Кето тобы"},
    {"id": 8, "title": "Көмірсутектер салыстыру", "topic": "Алкан, Алкен, Алкин"},
    {"id": 9, "title": "Карбон қышқылдары", "topic": "Карбоксил тобы"},
    {"id": 10, "title": "Эфирлер", "topic": "Сложный эфирлер"},
    {"id": 11, "title": "Аминдар", "topic": "Амино тобы"},
    {"id": 12, "title": "Аминқышқылдар", "topic": "Аминқышқылдар"},
    {"id": 13, "title": "Галогентуындылар", "topic": "Галогентуындылар"},
    {"id": 14, "title": "Нитросоединениялар", "topic": "Нитро тобы"},
    {"id": 15, "title": "Сульфокислоталар", "topic": "Сульфо тобы"},
    {"id": 16, "title": "Тотығу реакциялары", "topic": "Тотығу"},
    {"id": 17, "title": "Қосылу реакциялары", "topic": "Қосылу"},
    {"id": 18, "title": "Ауыстыру реакциялары", "topic": "Ауыстыру"},
    {"id": 19, "title": "Полимерлеу", "topic": "Полимерлер"},
    {"id": 20, "title": "Изомерлер", "topic": "Изомерлер"},
    {"id": 21, "title": "Гомологтар", "topic": "Гомологтар"},
    {"id": 22, "title": "Функционалдық топтар", "topic": "Функционалдық топтар"},
    {"id": 23, "title": "Качелік реакциялар", "topic": "Качелік реакциялар"},
    {"id": 24, "title": "Саналық реакциялар", "topic": "Саналық реакциялар"},
    {"id": 25, "title": "Органикалық синтез", "topic": "Синтез"},
    {"id": 26, "title": "Биомолекулалар", "topic": "Биомолекулалар"},
    {"id": 27, "title": "Көмірсутектер қасиеттері", "topic": "Қасиеттер"},
    {"id": 28, "title": "Органикалық заттар", "topic": "Заттар"},
    {"id": 29, "title": "Реакция механизмдері", "topic": "Механизмдер"},
    {"id": 30, "title": "Катализ", "topic": "Катализаторлар"},
    {"id": 31, "title": "Энергетика", "topic": "Энергия"},
    {"id": 32, "title": "Кинетика", "topic": "Жылдамдық"},
    {"id": 33, "title": "Термодинамика", "topic": "Термодинамика"},
    {"id": 34, "title": "Қорытынды сабақ", "topic": "Қорытынды"}
]

# Функция для генерации 19 вопросов для урока
def generate_questions(lesson_id):
    questions = []
    for i in range(1, 20):  # 19 вопросов
        question = {
            "question": f"{lesson_id}-сабақ. {i}. Органикалық химияның негізгі ұғымдары қандай?",
            "options": [
                "Вариант A: Органикалық қосылыстар",
                "Вариант B: Көмірсутектер",
                "Вариант C: Функционалдық топтар", 
                "Вариант D: Барлығы дұрыс"
            ],
            "correct": random.randint(0, 3)  # Случайный правильный ответ
        }
        questions.append(question)
    return questions

# Создаем вопросы для всех уроков
all_questions = {}
for lesson in lessons:
    all_questions[lesson["id"]] = generate_questions(lesson["id"])

# Инициализация состояния
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = 1
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "test_started" not in st.session_state:
    st.session_state.test_started = False

# Сайдбар для навигации
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2097/2097067.png", width=100)
    st.title("📚 Меню")
    
    st.markdown("---")
    selected_lesson = st.selectbox(
        "Сабақты таңдаңыз:",
        options=[f"{l['id']}. {l['title']}" for l in lessons],
        index=st.session_state.current_lesson-1
    )
    
    if st.button("Сабаққа өту", type="primary"):
        lesson_id = int(selected_lesson.split(".")[0])
        st.session_state.current_lesson = lesson_id
        st.session_state.test_started = False
        st.rerun()
    
    st.markdown("---")
    st.info("""
    **Нұсқаулық:**
    1. Сабақты таңдаңыз
    2. Тестті бастаңыз
    3. 19 сұраққа жауап беріңіз
    4. Нәтижені тексеріңіз
    """)

# Основной контент
current_lesson_id = st.session_state.current_lesson
current_lesson = lessons[current_lesson_id-1]

st.markdown(f'<div class="lesson-box">', unsafe_allow_html=True)
st.markdown(f"### 📖 Сабақ {current_lesson_id}: {current_lesson['title']}")
st.markdown(f"**Тақырып:** {current_lesson['topic']}")
st.markdown('</div>', unsafe_allow_html=True)

# Кнопка начала теста
if not st.session_state.test_started:
    if st.button(f"🎯 Сабақ {current_lesson_id} тестін бастау (19 сұрақ)", type="primary", use_container_width=True):
        st.session_state.test_started = True
        st.session_state.answers[current_lesson_id] = {}
        st.rerun()

# Если тест начат
if st.session_state.test_started and current_lesson_id in all_questions:
    questions = all_questions[current_lesson_id]
    
    st.markdown(f"### 📝 Тест: {current_lesson['title']}")
    st.markdown(f"**Сұрақтар саны:** 19")
    
    # Прогресс бар
    answered_count = len(st.session_state.answers.get(current_lesson_id, {}))
    progress = answered_count / len(questions)
    st.progress(progress)
    st.caption(f"Жауап берілді: {answered_count}/{len(questions)}")
    
    # Вопросы
    for i, q in enumerate(questions):
        st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f"**{i+1}. {q['question']}**")
        
        # Показываем ответ, если уже отвечали
        if current_lesson_id in st.session_state.answers and i in st.session_state.answers[current_lesson_id]:
            user_answer = st.session_state.answers[current_lesson_id][i]
            is_correct = (user_answer == q['correct'])
            
            if is_correct:
                st.markdown(f'<p class="correct-answer">✓ Сіздің жауабыңыз: {q["options"][user_answer]}</p>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p class="wrong-answer">✗ Сіздің жауабыңыз: {q["options"][user_answer]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="correct-answer">✓ Дұрыс жауап: {q["options"][q["correct"]]}</p>', unsafe_allow_html=True)
        else:
            # Радио-кнопки для ответа
            user_choice = st.radio(
                f"Жауап {i+1}",
                options=q["options"],
                key=f"q{current_lesson_id}_{i}",
                index=None
            )
            
            if user_choice:
                selected_index = q["options"].index(user_choice)
                if current_lesson_id not in st.session_state.answers:
                    st.session_state.answers[current_lesson_id] = {}
                st.session_state.answers[current_lesson_id][i] = selected_index
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Кнопка завершения теста
    if answered_count == len(questions):
        correct_count = 0
        for i, q in enumerate(questions):
            if (current_lesson_id in st.session_state.answers and 
                i in st.session_state.answers[current_lesson_id] and
                st.session_state.answers[current_lesson_id][i] == q["correct"]):
                correct_count += 1
        
        percentage = (correct_count / len(questions)) * 100
        
        st.markdown("---")
        st.markdown(f"### 📊 Тест нәтижесі")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Дұрыс жауап", f"{correct_count}/{len(questions)}")
        with col2:
            st.metric("Ұпай", f"{correct_count*5}")
        with col3:
            st.metric("Пайыз", f"{percentage:.1f}%")
        
        if percentage >= 90:
            st.success("🎉 Тамаша! Сіз сабақты жақсы меңгердіңіз!")
            st.balloons()
        elif percentage >= 70:
            st.info("👍 Жақсы! Бірақ кейбір тақырыптарды қайталаңыз.")
        elif percentage >= 50:
            st.warning("⚠️ Орташа. Теорияны қайта оқыңыз.")
        else:
            st.error("❌ Әлсіз. Сабақты қайта оқып шығыңыз.")
        
        if st.button("🔄 Тестті қайта бастау", type="secondary"):
            st.session_state.answers[current_lesson_id] = {}
            st.rerun()

# Нижняя часть
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>Органикалық химия - 10 сынып | 34 сабақ | 646 сұрақ</p>
    <p>© 2024 Химия оқу платформасы</p>
</div>
""", unsafe_allow_html=True)

# Статистика
st.sidebar.markdown("---")
st.sidebar.markdown("### 📈 Статистика")
total_questions = 34 * 19  # 34 урока × 19 вопросов
st.sidebar.metric("Барлық сұрақтар", total_questions)
st.sidebar.metric("Барлық сабақтар", 34)
st.sidebar.metric("Орташа уақыт", "45 мин/сабақ")
