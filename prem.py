import random
import streamlit as st
import urllib.parse

# --- SONG DATA ---
songs_data = {
    "Happy": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "Pop/Funk"),
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0", "Dance/Funk"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw", "Pop"),
        ("Shake It Off", "Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM", "Pop"),
        ("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=vuq-VAiW9kw", "R&B/Soul"),
        ("Lovely Day", "Bill Withers", "https://www.youtube.com/watch?v=bO0yXbJd2iQ", "Soul/Classic"),
        ("I Wanna Dance with Somebody", "Whitney Houston", "https://www.youtube.com/watch?v=eH3giaIzONA", "80s Pop")
    ],
    "Sad": [
        ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "Ballad"),
        ("Let Her Go", "Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA", "Acoustic"),
        ("When I Was Your Man", "Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4", "Ballad"),
        ("Hello", "Adele", "https://www.youtube.com/watch?v=YQHsXMglC9A", "Soul"),
        ("Hurt", "Johnny Cash", "https://www.youtube.com/watch?v=vt1P_0f5w9g", "Acoustic"),
        ("Fix You", "Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM", "Rock")
    ],
    "Relaxed": [
        ("Let It Be", "The Beatles", "https://www.youtube.com/watch?v=QDYfEBY9NM4", "Classic Rock"),
        ("Perfect", "Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "Acoustic Pop"),
        ("Lovely", "Billie Eilish & Khalid", "https://www.youtube.com/watch?v=V1Pl8CzNzCw", "Atmospheric"),
        ("Sunflower", "Post Malone & Swae Lee", "https://www.youtube.com/watch?v=ApXoWvfEYVU", "Hip-Hop/Chill"),
        ("Let Me Down Slowly", "Alec Benjamin", "https://www.youtube.com/watch?v=50VNCymT-Cs", "Acoustic Pop"),
        ("A Thousand Years", "Christina Perry", "https://www.youtube.com/watch?v=rtOvBOTyX00", "Ballad")
    ],
    "Energetic": [
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc", "Rock"),
        ("Thunder", "Imagine Dragons", "https://www.youtube.com/watch?v=fKopy74weus", "Pop/Rock"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "Hip-Hop"),
        ("Don't Start Now", "Dua Lipa", "https://www.youtube.com/watch?v=oygrmJFKYZY", "Dance/Pop"),
        ("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg", "EDM")
    ]
}

REMIX_STYLES = [
    "Original Vibe", "Acoustic Cover", "8-bit/Chiptune", 
    "Dubstep Drop", "Lo-Fi Slowed", "Orchestral Sweep", "Reggaeton Bounce"
]

def generate_remix_description(song_title, remix_style):
    desc = {
        "Original Vibe": f"The original '{song_title}' stays true to your current mood!",
        "Acoustic Cover": f"'{song_title}' turned mellow — just vocals and guitar strings.",
        "8-bit/Chiptune": f"Retro vibes! '{song_title}' as if it’s from a GameBoy!",
        "Dubstep Drop": f"'{song_title}' remixed with thunderous drops and bass power.",
        "Lo-Fi Slowed": f"A rainy-day version of '{song_title}' — calm and nostalgic.",
        "Orchestral Sweep": f"'{song_title}' turned cinematic with violins and emotion.",
        "Reggaeton Bounce": f"'{song_title}' gets a Latin groove you can’t resist dancing to!"
    }
    return desc.get(remix_style, "A fresh remix take!")

# Page Config
st.set_page_config(page_title="AI Music Mood Generator 🎵", page_icon="🎧", layout="centered")

# Session setup
if 'current_mood' not in st.session_state:
    st.session_state['current_mood'] = 'Happy'
if 'selected_genre' not in st.session_state:
    st.session_state['selected_genre'] = 'Any Genre'
if 'selected_remix_style' not in st.session_state:
    st.session_state['selected_remix_style'] = 'Original Vibe'
if 'show_player' not in st.session_state:
    st.session_state['show_player'] = False

# --- APP TITLE ---
st.markdown("""
<h1 style='text-align:center; color:#FF4081;'>🎶 AI Mood Music Generator</h1>
<p style='text-align:center; font-size:18px; color:#444;'>Find your perfect song & remix for your current vibe!</p>
""", unsafe_allow_html=True)

# --- FILTER SECTION ---
st.markdown("### 🎧 Select Your Mood")

col_mood, col_genre = st.columns(2)

with col_mood:
    mood_choice = st.selectbox("Mood:", list(songs_data.keys()), index=list(songs_data.keys()).index(st.session_state['current_mood']))
with col_genre:
    genres = sorted(list(set(song[3] for song in songs_data[mood_choice])))
    genre_choice = st.selectbox("Genre:", ["Any Genre"] + genres)

st.markdown("---")

# Remix style
remix_style_choice = st.selectbox("Remix Style:", REMIX_STYLES)

# Toggle Player
st.session_state['show_player'] = st.toggle("Show YouTube Player", value=st.session_state['show_player'])

# --- BUTTON ---
if st.button("Generate My Song ✨", use_container_width=True):
    songs = songs_data[mood_choice]
    if genre_choice != "Any Genre":
        songs = [s for s in songs if s[3] == genre_choice]
    song = random.choice(songs)
    title, artist, url, genre = song

    remix_desc = generate_remix_description(title, remix_style_choice)

    st.success(f"**{mood_choice.upper()} Vibe Activated!**")
    st.markdown(f"<h2 style='text-align:center;color:#222;'>🎵 {title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center;color:#555;'>by <b>{artist}</b></h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#444; font-style:italic;'>{remix_desc}</p>", unsafe_allow_html=True)

    if st.session_state['show_player']:
        st.video(url)
    
    spotify_query = urllib.parse.quote_plus(f"{title} {artist}")
    spotify_url = f"https://open.spotify.com/search/{spotify_query}"

    col1, col2 = st.columns(2)
    with col1:
        st.link_button("▶️ Open on YouTube", url)
    with col2:
        st.link_button("🎧 Open on Spotify", spotify_url)

# --- FOOTER ---
st.markdown("""
<hr>
<div style='text-align:center; font-size:14px; color:#333;'>
Developed with ❤️ by <b>Chilkamarri Prem Kumar (TechBro)</b><br>
Vignan Institute of Technology and Science, Hyderabad
</div>
""", unsafe_allow_html=True)

# --- STYLING (Colorful Gradient Theme) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    font-family: 'Poppins', sans-serif;
    color: #222;
}
div[data-testid="stSelectbox"] label {
    color: #111;
    font-weight: 600;
}
div.stButton > button {
    background: linear-gradient(90deg, #FF4081, #81D4FA);
    color: white;
    border-radius: 10px;
    border: none;
    height: 3em;
    font-size: 1.1em;
    font-weight: bold;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.stSuccess {
    background: #E1F5FE;
    border-left: 5px solid #FF4081;
    color: #111;
    font-weight: 600;
    border-radius: 6px;
}
hr {
    border: none;
    height: 2px;
    background: linear-gradient(to right, #FF4081, #81D4FA);
}
</style>
""", unsafe_allow_html=True)
