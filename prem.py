import random
import streamlit as st
import urllib.parse

# songs_data now has tuples: (Title, Artist, URL, Genre, Language)
songs_data = {
    "Happy": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "Pop/Funk", "English"),
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0", "Dance/Funk", "English"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw", "Pop", "English"),
        ("Shake It Off", "Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM", "Pop", "English"),
        ("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=vuq-VAiW9kw", "R&B/Soul", "English"),
        ("Lovely Day", "Bill Withers", "https://www.youtube.com/watch?v=bO0yXbJd2iQ", "Soul/Classic", "English"),
        ("I Wanna Dance with Somebody", "Whitney Houston", "https://www.youtube.com/watch?v=eH3giaIzONA", "80s Pop", "English")
    ],
    "Sad": [
        ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "Ballad", "English"),
        ("Let Her Go", "Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA", "Acoustic", "English"),
        ("When I Was Your Man", "Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4", "Ballad", "English"),
        ("Hello", "Adele", "https://www.youtube.com/watch?v=YQHsXMglC9A", "Soul", "English"),
        ("Hurt", "Johnny Cash", "https://www.youtube.com/watch?v=vt1P_0f5w9g", "Acoustic", "English"),
        ("Fix You", "Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM", "Rock", "English")
    ],
    "Relaxed": [
        ("Let It Be", "The Beatles", "https://www.youtube.com/watch?v=QDYfEBY9NM4", "Classic Rock", "English"),
        ("Perfect", "Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "Acoustic Pop", "English"),
        ("Lovely", "Billie Eilish & Khalid", "https://www.youtube.com/watch?v=V1Pl8CzNzCw", "Atmospheric", "English"),
        ("Ocean Eyes", "Billie Eilish", "https://www.youtube.com/watch?v=viimfQi_pUw", "Atmospheric", "English"),
        ("Sunflower", "Post Malone & Swae Lee", "https://www.youtube.com/watch?v=ApXoWvfEYVU", "Hip-Hop/Chill", "English"),
        ("Let Me Down Slowly", "Alec Benjamin", "https://www.youtube.com/watch?v=50VNCymT-Cs", "Acoustic Pop", "English"),
        ("A Thousand Years", "Christina Perry", "https://www.youtube.com/watch?v=rtOvBOTyX00", "Ballad", "English")
    ],
    "Energetic": [
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc", "Rock", "English"),
        ("Thunder", "Imagine Dragons", "https://www.youtube.com/watch?v=fKopy74weus", "Pop/Rock", "English"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "Hip-Hop", "English"),
        ("Don't Start Now", "Dua Lipa", "https://www.youtube.com/watch?v=oygrmJFKYZY", "Dance/Pop", "English"),
        ("Can't Hold Us", "Macklemore & Ryan Lewis", "https://www.youtube.com/watch?v=2zNSgSzhBfM", "Hip-Hop", "English"),
        ("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg", "EDM", "English")
    ]
}

REMIX_STYLES = [
    "Original Vibe",
    "Acoustic Cover",
    "8-bit/Chiptune",
    "Dubstep Drop",
    "Lo-Fi Slowed",
    "Orchestral Sweep",
    "Reggaeton Bounce"
]

def generate_remix_description(song_title, remix_style):
    if remix_style == "Original Vibe":
        return f"The original track, perfectly tuned to your current mood."
    elif remix_style == "Acoustic Cover":
        return f"Imagine '{song_title}' stripped back—just guitar and raw emotion."
    elif remix_style == "8-bit/Chiptune":
        return f"A pixelated soundscape! '{song_title}' remixed as a classic video game theme."
    elif remix_style == "Dubstep Drop":
        return f"WARNING: Heavy bass! '{song_title}' is transformed into a high-energy dance floor anthem."
    elif remix_style == "Lo-Fi Slowed":
        return f"A chill, rainy-day take: '{song_title}' slowed and draped in vinyl crackle."
    elif remix_style == "Orchestral Sweep":
        return f"A cinematic epic: '{song_title}' swells with violins and powerful brass."
    elif remix_style == "Reggaeton Bounce":
        return f"Get ready to move! '{song_title}' now features a driving Latin rhythm and dembow."
    return "A fresh take on the track, perfectly remixed for your vibe."

