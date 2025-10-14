import streamlit as st
import random

# 🎵 English Mood-Based Songs Dataset
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
    "Romantic": [
        ("Ed Sheeran - Perfect", "https://youtu.be/2Vv-BfVoq4g"),
        ("John Legend - All Of Me", "https://youtu.be/450p7goxZqg"),
        ("Shawn Mendes - Señorita", "https://youtu.be/Pkh8UtuejGw"),
        ("Lauv - I Like Me Better", "https://youtu.be/BcqxLCWn-CE"),
        ("Jason Mraz - I'm Yours", "https://youtu.be/EkHTsc9PU2A"),
    ],
    "Chill": [
        ("Post Malone - Circles", "https://youtu.be/wXhTHyIgQ_U"),
        ("Coldplay - Paradise", "https://youtu.be/1G4isv_Fylg"),
        ("Ed Sheeran - Photograph", "https://youtu.be/nSDgHBxUbVQ"),
        ("Khalid - Better", "https://youtu.be/x3bfa3DZ8JM"),
        ("Maroon 5 - Memories", "https://youtu.be/SlPhMPnQ58k"),
    ],
}

# 🌈 Page Config
st.set_page_config(page_title="🎶 Mood Beats", page_icon="🎧", layout="wide")

# 💅 Custom CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .song-card {
        background-color: rgba(255,255,255,0.15);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .song-card:hover {
        transform: scale(1.05);
        background-color: rgba(255,255,255,0.25);
    }
    a {
        color: #FFD700;
        text-decoration: none;
        font-weight: 600;
    }
    a:hover {
        text-decoration: underline;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# 🎧 Title
st.markdown("<h1 style='text-align:center; color:white;'>🎶 Mood Beats - English Songs Recommender 🎧</h1>", unsafe_allow_html=True)
st.write("#### Feel the vibe 🎵 Choose your mood and explore top English hits!")

# 🌤️ Mood Selection
mood = st.selectbox("🎭 Select Your Mood:", list(songs.keys()))

if mood:
    st.markdown(f"### 💫 Songs for your **{mood}** mood:")
    selected_songs = songs[mood]
    random.shuffle(selected_songs)

    cols = st.columns(3)
    for i, (title, link) in enumerate(selected_songs):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='song-card'>
                <h4>{title}</h4>
                <a href='{link}' target='_blank'>▶️ Play on YouTube</a>
            </div>
            """, unsafe_allow_html=True)

# 🎉 Footer
st.markdown("<hr><center>🎵 Made with ❤️ by TechBro & Prem 🎧</center>", unsafe_allow_html=True)
