# ai_mood_music_prem.py
import random
import streamlit as st
import urllib.parse
import re

# ---------------------------
#  DATA (song list with language)
#  Format: (Title, Artist, YouTube URL, Language)
# ---------------------------
songs_data = {
    "All": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "English"),
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0", "English"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw", "English"),
        ("Shake It Off", "Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM", "English"),
        ("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=vuq-VAiW9kw", "English"),
        ("Lovely Day", "Bill Withers", "https://www.youtube.com/watch?v=bO0yXbJd2iQ", "English"),
        ("I Wanna Dance with Somebody", "Whitney Houston", "https://www.youtube.com/watch?v=eH3giaIzONA", "English"),
        ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "English"),
        ("Let Her Go", "Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA", "English"),
        ("When I Was Your Man", "Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4", "English"),
        ("Hello", "Adele", "https://www.youtube.com/watch?v=YQHsXMglC9A", "English"),
        ("Fix You", "Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM", "English"),
        ("Let It Be", "The Beatles", "https://www.youtube.com/watch?v=QDYfEBY9NM4", "English"),
        ("Perfect", "Ed Sheeran", "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "English"),
        ("Lovely", "Billie Eilish & Khalid", "https://www.youtube.com/watch?v=V1Pl8CzNzCw", "English"),
        ("Sunflower", "Post Malone & Swae Lee", "https://www.youtube.com/watch?v=ApXoWvfEYVU", "English"),
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc", "English"),
        ("Thunder", "Imagine Dragons", "https://www.youtube.com/watch?v=fKopy74weus", "English"),
        ("Don't Start Now", "Dua Lipa", "https://www.youtube.com/watch?v=oygrmJFKYZY", "English"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "English"),
        ("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg", "English"),
        # Telugu/Hindi/Tamil examples (replace or expand with real YouTube links you prefer)
        ("Butta Bomma", "Armaan Malik", "https://www.youtube.com/watch?v=XYz2F8z4sVk", "Telugu"),
        ("Samajavaragamana", "Sid Sriram", "https://www.youtube.com/watch?v=KQmnn2ZsXJ4", "Telugu"),
        ("Tum Hi Ho", "Arijit Singh", "https://www.youtube.com/watch?v=Umqb9KENgmk", "Hindi"),
        ("Kal Ho Naa Ho", "Sonu Nigam", "https://www.youtube.com/watch?v=VYY4Y2c9k7o", "Hindi"),
        ("Naan Pizhaippeno", "Vijay Yesudas", "https://www.youtube.com/watch?v=example_tamil", "Tamil"),
        ("Vaathi Coming", "Anirudh Ravichander", "https://www.youtube.com/watch?v=example_vaathi", "Tamil"),
    ]
}

# ---------------------------
#  Mood keyword map (lightweight detection)
#  We'll look for these words in title / URL (lowercased)
# ---------------------------
MOOD_KEYWORDS = {
    "Happy": ["happy", "celebrate", "party", "dance", "uptown", "feeling", "dance", "dancefloor"],
    "Energetic": ["believer", "thunder", "stronger", "drop", "titanium", "can't hold us", "remix", "upbeat", "fast"],
    "Sad": ["someone like you", "let her go", "hurt", "fix you", "goodbye", "missing", "alone", "cry", "sad", "tears"],
    "Relaxed": ["perfect", "let it be", "ocean", "sunflower", "lovely", "calm", "lo-fi", "acoustic", "slow", "romantic", "love", "perfect"],
    # "Romantic" could be folded into Relaxed, but we keep Relaxed as fallback
}

# ---------------------------
#  Gradient color map per mood
# ---------------------------
GRADIENTS = {
    "Happy": "linear-gradient(135deg, #FFEF9F 0%, #FFC371 100%);",       # yellow -> soft orange
    "Sad": "linear-gradient(135deg, #89CFF0 0%, #7257A5 100%);",         # light blue -> purple
    "Relaxed": "linear-gradient(135deg, #C7F9CC 0%, #7AE3D6 100%);",     # mint -> teal
    "Energetic": "linear-gradient(135deg, #7CFFB2 0%, #00E5FF 100%);",   # neon green -> cyan
    "Default": "linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);"      # pink -> sky
}

# ---------------------------
#  Utility: detect mood from metadata (fast keyword-based)
# ---------------------------
def detect_mood_from_text(text: str) -> str:
    txt = (text or "").lower()
    # remove punctuation for simpler matching
    txt = re.sub(r"[^\w\s]", " ", txt)
    for mood, keywords in MOOD_KEYWORDS.items():
        for kw in keywords:
            if kw in txt:
                return mood
    # fallback heuristics: length / exclamation marks -> energetic/happy
    if txt.count("!") >= 1 or any(w in txt for w in ["remix", "party", "dance", "dj"]):
        return "Energetic"
    return "Relaxed"  # safe default

# ---------------------------
#  Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Mood Music (Prem) 🎵", page_icon="🎧", layout="centered")

# initialize session state
if "auto_mood_theme" not in st.session_state:
    st.session_state["auto_mood_theme"] = True
if "show_player" not in st.session_state:
    st.session_state["show_player"] = False
if "last_detected_mood" not in st.session_state:
    st.session_state["last_detected_mood"] = "Default"
if "last_recommendation" not in st.session_state:
    st.session_state["last_recommendation"] = None

