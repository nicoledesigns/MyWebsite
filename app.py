import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# ------------------------
# Page config
# ------------------------
st.set_page_config(
    page_title="Nicole Antoun | Portfolio",
    page_icon="✨",
    layout="wide"
)

# ------------------------
# Load CSS
# ------------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ------------------------
# Load Lottie
# ------------------------
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie_welcome = load_lottieurl(
    "https://lottie.host/d4118a51-82ae-4e7d-8135-a3c4974dffdd/3nDtWjEIrX.json"
)

# ------------------------
# Load Images
# ------------------------
img_pet = Image.open("images/pet.png")
img_bible = Image.open("images/bibleapp.png")
img_chat = Image.open("images/chat.png")
img_ml = Image.open("images/ML.png")
img_portfolio = Image.open("images/project.png")

# ------------------------
# Language toggle
# ------------------------
lang = st.radio(
    "Language / Langue",
    ["English", "Français"],
    horizontal=True
)

is_en = lang == "English"

# ------------------------
# Text content
# ------------------------
title = "Welcome to My Portfolio 👋" if is_en else "Bienvenue sur mon Portfolio 👋"
about = (
    """
            I am a Software Engineering Student at Concordia University with strong skills in problem-solving, design, and full-stack development.  

            My goal is to transform technical knowledge into impactful, user-friendly solutions that help businesses grow.  

            I am highly motivated, quick to learn new technologies, and thrive in collaborative environments.
            ."""
    if is_en else
    "Je suis étudiante en génie logiciel à l’Université Concordia, passionnée par la création de solutions logicielles propres, intuitives et impactantes."
)

skills_title = "Core Skills" if is_en else "Compétences Clés"
projects_title = "Highlighted Projects" if is_en else "Projets Mis en Avant"
contact_title = "Get in Touch" if is_en else "Contactez-moi"

# ------------------------
# Welcome section
# ------------------------
with st.container():
    st.write("---")
    left, right = st.columns([2, 1])

    with left:
        st.title("Nicole Antoun")
        st.subheader(title)
        st.write(about)
        st.markdown("📄 [Resume](#)")
        st.markdown("💻 [GitHub](#)")

    with right:
        if lottie_welcome:
            st_lottie(lottie_welcome, height=350)

# ------------------------
# Skills
# ------------------------
with st.container():
    st.write("---")
    st.header(skills_title)
    st.markdown("""
    - **Full-Stack Development**
    - **Machine Learning**
    - **Problem Solving**
    - **Team Collaboration**
    - **Continuous Learning**
    """)

# ------------------------
# Projects (Carousel)
# ------------------------
projects = [
    {
        "img": img_pet,
        "title": {"en": "Pet Website", "fr": "Site web pour animaux"},
        "desc": {
            "en": "- 7-page responsive website built with HTML, CSS, and JavaScript\n- Designed for usability and aesthetics, earning a final grade of 97%",
            "fr": "- Site web responsive de 7 pages\n- Développé avec HTML, CSS et JavaScript\n- Conçu pour l’ergonomie et l’esthétique\n- Note finale : 97%"
        }
    },
    {
        "img": img_bible,
        "title": {"en": "Bible App", "fr": "Application biblique"},
        "desc": {
            "en": "- Flutter app for interactive Bible reading and reflection\n- Features: read and listen to Scripture, highlight verses, take notes, daily verses, prayer calendar, verse search\n- Biblical AI chat powered by gpt-4o-mini\n- Built with Flutter/Dart and tested on iOS simulators using Xcode",
            "fr": "- Application Flutter pour la lecture et la réflexion biblique interactives\n- Fonctionnalités : lecture et audio des Écritures, surlignage de versets, prise de notes, verset quotidien, calendrier de prière, recherche de versets\n- Chat biblique alimenté par l’IA\n- Développée avec Flutter/Dart et testée sur simulateur iOS via Xcode"
        }
    },
    {
        "img": img_chat,
        "title": {"en": "ChatHaven", "fr": "ChatHaven"},
        "desc": {
            "en": "- Full-stack communication platform focused on privacy, usability, and collaboration\n- Built with React, Express.js, and SQLite\n- Features group channels, private messaging, and media sharing\n- Developed using Agile methodology",
            "fr": "- Plateforme de communication full stack axée sur la confidentialité, l’ergonomie et la collaboration\n- Développée avec React, Express.js et SQLite\n- Fonctionnalités : canaux de groupe, messagerie privée et partage de médias\n- Réalisée selon la méthodologie Agile"
        }
    },
    {
        "img": img_ml,
        "title": {"en": "CIFAR-10 ML Pipeline", "fr": "Pipeline de classification CIFAR-10"},
        "desc": {
            "en": "- Image classification system for CIFAR-10 using Gaussian Naive Bayes, Decision Trees, MLPs, and VGG11 CNN\n- Implemented data pipelines, feature extraction, training, evaluation, and automated reports\n- Saved model weights and tracked performance metrics\n- Built with Python, NumPy, scikit-learn, PyTorch, and matplotlib in a team of three",
            "fr": "- Système de classification d’images CIFAR-10 utilisant Naive Bayes gaussien, arbres de décision, MLP et CNN VGG11\n- Mise en place de pipelines de données, extraction de caractéristiques, entraînement, évaluation et rapports automatisés\n- Sauvegarde des poids des modèles et suivi des métriques de performance\n- Réalisé avec Python, NumPy, scikit-learn, PyTorch et matplotlib au sein d’une équipe de trois personnes"
        }
    },
    {
        "img": img_portfolio,
        "title": {"en": "Portfolio Website", "fr": "Site portfolio"},
        "desc": {
            "en": "- Personal portfolio built using Streamlit, Python, and CSS\n- Interactive Lottie animations highlighting design and technical skills\n- Showcases responsive design, professional layout, and selected projects",
            "fr": "- Portfolio personnel développé avec Streamlit, Python et CSS\n- Animations Lottie interactives mettant en valeur les compétences techniques et de design\n- Présentation d’un design responsive, d’une mise en page professionnelle et de projets sélectionnés"
        }
    }
]


if "proj_idx" not in st.session_state:
    st.session_state.proj_idx = 0

with st.container():
    st.write("---")
    st.header(projects_title)

    # Navigation arrows
    left_arrow, _, right_arrow = st.columns([1, 6, 1])

    with left_arrow:
        if st.button("◀"):
            st.session_state.proj_idx = max(0, st.session_state.proj_idx - 1)

    with right_arrow:
        if st.button("▶"):
            st.session_state.proj_idx = min(len(projects) - 1, st.session_state.proj_idx + 1)

    project = projects[st.session_state.proj_idx]

    # Animated project display
    st.markdown('<div class="carousel-wrapper carousel-slide">', unsafe_allow_html=True)

    img_col, text_col = st.columns([1, 2])
    with img_col:
        st.image(project["img"], use_container_width=True)

    with text_col:
        st.subheader(project["title"]["en"] if is_en else project["title"]["fr"])
        st.write(project["desc"]["en"] if is_en else project["desc"]["fr"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Indicator dots
    dots = "".join("● " if i == st.session_state.proj_idx else "○ " for i in range(len(projects)))
    st.markdown(f"<p style='text-align:center;'>{dots}</p>", unsafe_allow_html=True)

# ------------------------
# Contact
# ------------------------
with st.container():
    st.write("---")
    st.header(contact_title)

    st.markdown("""
    <form action="https://formsubmit.co/YOUREMAIL@example.com" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message"></textarea>
        <button type="submit">Send</button>
    </form>
    """, unsafe_allow_html=True)
