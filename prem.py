import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="Play It Bro — Mood Music", page_icon="🎧", layout="centered")

# -------------------------
# Song database: only live YouTube links
# -------------------------
SONGS = [
    # Telugu
    ("Rowdy Baby", "Dhanush & Dhee", "https://www.youtube.com/watch?v=xRvB7pM3K0A", "Tamil", "Energetic"),
    ("Naatu Naatu", "Rahul Sipligunj, Kaala Bhairava", "https://www.youtube.com/watch?v=OsU0CGZoV8E", "Telugu", "Energetic"),
    ("Butta Bomma", "Armaan Malik", "https://www.youtube.com/watch?v=ksLZEepQ0nQ", "Telugu", "Romantic"),
    ("Samajavaragamana", "Sid Sriram", "https://www.youtube.com/watch?v=EJ6YlX3p0Rg", "Telugu", "Romantic"),
    ("Nee Kallu Neeli Samudram", "Javed Ali", "https://www.youtube.com/watch?v=J7d3Gm0X3R8", "Telugu", "Sad"),

    # Hindi
    ("Tum Hi Ho", "Arijit Singh", "https://www.youtube.com/watch?v=Umqb9KENgmk", "Hindi", "Sad"),
    ("Kal Ho Naa Ho", "Sonu Nigam", "https://www.youtube.com/watch?v=RhxF9Qg5mOU", "Hindi", "Romantic"),
    ("Malhari", "Vishal Dadlani", "https://www.youtube.com/watch?v=YxWlaYCA8MU", "Hindi", "Energetic"),
    ("Channa Mereya", "Arijit Singh", "https://www.youtube.com/watch?v=284Ov7ysmfA", "Hindi", "Sad"),

    # Tamil
    ("Vaathi Coming", "Anirudh Ravichander", "https://www.youtube.com/watch?v=MPV2METPeJU", "Tamil", "Energetic"),
    ("Enna Solla Pogirai", "Shankar Mahadevan", "https://www.youtube.com/watch?v=PL8PZkBwU3E", "Tamil", "Romantic"),
    ("Arabic Kuthu", "Anirudh Ravichander", "https://www.youtube.com/watch?v=Sa2jYn1LIVI", "Tamil", "Happy"),
]

# -------------------------
# Mood gradient families
# -------------------------
MOOD_GRADIENTS = {
    "Happy": [
        "linear-gradient(135deg, #FFF59D 0%, #FFB74D 100%)",
        "linear-gradient(135deg, #FFEEAD 0%, #FF8A65 100%)"
    ],
    "Sad": [
        "linear-gradient(135deg, #89CFF0 0%, #6A5ACD 100%)",
        "linear-gradient(135deg, #A8C7FF 0%, #7B61FF 100%)"
    ],
    "Romantic": [
        "linear-gradient(135deg, #FFD1DC 0%, #FF8FA3 100%)",
        "linear-gradient(135deg, #FFC1E3 0%, #FF9AA2 100%)"
    ],
    "Energetic": [
        "linear-gradient(135deg, #FF7E5F 0%, #FEB47B 100%)",
        "linear-gradient(135deg, #7CFFB2 0%, #00E5FF 100%)"
    ],
    "Relaxed": [
        "linear-gradient(135deg, #C7F9CC 0%, #7AE3D6 100%)",
        "linear-gradient(135deg, #D0F2EA 0%, #A1E3DA 100%)"
    ]
}
DEFAULT_GRADIENT = "linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%)"

# -------------------------
# Header
# -------------------------
st.markdown("""
    <div style="text-align:center;">
        <h1>🎶 Play It Bro — Mood Music</h1>
        <p style="color:#444;">Choose your mood and languages to get a real playable song!</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# Language and mood selection
# -------------------------
LANG_LABELS = ["🇮🇳 Telugu", "🇮🇳 Hindi", "🇮🇳 Tamil"]
label_to_lang = {
    "🇮🇳 Telugu": "Telugu",
    "🇮🇳 Hindi": "Hindi",
    "🇮🇳 Tamil": "Tamil"
}

selected_labels = st.multiselect(
    "Choose language(s):",
    options=LANG_LABELS,
    default=["🇮🇳 Telugu"]
)
selected_langs = [label_to_lang[l] for l in selected_labels]

mood_options = ["Happy", "Sad", "Romantic", "Energetic", "Relaxed"]
mood_choice = st.selectbox("Select Mood:", mood_options, index=0)

show_player = st.checkbox("Show YouTube Player", value=True)

st.markdown("---")

# -------------------------
# Song recommendation logic
# -------------------------
if st.button("Find me a song 🎧", use_container_width=True):
    candidates = [s for s in SONGS if s[3] in selected_langs and s[4] == mood_choice]
    if not candidates:
        st.warning("No songs found for this mood + language combination. Try other options.")
    else:
        song = random.choice(candidates)
        st.session_state["current_song"] = {
            "title": song[0],
            "artist": song[1],
            "url": song[2],
            "language": song[3],
            "mood": song[4]
        }

# -------------------------
# Display recommendation
# -------------------------
rec = st.session_state.get("current_song")
if rec:
    grad_list = MOOD_GRADIENTS.get(rec["mood"], [DEFAULT_GRADIENT])
    active_gradient = random.choice(grad_list)

    st.markdown(f"""
        <style>
        .stApp {{
            background: {active_gradient};
            font-family: 'Poppins', 'Segoe UI', sans-serif;
            color: #111;
        }}
        .pill-btn {{
            display:inline-block;
            padding:10px 14px;
            border-radius:12px;
            text-decoration:none;
            font-weight:700;
            margin:6px;
            color:#fff !important;
        }}
        .yt-pill {{ background: linear-gradient(90deg,#FF6A88,#FFA5C0); }}
        .sp-pill {{ background: linear-gradient(90deg,#6A11CB,#2575FC); }}
        .info-card {{
            background: rgba(255,255,255,0.95);
            padding:18px;
            border-radius:14px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.08);
        }}
        </style>
    """, unsafe_allow_html=True)

    st.success(f"✅ {rec['mood']} pick: {rec['title']} — {rec['artist']} ({rec['language']})")

    st.markdown(f"""
        <div class="info-card">
            <h2 style="text-align:center;">🎵 {rec['title']}</h2>
            <h4 style="text-align:center;">by {rec['artist']}</h4>
            <p style="text-align:center;">Mood: <b>{rec['mood']}</b></p>
        </div>
    """, unsafe_allow_html=True)

    if show_player:
        st.video(rec["url"])

    spotify_query = urllib.parse.quote_plus(f"{rec['title']} {rec['artist']}")
    spotify_url = f"https://open.spotify.com/search/{spotify_query}"

    yt_html = f'<a class="pill-btn yt-pill" href="{rec["url"]}" target="_blank">▶️ YouTube</a>'
    sp_html = f'<a class="pill-btn sp-pill" href="{spotify_url}" target="_blank">🎧 Spotify</a>'

    st.markdown(f'<div style="text-align:center">{yt_html} {sp_html}</div>', unsafe_allow_html=True)

else:
    st.markdown(f"""
        <style>
        .stApp {{
            background: {DEFAULT_GRADIENT};
            font-family: 'Poppins', sans-serif;
            color: #111;
        }}
        </style>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:#222;'>Developed with ❤️ by <b>Chilkamarri Prem Kumar (TechBro)</b></div>", unsafe_allow_html=True)
