# prem.py
import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="Play It Bro — Mood Music", page_icon="🎧", layout="centered")

# -------------------------
# Song database: (title, artist, youtube_url, language, mood)
# Expand/replace URLs with your preferred YouTube links
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
    # add more songs here...
]

# -------------------------
# Mood gradient families (random pick within family)
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
# UI - Header
# -------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="margin-bottom:4px;">🎶 Play It Bro — Mood Music</h1>
        <p style="margin-top:0; color:#444;">Choose language(s) → pick mood → get a matching song with links & player.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# -------------------------
# Controls: language multiselect (flag + text), mood select, show player toggle
# -------------------------
LANG_LABELS = ["🇮🇳 Telugu", "🇮🇳 Hindi", "🇬🇧 English", "🇮🇳 Tamil"]
label_to_lang = {
    "🇮🇳 Telugu": "Telugu",
    "🇮🇳 Hindi": "Hindi",
    "🇬🇧 English": "English",
    "🇮🇳 Tamil": "Tamil"
}

selected_labels = st.multiselect("Choose language(s):", options=LANG_LABELS, default=["🇮🇳 Telugu", "🇬🇧 English"])
selected_langs = [label_to_lang[l] for l in selected_labels]

mood_options = ["Happy", "Sad", "Romantic", "Energetic", "Relaxed"]
mood_choice = st.selectbox("Select Mood:", mood_options, index=0)

show_player = st.checkbox("Show YouTube Player", value=True)

st.markdown("---")

# -------------------------
# Generate recommendation
# -------------------------
if st.button("Find me a song 🎧", use_container_width=True):
    # filter SONGS by selected languages and mood
    candidates = [s for s in SONGS if s[3] in selected_langs and s[4] == mood_choice]
    if not candidates:
        st.warning("No songs found for that mood + language combination. Try selecting more languages or a different mood.")
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
# Display recommendation (if exists)
# -------------------------
rec = st.session_state.get("current_song")
if rec:
    # pick a random gradient from the mood family
    grad_list = MOOD_GRADIENTS.get(rec["mood"], [DEFAULT_GRADIENT])
    active_gradient = random.choice(grad_list)

    # inject CSS for dynamic gradient & pill buttons
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {active_gradient};
            font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
            color: #111;
            padding-top: 18px;
        }}
        .pill-btn {{
            display:inline-block;
            padding:10px 14px;
            border-radius:12px;
            text-decoration:none;
            font-weight:700;
            margin:6px;
            color:#fff !important;
            box-shadow: 0 8px 26px rgba(0,0,0,0.12);
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
        """,
        unsafe_allow_html=True,
    )

    # Song details
    st.success(f"✅ {rec['mood']} pick: {rec['title']} — {rec['artist']} ({rec['language']})")
    st.markdown(
        f"""
        <div class="info-card">
            <h2 style="text-align:center; margin:6px 0;">🎵 {rec['title']}</h2>
            <h4 style="text-align:center; margin:4px 0; color:#333;">by <b>{rec['artist']}</b></h4>
            <p style="text-align:center; font-style:italic; color:#333; margin-top:6px;">Mood: <b>{rec['mood']}</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Embedded player (optional)
    if show_player:
        # Attempt to embed YouTube; st.video accepts full youtube url
        st.video(rec["url"])

    # External clickable pills: YouTube & Spotify Search
    spotify_query = urllib.parse.quote_plus(f"{rec['title']} {rec['artist']}")
    spotify_url = f"https://open.spotify.com/search/{spotify_query}"

    yt_html = f'<a class="pill-btn yt-pill" href="{rec["url"]}" target="_blank">▶️ Open on YouTube</a>'
    sp_html = f'<a class="pill-btn sp-pill" href="{spotify_url}" target="_blank">🎧 Open on Spotify</a>'

    st.markdown(f'<div style="text-align:center">{yt_html} {sp_html}</div>', unsafe_allow_html=True)

else:
    # default background CSS when nothing selected
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {DEFAULT_GRADIENT};
            font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
            color: #111;
            padding-top: 18px;
        }}
        .stMultiSelect > div[role="listbox"] {{
            border-radius: 12px;
            padding: 8px;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 8px 30px rgba(0,0,0,0.06);
        }}
        .stSelectbox > div[role="combobox"] {{
            border-radius: 10px;
            padding: 6px 10px;
            background: rgba(255,255,255,0.98);
        }}
        .stButton > button {{
            background: linear-gradient(90deg,#FF6A88,#FFA5C0);
            color:white;
            border-radius:10px;
            height:44px;
            font-weight:800;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.markdown("<div style='text-align:center; color:#222;'>Developed with ❤️ by <b>Chilkamarri Prem Kumar (TechBro)</b></div>", unsafe_allow_html=True)
