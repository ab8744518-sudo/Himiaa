import streamlit as st
import pandas as pd

# Настройка страницы
st.set_page_config(page_title="Химия 10", layout="wide")

# Заголовок
st.title("🧪 Органикалық химия - 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# 19 уроков
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
]

# Вопросы для 8 урока (пример)
questions_8 = [
    {
        "question": "1. Көміртек атомдары арасында тек дара байланыстары бар көмірсутектер қалай аталады?",
        "options": ["А) Алкендер", "В) Алкиндер", "С) Алкандар", "D) Арендер"],
        "correct": 2
    },
    {
        "question": "2. Құрамында бір қос байланысы бар көмірсутектердің жалпы формуласы қандай?",
        "options": ["А) CnH2n+2", "В) CnH2n", "С) CnH2n-2", "D) CnHn"],
        "correct": 1
    },
    {
        "question": "3. Алкандарға, алкендерге және алкиндерге тән ортақ химиялық қасиет:",
        "options": ["А) Қосылу реакциясы", "В) Полимерлену реакциясы", 
                   "С) Тотығу (жану) реакциясы", "D) Орынбасу реакциясы"],
        "correct": 2
    },
    {
        "question": "4. Көміртек атомдарының гибридтену типін салыстырыңыз. Қай қатар дұрыс (алкан – алкен – алкин)?",
        "options": ["А) sp³ - sp² - sp", "В) sp² - sp³ - sp", 
                   "С) sp - sp² - sp³", "D) sp³ - sp - sp²"],
        "correct": 0
    },
    {
        "question": "5. Қай көмірсутектер класы бром суын түссіздендірмейді?",
        "options": ["А) Алкендер", "В) Алкиндер", "С) Алкандар", "D) Диендер"],
        "correct": 2
    },
    {
        "question": "6. Молекуласындағы сутек атомдарының саны ең аз көмірсутектер класы:",
        "options": ["А) Алкандар", "В) Алкендер", "С) Алкиндер", "D) Циклоалкандар"],
        "correct": 2
    },
    {
        "question": "7. Байланыс ұзындығының кему реті:",
        "options": ["А) Дара > Қос > Үш", "В) Үш > Қос > Дара", 
                   "С) Қос > Дара > Үш", "D) Барлығы бірдей"],
        "correct": 0
    },
    {
        "question": "8. Алкендер мен алкиндерге тән реакция типі:",
        "options": ["А) Айрылу", "В) Қосылу", "С) Алмасу", "D) Реакция жоқ"],
        "correct": 1
    },
    {
        "question": "9. Тек алкиндерге тән сапалық реакция:",
        "options": ["А) Бром суын түссіздендіру", "В) Күміс оксидімен тұнба", 
                   "С) Жану", "D) Гидрлену"],
        "correct": 1
    },
    {
        "question": "10. Көміртек атомдары арасындағы байланыс энергиясы ең жоғары:",
        "options": ["А) Алкандар", "В) Алкендер", "С) Алкиндер", "D) Барлығы бірдей"],
        "correct": 2
    }
]

# Вопросы для других уроков (шаблон)
questions_template = [
    {
        "question": f"1. {lessons[0]['title']} туралы сұрақ 1?",
        "options": ["А) Вариант 1", "В) Вариант 2", "С) Вариант 3", "D) Вариант 4"],
        "correct": 0
    },
    {
        "question": f"2. {lessons[0]['title']} туралы сұрақ 2?",
        "options": ["А) Вариант 1", "В) Вариант 2", "С) Вариант 3", "D) Вариант 4"],
        "correct": 1
    },
    # ... и так 10 вопросов
]

# Показываем список уроков
st.write("### 📚 Сабақтар тізімі")
cols = st.columns(3)
for idx, lesson in enumerate(lessons):
    with cols[idx % 3]:
        if st.button(f"Сабақ {lesson['id']}: {lesson['title']}", key=f"btn_{lesson['id']}"):
            st.session_state.selected_lesson = lesson['id']
            st.rerun()

# Если урок выбран
if 'selected_lesson' in st.session_state:
    lesson_id = st.session_state.selected_lesson
    lesson = lessons[lesson_id-1]
    
    st.markdown("---")
    st.write(f"## 📖 Сабақ {lesson_id}: {lesson['title']}")
    st.write(f"**Тақырып:** {lesson['topic']}")
    
    # Показываем тест
    st.write("### ✅ Тест (10 сұрақ)")
    
    # Используем вопросы для 8 урока, для остальных - шаблон
    if lesson_id == 8:
        questions = questions_8
    else:
        questions = []
        for i in range(10):
            questions.append({
                "question": f"{i+1}. {lesson['title']} туралы сұрақ {i+1}?",
                "options": ["А) Вариант 1", "В) Вариант 2", "С) Вариант 3", "D) Вариант 4"],
                "correct": i % 4  # для примера
            })
    
    score = 0
    user_answers = {}
    
    for i, q in enumerate(questions):
        st.write(f"**{q['question']}**")
        
        # Создаем ключ для каждого вопроса
        answer_key = f"lesson_{lesson_id}_q_{i}"
        
        # Если уже отвечали, показываем результат
        if answer_key in st.session_state:
            user_answer = st.session_state[answer_key]
            is_correct = (user_answer == q['correct'])
            
            if is_correct:
                st.success(f"✓ Сіздің жауабыңыз: {q['options'][user_answer]}")
                score += 1
            else:
                st.error(f"✗ Сіздің жауабыңыз: {q['options'][user_answer]}")
                st.info(f"✓ Дұрыс жауап: {q['options'][q['correct']]}")
        else:
            # Радио-кнопки для ответа
            user_choice = st.radio(
                f"Жауап {i+1}",
                q["options"],
                key=f"radio_{lesson_id}_{i}",
                index=None
            )
            
            if user_choice:
                selected_index = q["options"].index(user_choice)
                st.session_state[answer_key] = selected_index
                st.rerun()
        
        st.write("---")
    
    # Кнопка проверки
    if st.button("Тестті аяқтау", type="primary"):
        total_questions = len(questions)
        percentage = (score / total_questions) * 100
        
        st.success(f"**Нәтиже: {score}/{total_questions} ({percentage:.0f}%)**")
        
        if percentage >= 90:
            st.balloons()
            st.info("🎉 Тамаша! Сіз сабақты жақсы меңгердіңиз!")
        elif percentage >= 70:
            st.info("👍 Жақсы! Бірақ кейбір тармақтарды қайталаңыз.")
        else:
            st.warning("📚 Теорияны қайта оқып шығыңыз.")
    
    # Кнопка назад
    if st.button("← Басты бетке қайту"):
        del st.session_state.selected_lesson
        st.rerun()

# Статистика
st.markdown("---")
st.write("**Статистика:** 19 сабақ × 10 сұрақ = 190 сұрақ")
