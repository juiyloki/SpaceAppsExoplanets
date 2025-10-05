import streamlit as st
import numpy as np
import base64

def add_cosmic_background(animated_stars: int = 0, meteors_count: int = 5, planet_path: str = "frontend/pictures/planet.png"):
    """
    Dodaje kosmiczne tło z animowanymi gwiazdami, planetą i lecącymi meteorytami.
    Meteoryty są większe i poruszają się wolniej.
    :param animated_stars: liczba gwiazd
    :param meteors_count: liczba meteorytów
    :param planet_path: ścieżka do lokalnej planety
    """
    # Zakoduj planetę do base64
    with open(planet_path, "rb") as f:
        planet_base64 = base64.b64encode(f.read()).decode()

    # Gwiazdy
    stars_html = ""
    for i in range(animated_stars):
        left = f"{np.random.randint(0, 100)}%"
        top = f"{np.random.randint(0, 100)}%"
        size = f"{np.random.randint(1, 4)}px"
        duration = f"{np.random.uniform(2, 6)}s"
        stars_html += f"""
        <div class="star" style="
            left: {left};
            top: {top};
            width: {size};
            height: {size};
            animation-duration: {duration};
        "></div>
        """

    # Meteoryty (większe i wolniejsze)
    meteors_html = ""
    for i in range(meteors_count):
        start_left = np.random.randint(-20, 100)
        start_top = np.random.randint(-20, 0)
        size = np.random.randint(15, 30)  # większe meteoryty
        duration = np.random.uniform(8, 15)  # wolniejsza animacja
        delay = np.random.uniform(0, 5)
        meteors_html += f"""
        <div class="meteor" style="
            left: {start_left}%;
            top: {start_top}%;
            width: {size}px;
            height: {size/4}px;
            animation-duration: {duration}s;
            animation-delay: {delay}s;
        "></div>
        """

    # Wyświetlenie wszystkiego
    st.markdown(f"""
        <style>
        /* Tło kosmiczne */
        .stApp {{
            background-image: url('https://images.unsplash.com/photo-1581092334310-4b70ebdb4f1b?auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-attachment: fixed;
        }}

        @keyframes twinkle {{
            0% {{ transform: translateY(0px); opacity: 0.5; }}
            50% {{ transform: translateY(-5px); opacity: 1; }}
            100% {{ transform: translateY(0px); opacity: 0.5; }}
        }}

        /* Planeta poruszająca się po ekranie */
        .planet {{
            position: fixed;
            bottom: 10%;
            right: 5%;
            width: 200px;
            animation: orbit 10s linear infinite;
            z-index: 10;
        }}

        @keyframes orbit {{
            0% {{ transform: rotate(0deg) translateX(0px) rotate(0deg); }}
            50% {{ transform: rotate(180deg) translateX(-30px) rotate(-180deg); }}
            100% {{ transform: rotate(360deg) translateX(0px) rotate(-360deg); }}
        }}

        /* Meteoryty lecące po ekranie */
        .meteor {{
            position: fixed;
            background: linear-gradient(45deg, #fff, #aaa);
            border-radius: 50%;
            transform: rotate(45deg);
            animation-name: shoot;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
        }}

        @keyframes shoot {{
            0% {{ transform: translate(0, 0) rotate(45deg); opacity: 1; }}
            100% {{ transform: translate(-150vw, 150vh) rotate(45deg); opacity: 0; }}
        }}
        </style>

        {stars_html}

        {meteors_html}

        <div class="planet">
            <img src="data:image/webp;base64,{planet_base64}" width="100px"/>
        </div>
    """, unsafe_allow_html=True)
