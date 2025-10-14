import streamlit as st
import random

# 🎵 English Mood-Based Songs
songs = {
    "Happy": [
        ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
        ("Justin Timberlake - Can't Stop The Feeling", "https://youtu.be/ru0K8uYEZWw"),
        ("Katy Perry - Roar", "https://youtu.be/CevxZvSJLk8"),
        ("Dua Lipa - Levitating", "https://youtu.be/TUVcZfQe-Kw"),
        ("Taylor Swift - Shake It Off", "https://youtu.be/nfWlot6h_JM"),
    ],
    "Sad": [
        ("Adele - Someone Like You", "https://youtu.be/hLQl3WQQoQ0"),
        ("Lewis Capaldi - Someone You Loved", "https://youtu.be/zABLecsR5UE"),
        ("Billie Eilish - When The Party’s Over", "https://youtu.be/pbMwTqkKSps"),
        ("Coldplay - The Scientist", "https://youtu.be/RB-RcX5DS5A"),
        ("Sam Smith - Too Good At Goodbyes", "https://youtu.be/J_ub7Etch2U"),
    ],
    "Energetic": [
        ("Imagine Dragons - Believer", "https://youtu.be/7wtfhZwyrcc"),
        ("Eminem - Lose Yourself", "https://youtu.be/_Yhyp-_hX2s"),
        ("Linkin Park - Numb", "https://youtu.be/kXYiU_JCYtU"),
        ("The Weeknd - Blinding Lights", "https://youtu.be/fHI8X4OXluQ"),
        ("Queen - Don’t Stop Me Now", "https://youtu.be/HgzGwKwLmgM"),
    ],
    "Chill": [
        ("Post Malone - Circles", "https://youtu.be/wXhTHyIgQ_U"),
        ("Coldplay - Paradise", "https://youtu.be/1G4isv_Fylg"),
        ("Ed Sheeran - Photograph", "https://youtu.be/nSDgHBxUbVQ"),
        ("Khalid - Better", "https://youtu.be/x3bfa3DZ8JM"),
        ("Maroon 5 - Memories", "https://youtu.be/SlPhMPnQ58k"),
    ],
}

# 🎨 Define a background color for each mood
mood_colors = {
    "Happy": "#FFD700",      # gold
    "Sad": "#1E90FF",        # dodger blue
    "Energetic": "#FF4500",  # orange red
    "Chill": "#32CD32",      # lime green
}

# 🌈 Page Setup
st.set_page_config(page_title="Mood Beats", page_icon="🎧", layout="centered")

# 🎶 App Title
st.markdown("<h1 style='text-align:center;'>🎵 Mood Beats 🎵</h1>", unsafe_allow_html=True)
st.write("Select your current mood and get a perfect English song recommendation!")

# 🎭 Mood Selection
mood = st.selectbox("Choose your mood:", list(songs.keys()))

# 🎨 Change page background dynamically based on mood
if mood:
    color = mood_colors.get(mood, "#FFFFFF")
    st.markdown(f"""
        <style>
            body {{
                background-color: {color};
                color: #111;
                font-family: 'Poppins', sans-serif;
            }}
            .song-card {{
                background: rgba(255,255,255,0.2);
                border-radius: 15px;
                padding: 20px;
                margin-top: 20px;
                text-align: center;
                box-shadow: 0 6px 20px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }}
            .song-card:hover {{
                transform: scale(1.05);
                background: rgba(255,255,255,0.35);
            }}
            a {{
                color: #111;
                font-weight: bold;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    """, unsafe_allow_html=True)

# 🕹️ Recommend Button
if st.button("Recommend a Song 🎧"):
    if mood:
        song = random.choice(songs[mood])
        st.markdown(f"""
            <div class='song-card'>
                <h2>{song[0]}</h2>
                <a href='{song[1]}' target='_blank'>▶️ Watch on YouTube</a>
            </div>
        """, unsafe_allow_html=True)
