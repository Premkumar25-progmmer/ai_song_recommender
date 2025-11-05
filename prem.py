# prem_music_vibe.py
import random
import streamlit as st
import urllib.parse

# -------------------------
# Simple song database
# Each entry: (title, artist, youtube_url, language, mood_tag)
# mood_tag should match one of the moods below.
# Replace/expand links with your preferred YouTube URLs.
# -------------------------
SONGS = [
    ("Maamam", "Artist A", "https://www.youtube.com/watch?v=example_maamam", "Telugu", "Relaxed"),
    ("Rowdy Baby", "Dhanush & Dhee", "https://www.youtube.com/watch?v=xRvB7pM3K0A", "Tamil", "Energetic"),
    ("Naatu Naatu", "Rahul Sipligunj, Kaala Bhairava", "https://www.youtube.com/watch?v=example_naatu", "Telugu", "Energetic"),
    ("Butta Bomma", "Armaan Malik", "https://www.youtube.com/watch?v=XYz2F8z4sVk", "Telugu", "Romantic"),
    ("Samajavaragamana", "Sid Sriram", "https://www.youtube.com/watch?v=KQmnn2ZsXJ4", "Telugu", "Romantic"),
    ("Tum Hi Ho", "Arijit Singh", "https://www.youtube.com/watch?v=Umqb9KENgmk", "Hindi", "Sad"),
    ("Kal Ho Naa Ho", "Sonu Nigam", "https://www.youtube.com/watch?v=VYY4Y2c9k7o", "Hindi", "Romantic"),
    ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "English", "Happy"),
    ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0", "English", "Energetic"),
    ("Perfect", "Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "English", "Romantic"),
    ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "English", "Sad"),
    ("Let It Be", "The Beatles", "https://www.youtube.com/watch?v=QDYfEBY9NM4", "English", "Relaxed"),
    # add more songs as you like...
]

# -------------------------
# Mood definitions + gradient families (random pick inside family)
# -------------------------
MOODS = {
    "Happy": {
        "desc": "Bright & uplifting",
        "gradients": [
            "linear-gradient(135deg, #FFF59D 0%, #FFB74D 100%)",
            "linear-gradient(135deg, #FFEEAD 0%, #FF8A65 100%)",
            "linear-gradient(135deg, #FFF48F 0%, #FF7043 100%)"
        ]
    },
    "Sad": {
        "desc": "Calm & reflective",
        "gradients": [
            "linear-gradient(135deg, #89CFF0 0%, #6A5ACD 100%)",
            "linear-gradient(135deg, #A8C7FF 0%, #7B61FF 100%)",
            "linear-gradient(135deg, #8EBEF5 0%, #5D4B8A 100%)"
        ]
    },
    "Romantic": {
        "desc": "Warm & soft",
        "gradients": [
            "linear-gradient(135deg, #FFD1DC 0%, #FF8FA3 100%)",
            "linear-gradient(135deg, #FFC1E3 0%, #FF9AA2 100%)",
            "linear-gradient(135deg, #FFE0F0 0%, #FF6B9A 100%)"
        ]
    },
    "Energetic": {
        "desc": "Pumping & dynamic",
        "gradients": [
            "linear-gradient(135deg, #FF7E5F 0%, #FEB47B 100%)",
            "linear-gradient(135deg, #FF6A88 0%, #FF9A9E 100%)",
            "linear-gradient(135deg, #7CFFB2 0%, #00E5FF 100%)"
        ]
    },
    "Relaxed": {
        "desc": "Chill & mellow",
        "gradients": [
            "linear-gradient(135deg, #C7F9CC 0%, #7AE3D6 100%)",
            "linear-gradient(135deg, #D0F2EA 0%, #A1E3DA 100%)",
            "linear-gradient(135deg, #E0FFEF 0%, #9FE6D8 100%)"
        ]
    }
}

DEFAULT_GRADIENT = "linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%)"

# -------------------------
# UI Setup
# -------------------------
st.set_page_config(page_title="Prem's Mood Music 🎶", page_icon="🎧", layout="centered")

# session defaults
if "last_song" not in st.session_state:
    st.session_state["last_song"] = None

st.markdown("""
<h1 style="text-align:center; margin-bottom:6px;">🎶 Prem's Mood Music</h1>
<p style="text-align:center; color: #333; margin-top:0;">Select a mood & language(s). App will pick a matching song and set the vibe 🎨</p>
""", unsafe_allow_html=True)

st.markdown("---")

# language multiselect with flags (attractive)
LANG_OPTIONS = [
    "🇮🇳 Telugu",
    "🇮🇳 Hindi",
    "🇬🇧 English",
    "🇮🇳 Tamil"
]
# default select all
selected_languages = st.multiselect("Choose language(s) (multiselect):", options=LANG_OPTIONS, default=LANG_OPTIONS)

# map displayed label back to actual language string present in SONGS
label_to_lang = {
    "🇮🇳 Telugu": "Telugu",
    "🇮🇳 Hindi": "Hindi",
    "🇬🇧 English": "English",
    "🇮🇳 Tamil": "Tamil"
}
selected_lang_vals = [label_to_lang[l] for l in selected_languages] if selected_languages else []

st.write("")  # spacing

# Mood selector (manual)
mood_choice = st.selectbox("Select Mood:", options=list(MOODS.keys()), index=0, help="Pick how you want to feel right now.")

# Remix style (optional)
REMIX_STYLES = ["Original Vibe", "Acoustic Cover", "Lo-Fi Slowed", "8-bit/Chiptune", "Dubstep Drop", "Orchestral Sweep", "Reggaeton Bounce"]
remix_choice = st.selectbox("Remix Style (simulated):", REMIX_STYLES)

# Show player checkbox
show_player = st.checkbox("Show YouTube Player", value=True)

st.markdown("---")

# Generate button
if st.button("Find me a song 🎧", use_container_width=True):
    # filter songs by languages and mood
    candidates = [s for s in SONGS if s[3] in selected_lang_vals and s[4] == mood_choice]
    if not candidates:
        st.warning("No songs found for that mood + language combination. Try selecting more languages or a different mood.")
    else:
        song = random.choice(candidates)
        st.session_state["last_song"] = {
            "title": song[0],
            "artist": song[1],
            "url": song[2],
            "language": song[3],
            "mood": song[4],
            "remix": remix_choice
        }

# if a recommendation exists, display it
rec = st.session_state.get("last_song")
if rec:
    # choose a random gradient from the mood family
    mood = rec["mood"]
    gradient_list = MOODS.get(mood, {}).get("gradients", [DEFAULT_GRADIENT])
    active_gradient = random.choice(gradient_list)

    # render dynamic CSS to change background
    st.markdown(f"""
    <style>
    .stApp {{
        background: {active_gradient};
        font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
        color: #111;
        padding-top: 18px;
    }}
    .pill-lang .css-1w0ym84 {{ /* selectbox label area hack for spacing on some Streamlit versions */ padding-top: 6px; }}
    /* Fancy pill buttons for external links */
    .link-pill {{
        background: rgba(255,255,255,0.9);
        border-radius: 12px;
        display: inline-block;
        padding: 10px 14px;
        font-weight:700;
        color: #111;
        text-decoration: none;
        margin:6px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }}
    .small-note {{ color: #111; opacity:0.9; font-size:13px; }}