# Mood -> gradient families (random pick inside a family)
MOOD_GRADIENTS = {
    "Happy": [
        "linear-gradient(135deg, #FFF59D 0%, #FFB74D 100%)",
        "linear-gradient(135deg, #FFEEAD 0%, #FF8A65 100%)",
        "linear-gradient(135deg, #FFF48F 0%, #FF7043 100%)"
    ],
    "Sad": [
        "linear-gradient(135deg, #89CFF0 0%, #7257A5 100%)",
        "linear-gradient(135deg, #A8C7FF 0%, #7B61FF 100%)",
        "linear-gradient(135deg, #8EBEF5 0%, #5D4B8A 100%)"
    ],
    "Relaxed": [
        "linear-gradient(135deg, #C7F9CC 0%, #7AE3D6 100%)",
        "linear-gradient(135deg, #D0F2EA 0%, #A1E3DA 100%)",
        "linear-gradient(135deg, #E0FFEF 0%, #9FE6D8 100%)"
    ],
    "Energetic": [
        "linear-gradient(135deg, #FF7E5F 0%, #FEB47B 100%)",
        "linear-gradient(135deg, #FF6A88 0%, #FF9A9E 100%)",
        "linear-gradient(135deg, #7CFFB2 0%, #00E5FF 100%)"
    ]
}
DEFAULT_GRADIENT = "linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%)"

def pick_gradient_for_mood(mood):
    return random.choice(MOOD_GRADIENTS.get(mood, [DEFAULT_GRADIENT]))

# Streamlit config
st.set_page_config(page_title="Play It Bro — Mood Vibes", page_icon="🎧", layout="centered")

# Session defaults
if "last_recommendation" not in st.session_state:
    st.session_state["last_recommendation"] = None
if "show_player" not in st.session_state:
    st.session_state["show_player"] = False

# Header
st.markdown("<h1 style='text-align:center; margin-bottom:6px;'>🎶 Play It Bro — Mood Vibes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; margin-top:0;'>Pick a mood, choose languages, and get a vibey song!</p>", unsafe_allow_html=True)
st.markdown("---")

# Controls row
col_mood, col_spacer, col_lang = st.columns([2, .2, 2])

with col_mood:
    mood_choice = st.selectbox("Choose Mood:", options=list(songs_data.keys()), index=0, help="Select the mood you want.")

with col_lang:
    # Stylish language multiselect (flag + text)
    LANG_LABELS = ["🇮🇳 Telugu", "🇮🇳 Hindi", "🇺🇸 English", "🇮🇳 Tamil"]
    label_to_lang = {
        "🇮🇳 Telugu": "Telugu",
        "🇮🇳 Hindi": "Hindi",
        "🇺🇸 English": "English",
        "🇮🇳 Tamil": "Tamil"
    }
    selected_labels = st.multiselect("Language(s):", options=LANG_LABELS, default=["🇺🇸 English"])
    selected_langs = [label_to_lang[l] for l in selected_labels] if selected_labels else []

# Remix style
remix_choice = st.selectbox("Remix Style:", REMIX_STYLES, index=0, help="Pick a simulated remix vibe.")

# Show player toggle
st.session_state["show_player"] = st.toggle("Show YouTube Player", value=st.session_state["show_player"])

st.markdown("---")

# Generate recommendation button
if st.button("Generate Song Recommendation ✨", use_container_width=True):
    # Filter by mood -> initial list
    mood_songs = songs_data.get(mood_choice, [])
    # Filter by language if any selected
    if selected_langs:
        filtered = [s for s in mood_songs if s[4] in selected_langs]
    else:
        filtered = mood_songs[:]

    if not filtered:
        st.warning("No songs found for this mood + language selection. Try selecting more languages or a different mood.")
    else:
        song = random.choice(filtered)
        title, artist, url, genre, language = song
        remix_desc = generate_remix_description(title, remix_choice)

        st.session_state["last_recommendation"] = {
            "title": title,
            "artist": artist,
            "url": url,
            "genre": genre,
            "language": language,
            "remix_style": remix_choice,
            "remix_desc": remix_desc
        }

