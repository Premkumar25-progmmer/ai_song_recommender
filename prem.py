import random
import streamlit as st

# 🎵 Mood-to-song mapping (only English songs, all working YouTube links)
songs = {
    "Happy": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Shake It Off", "Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM"),
        ("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=vuq-VAiW9kw"),
        ("Happy Now", "Kygo & Sandro Cavazza", "https://www.youtube.com/watch?v=f7LDspHg8EU")
    ],
    "Sad": [
        ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go", "Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("When I Was Your Man", "Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4"),
        ("Fix You", "Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("Lose You To Love Me", "Selena Gomez", "https://www.youtube.com/watch?v=zlJDTxahav0"),
        ("All I Want", "Kodaline", "https://www.youtube.com/watch?v=mtf7hC17IBM")
    ],
    "Relaxed": [
        ("Let It Be", "The Beatles", "https://www.youtube.com/watch?v=QDYfEBY9NM4"),
        ("Perfect", "Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g"),
        ("Lovely", "Billie Eilish & Khalid", "https://www.youtube.com/watch?v=V1Pl8CzNzCw"),
        ("Ocean Eyes", "Billie Eilish", "https://www.youtube.com/watch?v=viimfQi_pUw"),
        ("Sunflower", "Post Malone & Swae Lee", "https://www.youtube.com/watch?v=ApXoWvfEYVU"),
        ("Let Me Down Slowly", "Alec Benjamin", "https://www.youtube.com/watch?v=50VNCymT-Cs")
    ],
    "Energetic": [
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Thunder", "Imagine Dragons", "https://www.youtube.com/watch?v=fKopy74weus"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Don't Start Now", "Dua Lipa", "https://www.youtube.com/watch?v=oygrmJFKYZY"),
        ("Can't Hold Us", "Macklemore & Ryan Lewis", "https://www.youtube.com/watch?v=2zNSgSzhBfM"),
        ("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg")
    ]
}

# 🎧 Streamlit Page Setup
st.set_page_config(page_title="Mood-Based Song Recommender", page_icon="🎵", layout="centered")

st.title("🎶 Mood-Based Song Recommender")
st.write("Select your current mood and get a perfect English song recommendation! 🎧")

# 🎭 Mood selection
mood_choice = st.selectbox("Choose your mood:", list(songs.keys()))

# 🕹️ Recommend button
if st.button("Recommend Song 🎵"):
    if mood_choice:
        song = random.choice(songs[mood_choice])
        st.success(f"**🎧 '{song[0]}'** by *{song[1]}* — perfect for your {mood_choice.lower()} mood!")
        st.markdown(f"[▶️ Watch on YouTube]({song[2]})", unsafe_allow_html=True)
    else:
        st.warning("Please select a mood first!")

# 🌈 Styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #c3ec52, #0ba29d);
        color: #111;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #111;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 12em;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #333;
        color: #00ffcc;
    }
</style>
""", unsafe_allow_html=True)
