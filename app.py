```python
import streamlit as st

# ── страница ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Этнохимиялық анықтамалық — Зертхана №2",
    page_icon="🧫",
    layout="wide",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
body { background: #0a0f1a; color: #e2e8f0; }
.stApp { background: linear-gradient(135deg, #020817 0%, #0f172a 60%, #022c22 100%); }
h1, h2, h3 { color: #34d399; }
.stTabs [data-baseweb="tab-list"] { background: #1e293b; border-radius: 12px; gap: 4px; padding: 4px; }
.stTabs [data-baseweb="tab"] { color: #94a3b8; border-radius: 8px; }
.stTabs [aria-selected="true"] { background: #059669 !important; color: white !important; }
.block { background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 20px; margin-bottom: 12px; }
.step-blue  { border-left: 4px solid #3b82f6; background: #0f2337; border-radius: 12px; padding: 16px; }
.step-purple{ border-left: 4px solid #8b5cf6; background: #1a0f37; border-radius: 12px; padding: 16px; }
.step-orange{ border-left: 4px solid #f97316; background: #2d1500; border-radius: 12px; padding: 16px; }
.step-green { border-left: 4px solid #10b981; background: #022c1a; border-radius: 12px; padding: 16px; }
.warn  { background: #2d0707; border: 1px solid #7f1d1d; border-radius: 10px; padding: 10px 14px; color: #fca5a5; }
.hint  { background: #2d2000; border: 1px solid #713f12; border-radius: 10px; padding: 10px 14px; color: #fde68a; }
.answer{ background: #022c1a; border: 1px solid #065f46; border-radius: 10px; padding: 10px 14px; color: #6ee7b7; }
.eq-box{ background: #0f172a; border-radius: 12px; padding: 16px; font-family: monospace; }
.material-card { background: #0f172a; border: 1px solid #334155; border-radius: 12px;
                 padding: 12px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "oil_type"     not in st.session_state: st.session_state.oil_type     = "sunflower"
if "alkali_type"  not in st.session_state: st.session_state.alkali_type  = "NaOH"
if "current_step" not in st.session_state: st.session_state.current_step = 1
if "answers"      not in st.session_state: st.session_state.answers      = ["", "", ""]
if "revealed"     not in st.session_state: st.session_state.revealed     = [False, False, False]
if "hints"        not in st.session_state: st.session_state.hints        = [False, False, False]
if "score"        not in st.session_state: st.session_state.score        = None

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='background:#020817;border-bottom:1px solid #1e293b;padding:12px 0 10px;margin-bottom:4px'>
  <span style='color:#34d399;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase'>
    🧫 Этнохимиялық анықтамалық · Зертханалық жұмыс №2
  </span><br>
  <span style='color:white;font-size:20px;font-weight:800'>Табиғи майлардан сабын алу</span>
  <span style='color:#475569;font-size:12px;float:right'>Сабындану реакциялары</span>
</div>
""", unsafe_allow_html=True)

st.info("**Мақсаты:** Майлардың химиялық заты, сілтілік ортада триглицеридтердің гидролиздену процессін зерттеу және сабын алу технологиясын меңгеру.")

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🧪 Зерттеу", "⚗️ Теңдеу", "🔬 Сұрақтар"])


# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — EXPERIMENT
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    col_mat, col_beaker, col_steps = st.columns([1.1, 1, 1.1])

    # ── Left: Materials ──────────────────────────────────────────────────────
    with col_mat:
        st.markdown("### 🧪 Реагенттерді таңдаңыз")

        st.markdown("**Май түрі:**")
        oil_col1, oil_col2 = st.columns(2)
        with oil_col1:
            if st.button("🌻 Күнбағыс майы\n*(Linoleic C18:2)*",
                         use_container_width=True,
                         type="primary" if st.session_state.oil_type == "sunflower" else "secondary"):
                st.session_state.oil_type = "sunflower"
                st.rerun()
        with oil_col2:
            if st.button("🫒 Зайтун майы\n*(Oleic C18:1)*",
                         use_container_width=True,
                         type="primary" if st.session_state.oil_type == "olive" else "secondary"):
                st.session_state.oil_type = "olive"
                st.rerun()

        st.markdown("**Сілті түрі:**")
        alk_col1, alk_col2 = st.columns(2)
        with alk_col1:
            if st.button("⬜ NaOH\n*Қатты сабын*",
                         use_container_width=True,
                         type="primary" if st.session_state.alkali_type == "NaOH" else "secondary"):
                st.session_state.alkali_type = "NaOH"
                st.rerun()
        with alk_col2:
            if st.button("🟡 KOH\n*Суйық сабын*",
                         use_container_width=True,
                         type="primary" if st.session_state.alkali_type == "KOH" else "secondary"):
                st.session_state.alkali_type = "KOH"
                st.rerun()

        result_label = "Қатты сабын" if st.session_state.alkali_type == "NaOH" else "Суйық сабын"
        st.markdown(f"""
        <div class='block' style='font-size:13px'>
          <div style='color:#94a3b8;font-size:11px;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px'>Сипаттамалар</div>
          <table style='width:100%;border-collapse:collapse'>
            <tr><td style='color:#64748b'>Май көлемі</td><td style='color:#fbbf24;text-align:right'>30 мл</td></tr>
            <tr><td style='color:#64748b'>Сілті</td><td style='color:#93c5fd;text-align:right'>10 г</td></tr>
            <tr><td style='color:#64748b'>Су</td><td style='color:#e2e8f0;text-align:right'>20 мл</td></tr>
            <tr><td style='color:#64748b'>Этанол</td><td style='color:#c4b5fd;text-align:right'>10 мл</td></tr>
            <tr><td style='color:#64748b'>Қыздыру</td><td style='color:#fb923c;text-align:right'>30–40 мин</td></tr>
            <tr><td style='color:#64748b'>Нәтиже</td><td style='color:#34d399;text-align:right'>{result_label}</td></tr>
          </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='warn'>
          <b>⚠️ Қауіпсіздік ережелері:</b><br>
          • Көзілдірік және қолғап кию міндетті<br>
          • NaOH суда ерігенде жылу бөлінеді<br>
          • Сілтіні баяу, мұқият қосыңыз<br>
          • Балалар қадағалаусыз жұмыс жасамасын
        </div>
        """, unsafe_allow_html=True)

    # ── Center: Beaker ───────────────────────────────────────────────────────
    with col_beaker:
        step = st.session_state.current_step
        oil  = st.session_state.oil_type
        alk  = st.session_state.alkali_type

        status_text = {
            1: "Сілті ерітіндісін дайындау...",
            2: "Компоненттерді қосу...",
            3: "Су моншасында қыздыру...",
            4: "Тұздау — сабын бөлінуде...",
        }[step]

        st.markdown(f"""
        <div style='text-align:center;margin-bottom:6px'>
          <div style='color:#64748b;font-size:11px;text-transform:uppercase;letter-spacing:1px'>Виртуалды зертхана</div>
          <div style='color:#cbd5e1;font-size:14px;font-weight:600'>{status_text}</div>
        </div>
        """, unsafe_allow_html=True)

        # SVG beaker
        liq_colors = ["#f5c842", "#dde8e8", "#d4c87a", "#c8a84a", "#f5f0e0"]
        liq_color  = liq_colors[step - 1]
        liq_h      = [40, 55, 65, 65, 70][step - 1]
        liq_y      = 195 - int(liq_h * 1.7)

        flame_html = ""
        if step == 3:
            flame_html = """
            <rect x="55" y="200" width="50" height="8" rx="4" fill="#f97316" opacity="0.8"/>
            <ellipse cx="68" cy="195" rx="7" ry="12" fill="#ef4444" opacity="0.8"/>
            <ellipse cx="80" cy="190" rx="8" ry="16" fill="#f97316" opacity="0.9"/>
            <ellipse cx="92" cy="195" rx="7" ry="12" fill="#ef4444" opacity="0.8"/>
            <ellipse cx="68" cy="193" rx="4" ry="8" fill="#fbbf24" opacity="0.9"/>
            <ellipse cx="80" cy="187" rx="5" ry="10" fill="#fde68a" opacity="0.9"/>
            <ellipse cx="92" cy="193" rx="4" ry="8" fill="#fbbf24" opacity="0.9"/>
            """

        bubbles_html = ""
        if step == 3:
            for bx, by, r in [(50,150,3),(65,130,4),(80,155,3),(95,140,4),(110,148,3)]:
                bubbles_html += f'<circle cx="{bx}" cy="{by}" r="{r}" fill="white" opacity="0.4"/>'

        soap_layer = ""
        if step == 4:
            soap_layer = f'<rect x="20" y="{liq_y - 20}" width="120" height="22" fill="#fffde7" opacity="0.95" clip-path="url(#bc)"/>'

        nacl_html = ""
        if step == 4:
            nacl_html = """
            <rect x="35" y="175" width="7" height="7" fill="#e2e8f0" rx="1" opacity="0.9"/>
            <rect x="60" y="178" width="6" height="6" fill="#e2e8f0" rx="1"/>
            <rect x="88" y="173" width="8" height="8" fill="#e2e8f0" rx="1" opacity="0.9"/>
            <rect x="113" y="177" width="6" height="6" fill="#e2e8f0" rx="1"/>
            """

        rod_html = ""
        if step in (2, 3):
            rod_html = '<line x1="100" y1="5" x2="90" y2="190" stroke="#64748b" stroke-width="3" stroke-linecap="round"/>'

        steam_html = ""
        if step == 3:
            steam_html = """
            <path d="M60 12 Q55 2 62 -6" stroke="#94a3b8" stroke-width="2" fill="none" opacity="0.5"/>
            <path d="M80 8  Q75-2 82-10" stroke="#94a3b8" stroke-width="2" fill="none" opacity="0.5"/>
            <path d="M100 12 Q95 2 102 -6" stroke="#94a3b8" stroke-width="2" fill="none" opacity="0.5"/>
            """

        oil_label  = "Күнбағыс" if oil == "sunflower" else "Зайтун"
        alk_label  = "NaOH" if alk == "NaOH" else "KOH"

        svg = f"""
        <svg viewBox="0 0 160 220" width="220" height="260" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <clipPath id="bc">
              <path d="M20 20 L20 185 Q20 195 30 195 L130 195 Q140 195 140 185 L140 20 Z"/>
            </clipPath>
            <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%"   stop-color="{liq_color}" stop-opacity="0.7"/>
              <stop offset="50%"  stop-color="{liq_color}" stop-opacity="1"/>
              <stop offset="100%" stop-color="{liq_color}" stop-opacity="0.7"/>
            </linearGradient>
          </defs>
          {flame_html}
          <rect x="20" y="{liq_y}" width="120" height="{int(liq_h*1.7)}"
                fill="url(#lg)" clip-path="url(#bc)"/>
          {soap_layer}
          {bubbles_html}
          {nacl_html}
          {rod_html}
          {steam_html}
          <path d="M20 20 L20 185 Q20 195 30 195 L130 195 Q140 195 140 185 L140 20"
                fill="none" stroke="#94a3b8" stroke-width="3"/>
          <path d="M20 20 L10 5"   fill="none" stroke="#94a3b8" stroke-width="3"/>
          <path d="M140 20 L150 5" fill="none" stroke="#94a3b8" stroke-width="3"/>
          <line x1="130" y1="140" x2="140" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
          <line x1="130" y1="95"  x2="140" y2="95"  stroke="#94a3b8" stroke-width="1.5"/>
          <line x1="130" y1="50"  x2="140" y2="50"  stroke="#94a3b8" stroke-width="1.5"/>
        </svg>
        """

        st.markdown(f"<div style='display:flex;justify-content:center'>{svg}</div>", unsafe_allow_html=True)

        # labels
        labels_html = f"<div style='text-align:center;font-size:12px;color:#94a3b8'>"
        labels_html += f"<span style='color:#fbbf24'>{oil_label} майы: 30мл</span>"
        if step >= 2: labels_html += f" &nbsp;·&nbsp; <span style='color:#93c5fd'>{alk_label}/H₂O: 10г/20мл</span>"
        if step >= 2: labels_html += " &nbsp;·&nbsp; <span style='color:#c4b5fd'>Этанол: 10мл</span>"
        if step == 4: labels_html += " &nbsp;·&nbsp; <span style='color:#e2e8f0'>NaCl</span>"
        labels_html += "</div>"
        st.markdown(labels_html, unsafe_allow_html=True)

        # progress bar
        st.progress(step / 4, text=f"Прогресс: {step}/4 кезең")

        if step == 4:
            soap_name = "Қатты сабын" if alk == "NaOH" else "Суйық сабын"
            ion_name  = "натрий" if alk == "NaOH" else "калий"
            st.success(f"🎉 {soap_name} алынды! — {oil_label} майынан жасалған {ion_name} сабыны")

    # ── Right: Steps ─────────────────────────────────────────────────────────
    with col_steps:
        st.markdown("### 📋 Жұмыс барысы")

        STEPS = [
            {
                "id": 1, "icon": "🧊", "color": "step-blue",
                "title": "Сілті ерітіндісін дайындау",
                "desc":  "10 г NaOH-ті 20 мл тазартылған суда ерітіңіз.",
                "details": [
                    "Ыдысқа 20 мл суық тазартылған су алыңыз.",
                    "NaOH гранулаларын ақырын суға қосыңыз (керісінше емес!).",
                    "Шыны таяқшамен үздіксіз араластырыңыз.",
                    "Ерітінді қатты жылынады — экзотермиялық реакция.",
                    "Бөлме температурасына дейін суытыңыз.",
                ],
                "note": "⚠️ NaOH — күшті сілті! Терімен жанасуынан сақтаныңыз.",
            },
            {
                "id": 2, "icon": "🫗", "color": "step-purple",
                "title": "Гидролиз реакциясы — қосу",
                "desc":  "Майды, спиртті және сілтіні мұқият біріктіру.",
                "details": [
                    "Стаканға 30 мл өсімдік майын құйыңыз.",
                    "10 мл этил спиртін (96%) майға қосыңыз.",
                    "Май–спирт қоспасын жақсылап араластырыңыз.",
                    "Суыған NaOH ерітіндісін тамшылатып қосыңыз.",
                    "Шыны таяқшамен 5–10 минут бойы араластырыңыз.",
                ],
                "note": "💡 Этанол — ортақ еріткіш: май (полярлы емес) + сілті (полярлы).",
            },
            {
                "id": 3, "icon": "🔥", "color": "step-orange",
                "title": "Су моншасында қыздыру",
                "desc":  "30–40 минут баяу қыздыру арқылы реакцияны аяқтау.",
                "details": [
                    "Үлкен ыдысқа 70–80°C ыстық су толтырыңыз.",
                    "Реакция қоспасы бар стаканды су моншасына қойыңыз.",
                    "30–40 минут баяу қыздырыңыз.",
                    "Мезгіл-мезгіл таяқшамен араластырыңыз.",
                    "Тұтқыр консистенцияға жеткізіңіз.",
                ],
                "note": "⚠️ Тікелей отта қыздырмаңыз — этанол өртенуі мүмкін!",
            },
            {
                "id": 4, "icon": "🧂", "color": "step-green",
                "title": "Тұздау (Salting-out)",
                "desc":  "NaCl ерітіндісімен сабынды бөліп алу.",
                "details": [
                    "Қаныққан NaCl ерітіндісін дайындаңыз.",
                    "Аяқталған қоспаға NaCl ерітіндісін қосыңыз.",
                    "Araластырыңыз — сабын бетіне қалқып шығады.",
                    "Бетіндегі сабынды жинап, қалыпқа құйыңыз.",
                    "Суытып, кептіріңіз.",
                ],
                "note": "💡 Na⁺ иондары судың сабынды ерітетін мүмкіндігін төмендетеді.",
            },
        ]

        # Step selector buttons
        btn_cols = st.columns(4)
        for i, s in enumerate(STEPS):
            with btn_cols[i]:
                active = (st.session_state.current_step == s["id"])
                if st.button(f"{s['icon']} {s['id']}", use_container_width=True,
                             type="primary" if active else "secondary",
                             key=f"stepbtn_{s['id']}"):
                    st.session_state.current_step = s["id"]
                    st.rerun()

        cur = STEPS[st.session_state.current_step - 1]
        details_html = "".join(
            f"<li style='margin:5px 0'>{d}</li>" for d in cur["details"]
        )
        st.markdown(f"""
        <div class='{cur["color"]}' style='margin-top:10px'>
          <div style='font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;opacity:.7'>
            {cur["id"]}-кезең
          </div>
          <div style='font-size:16px;font-weight:800;margin:4px 0'>{cur["icon"]} {cur["title"]}</div>
          <div style='font-size:13px;opacity:.8;margin-bottom:10px'>{cur["desc"]}</div>
          <ol style='margin:0;padding-left:18px;font-size:13px;line-height:1.7'>{details_html}</ol>
          <div style='margin-top:10px;font-size:12px;opacity:.85'>{cur["note"]}</div>
        </div>
        """, unsafe_allow_html=True)

        prev_col, next_col = st.columns(2)
        with prev_col:
            if st.button("← Алдыңғы", use_container_width=True,
                         disabled=(st.session_state.current_step == 1)):
                st.session_state.current_step -= 1
                st.rerun()
        with next_col:
            if st.button("Келесі →", use_container_width=True,
                         disabled=(st.session_state.current_step == 4),
                         type="primary"):
                st.session_state.current_step += 1
                st.rerun()

    # ── Materials reference ──────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 🛠️ Қажетті құралдар мен материалдар")
    materials = [
        ("🫙", "Өсімдік майы",    "Күнбағыс / Зайтун, 30 мл"),
        ("🧴", "NaOH / KOH",     "Сілті, 10 г"),
        ("💧", "Этил спирті",    "96%, 10 мл"),
        ("🥃", "Шыны стакан",    "200–300 мл"),
        ("🥢", "Шыны таяқша",    "Араластыруға"),
        ("🍲", "Су моншасы",     "70–80°C"),
        ("🧂", "NaCl (ас тұзы)", "Қаныққан ерітінді"),
        ("🥽", "Қорғаныш",       "Көзілдірік + қолғап"),
    ]
    mat_cols = st.columns(4)
    for i, (icon, name, sub) in enumerate(materials):
        with mat_cols[i % 4]:
            st.markdown(f"""
            <div class='material-card'>
              <div style='font-size:28px'>{icon}</div>
              <div style='color:#cbd5e1;font-size:13px;font-weight:600'>{name}</div>
              <div style='color:#475569;font-size:11px'>{sub}</div>
            </div>
            """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — CHEMICAL EQUATION
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    oil = st.session_state.oil_type
    alk = st.session_state.alkali_type
    is_naoh   = (alk == "NaOH")
    cation    = "Na" if is_naoh else "K"
    soap_name = "натрий карбоксилаты (қатты сабын)" if is_naoh else "калий карбоксилаты (суйық сабын)"
    alkali_kz = "Натрий гидроксиді" if is_naoh else "Калий гидроксиді"
    oil_formula  = "C₃H₅(OOCС₁₇H₃₁)₃" if oil == "sunflower" else "C₃H₅(OOCС₁₇H₃₃)₃"
    fatty_acid   = "C₁₇H₃₃COO"
    soap_formula = f"{fatty_acid}{cation}"
    r_label  = "C₁₇H₃₁ (линол қышқылы)" if oil == "sunflower" else "C₁₇H₃₃ (олеин қышқылы)"

    st.markdown("## ⚗️ Химиялық теңдеу")

    st.markdown(f"""
    <div class='eq-box'>
      <div style='color:#94a3b8;font-size:11px;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px'>
        Сабындану реакциясы (Saponification):
      </div>
      <div style='font-size:18px;margin-bottom:6px'>
        <span style='color:#fbbf24;font-weight:700'>{oil_formula}</span>
        <span style='color:#64748b;margin:0 8px'>+</span>
        <span style='color:#93c5fd;font-weight:700'>3{cation}OH</span>
        <span style='color:#64748b;margin:0 12px'>→</span>
        <span style='color:#34d399;font-weight:700'>3 {soap_formula}</span>
        <span style='color:#64748b;margin:0 8px'>+</span>
        <span style='color:#f9a8d4;font-weight:700'>C₃H₅(OH)₃</span>
      </div>
      <div style='font-size:12px;color:#64748b'>
        <span style='color:#92400e'>Триглицерид (май)</span> +
        <span style='color:#1e40af'> {alkali_kz}</span> →
        <span style='color:#065f46'> {soap_name}</span> +
        <span style='color:#831843'> Глицерин</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_struct, col_mech = st.columns(2)

    with col_struct:
        st.markdown(f"""
        <div class='block'>
          <div style='color:#94a3b8;font-size:11px;text-transform:uppercase;margin-bottom:10px'>
            Триглицеридтің құрылымы
          </div>
          <pre style='color:#cbd5e1;font-size:14px;font-family:monospace;line-height:1.8;margin:0'>
<span style='color:#f9a8d4'>CH₂</span>—O—CO—<span style='color:#fbbf24'>R₁</span>
 │
<span style='color:#f9a8d4'>CH </span>—O—CO—<span style='color:#fbbf24'>R₂</span>
 │
<span style='color:#f9a8d4'>CH₂</span>—O—CO—<span style='color:#fbbf24'>R₃</span></pre>
          <div style='color:#64748b;font-size:12px;margin-top:10px'>R = {r_label}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_mech:
        st.markdown(f"""
        <div class='block'>
          <div style='color:#94a3b8;font-size:11px;text-transform:uppercase;margin-bottom:10px'>
            Гидролиз механизмі
          </div>
          <ol style='color:#cbd5e1;font-size:13px;line-height:2;padding-left:18px;margin:0'>
            <li><span style='color:#93c5fd'>OH⁻</span> иоңы эфир байланысына шабуыл жасайды</li>
            <li>Тетраэдрлік аралық қосылыс түзіледі</li>
            <li><span style='color:#f9a8d4'>—OR</span> тобы кетеді → карбоксилат анионы</li>
            <li>✓ <span style='color:#34d399'>RCOO⁻{cation}⁺</span> = Сабын молекуласы</li>
          </ol>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='block'>
      <div style='color:#94a3b8;font-size:11px;text-transform:uppercase;margin-bottom:10px'>
        Сабын молекуласының амфифильдік құрылымы
      </div>
      <div style='font-family:monospace;font-size:15px;margin-bottom:10px'>
        <span style='color:#fbbf24'>C—C—C—C—C—C—C—C—C—C</span>
        <span style='color:#64748b'>—</span>
        <span style='color:#f87171;font-weight:700'>COO⁻</span>
        &nbsp;
        <span style='color:#93c5fd;font-weight:700'>{cation}⁺</span>
      </div>
      <div style='font-size:12px;display:flex;gap:24px'>
        <span>
          <span style='display:inline-block;width:50px;height:8px;background:#92400e;border-radius:4px;vertical-align:middle'></span>
          &nbsp; Гидрофобты «құйрық» (май)
        </span>
        <span>
          <span style='display:inline-block;width:24px;height:8px;background:#1d4ed8;border-radius:4px;vertical-align:middle'></span>
          &nbsp; Гидрофильді «бас» (су)
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — RESEARCH QUIZ
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("## 🔬 Зерттеу сұрақтары")

    QUESTIONS = [
        {
            "id": 0,
            "question": "1. Сабындану реакциясы дегеніміз не?",
            "hint":     "Майдың (триглицеридтің) сілтімен әрекеттесуін ойлаңыз...",
            "answer":   "Май (триглицерид) сілтімен (NaOH немесе KOH) әрекеттесіп, май қышқылдарының тұздары (сабын) мен глицеринге ыдырайды. Бұл процесс «сабындану» немесе saponification деп аталады.",
            "keyword":  "триглицерид",
        },
        {
            "id": 1,
            "question": "2. Неге сабын алу үшін спирт (этанол) қолданамыз?",
            "hint":     "Май мен сілті судағы ерігіштігін ойлаңыз...",
            "answer":   "Май (полярлы емес) мен сілті ерітіндісі (полярлы) бір-бірінде ерімейді. Этанол ортақ еріткіш ретінде екі фазаны біріктіреді, реакция жылдамдатады.",
            "keyword":  "еріткіш",
        },
        {
            "id": 2,
            "question": "3. Неге тұз (NaCl) қосқанда сабын бөлініп шығады?",
            "hint":     "«Тұздау әсері» немесе salting-out эффектісін ойлаңыз...",
            "answer":   "«Тұздау әсері» (salting-out): NaCl иондары су молекулаларын тартады, сабынның ерігіштігі төмендейді де сабын бетіне қалқып шығады.",
            "keyword":  "тұздау",
        },
    ]

    for q in QUESTIONS:
        i = q["id"]
        with st.container():
            st.markdown(f"**{q['question']}**")
            st.session_state.answers[i] = st.text_area(
                label=f"answer_{i}",
                value=st.session_state.answers[i],
                placeholder="Жауабыңызды осында жазыңыз...",
                height=90,
                key=f"qa_{i}",
                label_visibility="collapsed",
            )

            h_col, r_col = st.columns([1, 1])
            with h_col:
                if st.button(
                    "💡 Кеңесті жасыру" if st.session_state.hints[i] else "💡 Кеңес алу",
                    key=f"hint_{i}"
                ):
                    st.session_state.hints[i] = not st.session_state.hints[i]
                    st.rerun()
            with r_col:
                if st.button("📖 Жауабын көру", key=f"reveal_{i}"):
                    st.session_state.revealed[i] = True
                    st.rerun()

            if st.session_state.hints[i]:
                st.markdown(f"<div class='hint'>💡 {q['hint']}</div>", unsafe_allow_html=True)

            if st.session_state.revealed[i]:
                st.markdown(f"""
                <div class='answer'>
                  <b>Толық жауап:</b><br>{q['answer']}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")

    if st.button("✅ Жауаптарды тексеру", type="primary"):
        score = sum(
            1 for q in QUESTIONS
            if q["keyword"] in st.session_state.answers[q["id"]].lower()
        )
        st.session_state.score = score
        st.rerun()

    if st.session_state.score is not None:
        s = st.session_state.score
        if s == 3:
            st.success(f"🏆 Керемет! {s}/3 — барлық тірек сөздер табылды!")
        elif s == 2:
            st.info(f"👍 Жақсы! {s}/3 — жетік болды!")
        else:
            st.warning(f"📚 {s}/3 — тағы да оқып шығыңыз")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;color:#334155;font-size:12px;margin-top:40px;padding-top:16px;
            border-top:1px solid #1e293b'>
  Этнохимиялық анықтамалық · Зертханалық жұмыс №2 · Виртуалды зертхана
</div>
""", unsafe_allow_html=True)
```

---

**Запуск:**

```bash
pip install streamlit
streamlit run app.py
```