# Display recommendation
rec = st.session_state.get("last_recommendation")
active_gradient = pick_gradient_for_mood(mood_choice) if mood_choice else DEFAULT_GRADIENT

# Inject colorful gradient background + updated styling
st.markdown(f"""
<style>
/* App background */
.stApp {{
    background: {active_gradient};
    font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
    color: #111;
}}

/* Card */
.info-card {{
    background: rgba(255,255,255,0.95);
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.08);
    margin-top: 16px;
}}

/* Big primary button style */
div.stButton > button {{
    background: linear-gradient(90deg,#FF6A88,#FFA5C0);
    color:white;
    border-radius:10px;
    height:48px;
    font-weight:800;
}}

.lang-pill {{
    display:inline-block;
    background: rgba(255,255,255,0.9);
    padding:8px 12px;
    border-radius:999px;
    margin:4px;
    font-weight:700;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
}}

.footer {{
    text-align:center;
    color:#222;
    margin-top:24px;
}}
</style>
""", unsafe_allow_html=True)

if rec:
    st.success(f"✅ Vibe: {mood_choice} — {rec['title']} by {rec['artist']} ({rec['language']})")
    st.markdown(f"""
    <div class="info-card">
        <h2 style="text-align:center; margin:6px 0;">🎵 {rec['title']}</h2>
        <h4 style="text-align:center; margin:4px 0; color:#333;">by <b>{rec['artist']}</b></h4>
        <p style="text-align:center; font-style:italic; color:#444;">{rec['remix_desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Player or play link
    if st.session_state["show_player"]:
        # embedding may be blocked for some videos; use a safe play link below
        embed_link = rec['url'].replace("watch?v=", "embed/").replace("https://www.youtube.com", "https://www.youtube-nocookie.com")
        st.markdown(f"""
        <div style="text-align:center; margin-top:12px;">
            <iframe width="560" height="315" src="{embed_link}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <div style="margin-top:10px;">
                <a href="{rec['url']}" target="_blank" style="display:inline-block; background:linear-gradient(90deg,#FF6A88,#FFA5C0); color:white; padding:10px 18px; border-radius:10px; text-decoration:none; font-weight:700;">▶️ Open on YouTube</a>
                <a href="https://open.spotify.com/search/{urllib.parse.quote_plus(rec['title'] + ' ' + rec['artist'])}" target="_blank" style="display:inline-block; margin-left:8px; background:linear-gradient(90deg,#6A11CB,#2575FC); color:white; padding:10px 18px; border-radius:10px; text-decoration:none; font-weight:700;">🎧 Open on Spotify</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # show play buttons only
        st.markdown(f"""
        <div style="text-align:center; margin-top:12px;">
            <a href="{rec['url']}" target="_blank" style="display:inline-block; background:linear-gradient(90deg,#FF6A88,#FFA5C0); color:white; padding:12px 20px; border-radius:10px; text-decoration:none; font-weight:800;">▶️ Play on YouTube</a>
            <a href="https://open.spotify.com/search/{urllib.parse.quote_plus(rec['title'] + ' ' + rec['artist'])}" target="_blank" style="display:inline-block; margin-left:8px; background:linear-gradient(90deg,#6A11CB,#2575FC); color:white; padding:12px 20px; border-radius:10px; text-decoration:none; font-weight:800;">🎧 Spotify</a>
        </div>
        """, unsafe_allow_html=True)
else:
    # show friendly hint and language pill visuals
    st.markdown("<div style='text-align:center; margin-top:12px;'>Choose languages (flag pills) and press the pink button to get a song 🎶</div>", unsafe_allow_html=True)
    # display selected language pills for visual flair
    if selected_labels:
        pill_html = "".join([f"<span class='lang-pill'>{lab}</span>" for lab in selected_labels])
        st.markdown(f"<div style='text-align:center; margin-top:10px;'>{pill_html}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed with ❤️ by <b>Chilkamarri Prem Kumar (TechBro)</b></div>", unsafe_allow_html=True)