# Header
st.markdown("""
<h1 style='text-align:center; margin-bottom:4px;'>🎶 AI Music Remix & Mood Generator (Prem)</h1>
<p style='text-align:center; color:#444; margin-top:0;'>Automatic mood detection → dynamic gradient background. Language filter included.</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Controls: Auto-theme toggle, show player toggle
col_a, col_b = st.columns([1,1])
with col_a:
    st.session_state["auto_mood_theme"] = st.toggle("Auto Mood Theme (ON / OFF)", value=st.session_state["auto_mood_theme"],
                                                   help="When ON the background gradient changes automatically based on the detected mood of the recommended song.")
with col_b:
    st.session_state["show_player"] = st.toggle("Show YouTube Player", value=st.session_state["show_player"],
                                                help="Embed the YouTube player in-app when playing a recommendation.")

# Language filter (multi-select)
available_languages = sorted(list(set([s[3] for s in songs_data["All"]])))
selected_languages = st.multiselect("Filter by Language (choose 1 or more):",
                                    options=available_languages,
                                    default=available_languages)

st.markdown("---")

# Remix style (optional, lightweight)
REMIX_STYLES = ["Original Vibe", "Acoustic Cover", "Lo-Fi Slowed", "8-bit/Chiptune", "Dubstep Drop", "Orchestral Sweep", "Reggaeton Bounce"]
remix_style_choice = st.selectbox("AI Remix Style (simulated):", REMIX_STYLES, index=0)

# Generate button
if st.button("Generate Song Recommendation ✨", use_container_width=True):
    # Filter by language
    filtered = [s for s in songs_data["All"] if s[3] in selected_languages]
    if not filtered:
        st.warning("No songs found for the chosen language(s). Choose another language.")
        st.stop()

    song = random.choice(filtered)
    title, artist, youtube_url, lang = song

    # Lightweight mood detection using title & url
    metadata_text = f"{title} {artist} {youtube_url}"
    detected_mood = detect_mood_from_text(metadata_text)
    st.session_state["last_detected_mood"] = detected_mood

    # Create a fun remix description (simple)
    remix_desc = {
        "Original Vibe": f"The original '{title}' tuned to your vibe.",
        "Acoustic Cover": f"'{title}' stripped-back acoustic — raw feeling.",
        "Lo-Fi Slowed": f"A chill lo-fi take on '{title}' for soft moods.",
        "8-bit/Chiptune": f"'{title}' as a retro game theme (8-bit).",
        "Dubstep Drop": f"High-energy bass remix of '{title}'.",
        "Orchestral Sweep": f"A cinematic orchestral take on '{title}'.",
        "Reggaeton Bounce": f"'{title}' with a Latin dembow groove — dance mode."
    }.get(remix_style_choice, "")

    # Save recommendation
    st.session_state["last_recommendation"] = {
        "title": title,
        "artist": artist,
        "url": youtube_url,
        "language": lang,
        "detected_mood": detected_mood,
        "remix_style": remix_style_choice,
        "remix_desc": remix_desc
    }

# If we have a recommendation show it
rec = st.session_state.get("last_recommendation")
if rec:
    detected = rec["detected_mood"]
    title = rec["title"]
    artist = rec["artist"]
    url = rec["url"]
    remix_desc = rec["remix_desc"]

    st.success(f"✅ Recommendation: {title} — {artist}  (Detected mood: {detected})")
    st.markdown(f"<h2 style='text-align:center; margin-top:6px;'>🎵 {title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center; color:#333;'>by <b>{artist}</b> — <small>{rec['language']}</small></h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-style:italic; color:#333;'>{remix_desc}</p>", unsafe_allow_html=True)

    if st.session_state["show_player"]:
        st.video(url)

    # External links
    spotify_query = urllib.parse.quote_plus(f"{title} {artist}")
    spotify_url = f"https://open.spotify.com/search/{spotify_query}"

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<a href="{url}" target="_blank"><button style="width:100%;height:48px;border-radius:8px;border:none;background:linear-gradient(90deg,#FF6A88,#FFA5C0);color:white;font-weight:700;">▶️ Open on YouTube</button></a>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<a href="{spotify_url}" target="_blank"><button style="width:100%;height:48px;border-radius:8px;border:none;background:linear-gradient(90deg,#6A11CB,#2575FC);color:white;font-weight:700;">🎧 Open on Spotify</button></a>""", unsafe_allow_html=True)

# ---------------------------
#  Dynamic CSS injection for gradient background
# ---------------------------
def get_active_gradient():
    if st.session_state["auto_mood_theme"] and st.session_state.get("last_detected_mood"):
        g = GRADIENTS.get(st.session_state["last_detected_mood"], GRADIENTS["Default"])
    else:
        g = GRADIENTS["Default"]
    return g

active_gradient = get_active_gradient()

st.markdown(f"""
<style>
/* App background */
.stApp {{
    background: {active_gradient}
    font-family: 'Poppins', 'Segoe UI', Roboto, Arial, sans-serif;
    color: #111;
    padding-top: 18px;
}}
/* Title style */
h1{{ color: #222; }}
/* Buttons */
div.stButton > button {{
    background: linear-gradient(90deg, #FF6A88, #FFA5C0);
    color: white;
    border-radius: 10px;
    height: 46px;
    font-size: 1.0rem;
    font-weight: 700;
}}
div.stButton > button:hover {{
    transform: scale(1.02);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}}
/* Success box */
.stSuccess {{
    background: rgba(255,255,255,0.9);
    border-left: 6px solid rgba(0,0,0,0.08);
    color: #111;
}}
/* Misc */
hr{{ border: none; height: 2px; background: rgba(255,255,255,0.25); margin: 18px 0; border-radius:4px; }}
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<div style='text-align:center; font-size:13px; color:#222;'>
Developed with ❤️ by <b>Chilkamarri Prem Kumar (TechBro)</b><br>
Vignan Institute of Technology and Science, Hyderabad
</div>
""", unsafe_allow_html=True)
