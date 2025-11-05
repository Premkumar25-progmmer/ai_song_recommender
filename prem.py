import streamlit as st
import random

# -----------------------------
# 🎵 SONG DATABASE (100 per mood sample)
# -----------------------------
# For demonstration, using 10 songs each; you can expand to 100 easily
songs_db = {
    "Happy": [
        ("Happy Song 1", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        ("Happy Song 2", "https://www.youtube.com/watch?v=3GwjfUFyY6M"),
        ("Happy Song 3", "https://www.youtube.com/watch?v=oHg5SJYRHA0"),
        ("Happy Song 4", "https://www.youtube.com/watch?v=MtN1YnoL46Q"),
        ("Happy Song 5", "https://www.youtube.com/watch?v=ZZ5LpwO-An4"),
        ("Happy Song 6", "https://www.youtube.com/watch?v=6_b7RDuLwcI"),
        ("Happy Song 7", "https://www.youtube.com/watch?v=L_jWHffIx5E"),
        ("Happy Song 8", "https://www.youtube.com/watch?v=kJQP7kiw5Fk"),
        ("Happy Song 9", "https://www.youtube.com/watch?v=fLexgOxsZu0"),
        ("Happy Song 10", "https://www.youtube.com/watch?v=CevxZvSJLk8")
    ],
    "Sad": [
        ("Sad Song 1", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Sad Song 2", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Sad Song 3", "https://www.youtube.com/watch?v=ekzHIouo8Q4"),
        ("Sad Song 4", "https://www.youtube.com/watch?v=YQHsXMglC9A"),
        ("Sad Song 5", "https://www.youtube.com/watch?v=vt1P_0f5w9g"),
        ("Sad Song 6", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("Sad Song 7", "https://www.youtube.com/watch?v=5qap5aO4i9A"),
        ("Sad Song 8", "https://www.youtube.com/watch?v=AN3JZ0kCzxY"),
        ("Sad Song 9", "https://www.youtube.com/watch?v=hoNBkIbhvLQ"),
        ("Sad Song 10", "https://www.youtube.com/watch?v=C3U77QFsjU0")
    ],
    "Energetic": [
        ("Energetic Song 1", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Energetic Song 2", "https://www.youtube.com/watch?v=fKopy74weus"),
        ("Energetic Song 3", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Energetic Song 4", "https://www.youtube.com/watch?v=oygrmJFKYZY"),
        ("Energetic Song 5", "https://www.youtube.com/watch?v=2zNSgSzhBfM"),
        ("Energetic Song 6", "https://www.youtube.com/watch?v=JRfuAukYTKg"),
        ("Energetic Song 7", "https://www.youtube.com/watch?v=kJQP7kiw5Fk"),
        ("Energetic Song 8", "https://www.youtube.com/watch?v=fLexgOxsZu0"),
        ("Energetic Song 9", "https://www.youtube.com/watch?v=CevxZvSJLk8"),
        ("Energetic Song 10", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ],
    "Romantic": [
        ("Romantic Song 1", "https://www.youtube.com/watch?v=3vLm-Lwibx0"),
        ("Romantic Song 2", "https://www.youtube.com/watch?v=1J76wN0TPI4"),
        ("Romantic Song 3", "https://www.youtube.com/watch?v=yIw2Y6sONJU"),
        ("Romantic Song 4", "https://www.youtube.com/watch?v=Umqb9KENgmk"),
        ("Romantic Song 5", "https://www.youtube.com/watch?v=Q8q0vFjzv-8"),
        ("Romantic Song 6", "https://www.youtube.com/watch?v=3yYw2e4aGGE"),
        ("Romantic Song 7", "https://www.youtube.com/watch?v=kGiOytZtJmE"),
        ("Romantic Song 8", "https://www.youtube.com/watch?v=5O9q8IPlu6U"),
        ("Romantic Song 9", "https://www.youtube.com/watch?v=Zp9HUcFZ6N8"),
        ("Romantic Song 10", "https://www.youtube.com/watch?v=qzOeGW1gWVQ")
    ]
}

# -----------------------------
# 🌈 Mood Colors
# -----------------------------
mood_colors = {
    "Happy": "#FFD700",
    "Sad": "#4B0082",
    "Energetic": "#FF4500",
    "Romantic": "#FF69B4"
}

# -----------------------------
# STREAMLIT APP
# -----------------------------
st.set_page_config(page_title="Play It Bro 🎶", page_icon="🎵", layout="centered")

st.markdown(f"<h1 style='text-align:center; color:{mood_colors['Happy']}'>🎶 Play It Bro - Mood Based Songs 🎵</h1>", unsafe_allow_html=True)
st.write("Select your mood and get a random hit song!")

# Mood selection
mood = st.radio("Select your mood:", list(songs_db.keys()), horizontal=True)

# Recommend button
if st.button("🎧 Recommend Me a Song"):
    selected_song = random.choice(songs_db[mood])
    song_name, song_link = selected_song
    
    st.markdown(f"### 🎵 {song_name}")
    st.markdown(f"[Open on YouTube]({song_link})")
    
    # Embed video
    st.video(song_link)

st.markdown("<hr><p style='text-align:center;'>Built with ❤️ by Prem Kumar</p>", unsafe_allow_html=True)
