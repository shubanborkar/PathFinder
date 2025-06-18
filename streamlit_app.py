import streamlit as st
from agent import CareerPathwayAgent
from langchain_mistralai.chat_models import ChatMistralAI

# Branding assets
LOGO_URL = "https://cdn-icons-png.flaticon.com/512/3135/3135768.png"
FAVICON_URL = "https://cdn-icons-png.flaticon.com/512/3135/3135768.png"
BRAND_NAME = "PathFinder AI"
BRAND_COLOR = "#4F8BF9"

st.set_page_config(
    page_title=f"{BRAND_NAME} - Student Career Pathway Recommender",
    page_icon=FAVICON_URL,
    layout="wide"
)

# --- Session state and reset logic ---
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = ""
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""
if 'reset' not in st.session_state:
    st.session_state['reset'] = False
if 'step' not in st.session_state:
    st.session_state['step'] = 1

if st.session_state['reset']:
    st.session_state['conversation'] = ""
    st.session_state['user_input'] = ""
    st.session_state['step'] = 1
    st.session_state['reset'] = False

# --- Custom CSS for modern, clean look (no glass-card) ---
st.markdown(f"""
    <style>
    body, .stApp {{
        background: linear-gradient(120deg, #232936 0%, #181c24 100%) !important;
        color: #e0e6f0 !important;
        font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
    }}
    .floating-label {{
        position: absolute;
        left: 0.5em;
        top: 0.7em;
        color: #b0b8c9;
        font-size: 1.08em;
        pointer-events: none;
        transition: 0.2s;
        z-index: 2;
    }}
    .input-focused .floating-label,
    .input-has-value .floating-label {{
        top: -1.1em;
        left: 0.5em;
        font-size: 0.98em;
        color: {BRAND_COLOR};
        font-weight: 600;
    }}
    .stTextArea textarea {{
        background: #232936 !important;
        color: #e0e6f0 !important;
        border-radius: 10px !important;
        border: 1.5px solid #31384a !important;
        font-size: 1.13em;
        min-height: 110px !important;
        box-shadow: none !important;
    }}
    .glass-btn {{
        width: 100%;
        background: linear-gradient(90deg, #4F8BF9 60%, #2563eb 100%);
        color: #fff;
        border: none;
        border-radius: 10px;
        font-size: 1.18em;
        font-weight: 700;
        padding: 0.85em 0;
        margin-top: 1.2em;
        margin-bottom: 0.5em;
        box-shadow: 0 2px 8px 0 #00000020;
        transition: background 0.2s;
    }}
    .glass-btn:hover {{
        background: linear-gradient(90deg, #2563eb 60%, #4F8BF9 100%);
    }}
    .result-section {{
        margin-top: 2.2em;
        margin-bottom: 1.2em;
        padding: 1.5em 1.2em 1.2em 1.2em;
        background: rgba(232,240,254,0.13);
        border-radius: 14px;
        box-shadow: 0 2px 12px 0 #00000018;
        animation: fadeIn 0.8s;
    }}
    .result-title {{
        font-size: 1.35em;
        font-weight: 700;
        color: {BRAND_COLOR};
        margin-bottom: 0.7em;
        display: flex;
        align-items: center;
        gap: 0.5em;
    }}
    .result-icon {{
        font-size: 1.3em;
        vertical-align: middle;
    }}
    .result-expl {{
        margin-top: 1.2em;
        padding: 1em 1em 0.5em 1em;
        background: rgba(249,249,249,0.13);
        border-radius: 10px;
        color: #e0e6f0;
        font-size: 1.07em;
    }}
    @media (max-width: 700px) {{
        .stTextArea textarea {{
            font-size: 1em;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar with logo and instructions
st.sidebar.image(LOGO_URL, width=70)
st.sidebar.markdown(f"<h2 style='color:{BRAND_COLOR};margin-bottom:0;'>{BRAND_NAME}</h2>", unsafe_allow_html=True)
st.sidebar.markdown(
    f"""
    <div style='margin-bottom:1.2em;'></div>
    <div style='font-size:1.08em; font-weight:600; margin-bottom:0.5em;'>Instructions</div>
    <ul style='margin-left:-1em; margin-bottom:1.2em; color:#e0e6f0;'>
      <li style='margin-bottom:0.5em;'>Enter your <b>interests</b>, <b>hobbies</b>, and <b>academic strengths</b> below.</li>
      <li style='margin-bottom:0.5em;'>Click <b>Get Recommendations</b>.</li>
    </ul>
    <div style='margin-top:1.5em; margin-bottom:0.5em; text-align:left;'>
      <span style='background:#232936; color:#4F8BF9; border-radius:6px; padding:4px 10px; font-size:0.98em; font-weight:600; display:inline-block;'>🚀 Powered by Mistral AI</span>
    </div>
    """,
    unsafe_allow_html=True
)
if st.sidebar.button("Reset All", use_container_width=True):
    st.session_state['reset'] = True
    st.experimental_rerun()

# Large, prominent header and tagline (centered, bold)
st.markdown(
    f"""
    <div style='text-align:center; margin-top:1.5em; margin-bottom:1.2em;'>
        <span style='font-size:2.7em; font-weight:900; color:{BRAND_COLOR}; display:block; font-family:inherit;'>
            PathFinder AI 🧪
        </span>
        <span style='font-size:1.35em; font-weight:700; color:#b0b8c9; display:block; margin-top:0.3em;'>
            Discover your ideal career path with the power of AI.
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

agent = CareerPathwayAgent(llm=ChatMistralAI(temperature=0.3))

# --- Clean, modern right-hand side (main content) ---
with st.container():
    user_input = st.text_area(
        "",  # No label
        height=110,
        key='user_input',
        placeholder="Describe your interests, hobbies, and academic strengths..."
    )
    recommend_btn = st.button("🔎 Get Recommendations", key='recommend_btn', use_container_width=True, help="Get personalized career path suggestions")

    if recommend_btn:
        with st.spinner('Generating your personalized career path recommendations...'):
            st.session_state['conversation'] += f"Student: {st.session_state['user_input']}\n"
            st.markdown("<div class='result-section'>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-title'><span class='result-icon'>🎓</span> Recommendations</div>", unsafe_allow_html=True)
            response = agent.recommend_paths(st.session_state['conversation'])
            st.markdown(
                f"""<div class='fade-in' style='background-color:#e8f0fe;
                padding:15px;
                border-radius:8px;
                color:#1a1a1a;
                font-size:1.08em;
                font-weight:500;
                line-height:1.6;'>
                {response}
                </div>""",
                unsafe_allow_html=True
            )
            explanations = agent.get_cluster_explanations(st.session_state['conversation'])
            if explanations:
                st.markdown(f"<div class='result-title' style='margin-top:1.5em;'><span class='result-icon'>💡</span> Career Path Explanations</div>", unsafe_allow_html=True)
                for cluster, expl in explanations.items():
                    st.markdown(
                        f"""<div class='result-expl fade-in'>
                        <b>{cluster}</b>: {expl}
                        </div>""",
                        unsafe_allow_html=True
                    )
            st.markdown("</div>", unsafe_allow_html=True)

# Footer with copyright
st.markdown(
    f"""
    <hr style='margin-top:40px;margin-bottom:10px;border:1px solid {BRAND_COLOR};'>
    <div style='text-align:center;color:#7a7f8a;font-size:0.85em;'>
        &copy; 2024 PathFinder AI — Crafted with ❤️ by Shuban Borkar
    </div>
    """, unsafe_allow_html=True
) 