import random
import streamlit as st
import urllib.parse
from collections import defaultdict

# --- 1. CONFIGURATION (SHARP MONOCHROME & EXPANDED DATA) ---

# 🎵 Mood-to-song mapping
# DATA FORMAT: "Mood": [ (Title, Artist, URL, Genre/Vibe), ... ]
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
        ("Ocean Eyes", "Billie Eilish", "https://www.youtube.com/watch?v=viimfQi_pUw", "Atmospheric"),
        ("Sunflower", "Post Malone & Swae Lee", "https://www.youtube.com/watch?v=ApXoWvfEYVU", "Hip-Hop/Chill"),
        ("Let Me Down Slowly", "Alec Benjamin", "https://www.youtube.com/watch?v=50VNCymT-Cs", "Acoustic Pop"),
        ("A Thousand Years", "Christina Perry", "https://www.youtube.com/watch?v=rtOvBOTyX00", "Ballad")
    ],
    "Energetic": [
        ("Believer", "Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc", "Rock"),
        ("Thunder", "Imagine Dragons", "https://www.youtube.com/watch?v=fKopy74weus", "Pop/Rock"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "Hip-Hop"),
        ("Don't Start Now", "Dua Lipa", "https://www.youtube.com/watch?v=oygrmJFKYZY", "Dance/Pop"),
        ("Can't Hold Us", "Macklemore & Ryan Lewis", "https://www.youtube.com/watch?v=2zNSgSzhBfM", "Hip-Hop"),
        ("Titanium", "David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg", "EDM")
    ]
}

# 🎶 NEW: Remix Style Options
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
    """Generates a creative description for the simulated AI Remix."""
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


# 🎨 Aesthetic Monochrome Color Palette
COLOR_BLACK_PURE = "#000000"
COLOR_SOFT_BLACK = "#1C1C1C"      
COLOR_DARK_GRAY = "#333333"       
COLOR_MEDIUM_GRAY = "#888888"     
COLOR_LIGHT_GRAY = "#EEEEEE"      
COLOR_WHITE_PURE = "#FFFFFF"      

# 🌈 Mood-specific Accent Colors
MOOD_COLOR_ACCENTS = {
    "Happy": "#FFCC00",      # Amber/Gold
    "Sad": "#4B0082",        # Indigo
    "Relaxed": "#00AA6C",    # Sea Green
    "Energetic": "#FF4500"   # Orange-Red
}

MONOCHROME_THEME = {
    "primary_button_bg": COLOR_DARK_GRAY,
    "primary_button_text": COLOR_WHITE_PURE,
    "main_bg": COLOR_SOFT_BLACK,
    "main_text": COLOR_LIGHT_GRAY, 
    "container_bg": COLOR_WHITE_PURE,
    "container_text": COLOR_BLACK_PURE,
    "accent_border": COLOR_MEDIUM_GRAY
}

MOOD_THEMES = {
    "Happy": MONOCHROME_THEME,
    "Sad": MONOCHROME_THEME,
    "Relaxed": MONOCHROME_THEME,
    "Energetic": MONOCHROME_THEME
}

# 🎧 Streamlit Page Setup
st.set_page_config(page_title="AI Music Remix & Mood Generator", page_icon="🎵", layout="centered")

# Initialize session state for the current theme and selections
if 'current_mood' not in st.session_state:
    st.session_state['current_mood'] = 'Happy' 
if 'selected_artist' not in st.session_state:
    st.session_state['selected_artist'] = 'Any Artist'
if 'selected_genre' not in st.session_state:
    st.session_state['selected_genre'] = 'Any Genre'
if 'selected_remix_style' not in st.session_state:
    st.session_state['selected_remix_style'] = 'Original Vibe' # NEW STATE
if 'show_player' not in st.session_state:
    st.session_state['show_player'] = False  

# Assign the active theme colors (necessary for CSS variables)
current_theme = MOOD_THEMES[st.session_state['current_mood']]
current_accent_color = MOOD_COLOR_ACCENTS[st.session_state['current_mood']]

# Main Title
st.title("🎶 AI Music Remix & Mood Generator")

# ----------------------------------------------------------------------
# --- 2. MAIN APPLICATION LOGIC ---
# ----------------------------------------------------------------------

with st.container(border=False): 
    st.header("Select Your Vibe", divider='gray') 
    st.write("Refine your music recommendation by selecting mood, artist, genre, and a remix style. 🎧")

    # --- TOGGLE FEATURE ---
    st.session_state['show_player'] = st.toggle("Show YouTube Player in App", 
                                                value=st.session_state['show_player'], 
                                                help="Enable this to embed the YouTube player directly below the recommendation.")

    st.markdown(f"<hr style='border-top: 1px solid {COLOR_MEDIUM_GRAY}; margin: 30px 0;'>", unsafe_allow_html=True) 

    def update_mood():
        """Updates mood and resets other selections."""
        st.session_state['current_mood'] = st.session_state['selected_mood']
        st.session_state['selected_artist'] = 'Any Artist' 
        st.session_state['selected_genre'] = 'Any Genre'
        st.session_state['selected_remix_style'] = 'Original Vibe'
        st.rerun() 
        
    def update_artist():
        """Updates artist and resets genre/remix selection."""
        st.session_state['selected_genre'] = 'Any Genre'
        st.session_state['selected_remix_style'] = 'Original Vibe'
        st.rerun() 
    
    def update_genre():
        """Updates genre and resets remix selection."""
        st.session_state['selected_remix_style'] = 'Original Vibe'
        pass 
        
    def update_remix():
        """Updates remix selection."""
        pass

    # --- HORIZONTAL FILTERS USING COLUMNS ---
    col_mood, col_artist, col_genre = st.columns(3)

    # --- MOOD SELECTION ---
    with col_mood:
        mood_choice = st.selectbox(
            "Current Mood:", 
            list(songs_data.keys()), 
            index=list(songs_data.keys()).index(st.session_state['current_mood']), 
            key='selected_mood', 
            on_change=update_mood, 
            help="Choose how you're feeling."
        )

    # --- ARTIST SELECTION (DYNAMIC) ---
    current_mood_songs = songs_data[mood_choice]
    unique_artists = sorted(list(set([song[1] for song in current_mood_songs])))
    artist_options = ['Any Artist'] + unique_artists

    try:
        current_artist_index = artist_options.index(st.session_state['selected_artist'])
    except ValueError:
        current_artist_index = 0
        st.session_state['selected_artist'] = 'Any Artist'
    
    with col_artist:
        artist_choice = st.selectbox(
            "Filter by Artist:", 
            artist_options,
            index=current_artist_index,
            key='selected_artist',
            on_change=update_artist,
            help="Select a specific artist within this mood."
        )
    
    # --- GENRE SELECTION (DYNAMIC) ---
    if artist_choice != 'Any Artist':
        current_filtered_songs = [song for song in current_mood_songs if song[1] == artist_choice]
    else:
        current_filtered_songs = current_mood_songs

    unique_genres = sorted(list(set([song[3] for song in current_filtered_songs])))
    genre_options = ['Any Genre'] + unique_genres

    try:
        current_genre_index = genre_options.index(st.session_state['selected_genre'])
    except ValueError:
        current_genre_index = 0
        st.session_state['selected_genre'] = 'Any Genre'
    
    with col_genre:
        genre_choice = st.selectbox(
            "Filter by Genre:", 
            genre_options,
            index=current_genre_index,
            key='selected_genre',
            on_change=update_genre,
            help="Filter by a specific genre/vibe for more precise results."
        )

    st.markdown(f"<hr style='border-top: 1px solid {current_accent_color}; margin: 30px 0;'>", unsafe_allow_html=True) 

    # --- NEW FEATURE: REMIX STYLE SELECTION ---
    remix_style_choice = st.selectbox(
        "AI Remix Style:", 
        REMIX_STYLES,
        index=REMIX_STYLES.index(st.session_state['selected_remix_style']),
        key='selected_remix_style',
        on_change=update_remix,
        help="Choose a style for the simulated AI Remix of the song."
    )
    
    st.markdown(f"<hr style='border-top: 1px solid {current_accent_color}; margin: 30px 0;'>", unsafe_allow_html=True) 
    
    # 🕹️ Recommend button
    if st.button("Generate Song Recommendation ✨", use_container_width=True, type='primary'):
        if mood_choice:
            # --- TRIPLE FILTERING LOGIC ---
            filtered_songs = current_mood_songs
            
            if artist_choice != 'Any Artist':
                filtered_songs = [song for song in filtered_songs if song[1] == artist_choice]
            
            if genre_choice != 'Any Genre':
                filtered_songs = [song for song in filtered_songs if song[3] == genre_choice]
            
            if not filtered_songs:
                 st.warning("No songs found matching your selection. Try a broader filter.")
                 st.stop()
                 
            # --- FINAL RECOMMENDATION ---
            song = random.choice(filtered_songs)
            song_title, artist_name, youtube_url, genre = song
            
            # Generate the simulated remix description
            remix_desc = generate_remix_description(song_title, remix_style_choice)

            # Save the result to session state
            st.session_state['last_recommendation'] = {
                'title': song_title,
                'artist': artist_name,
                'url': youtube_url,
                'genre': genre,
                'remix_style': remix_style_choice, # Save style
                'remix_desc': remix_desc         # Save description
            }
            
            # --- Recommendation Output ---
            st.success(f"**✅ Vibe set to {mood_choice.upper()}!**")
            
            st.markdown(f"<h2 style='text-align: center; color: {COLOR_LIGHT_GRAY};'>'{song_title}'</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; color: {COLOR_LIGHT_GRAY};'>by <b>{artist_name}</b></h3>", unsafe_allow_html=True)
            
            # NEW: Remix Description Display
            st.markdown(f"""
            <div style="text-align: center; margin-top: 20px; padding: 10px 0; border-top: 1px dashed {COLOR_MEDIUM_GRAY}; border-bottom: 1px dashed {COLOR_MEDIUM_GRAY};">
                <span style="color: {current_accent_color}; font-weight: bold;">AI Remix Vibe:</span> 
                <span style="color: {COLOR_LIGHT_GRAY};">({remix_style_choice})</span>
                <p style="color: {COLOR_LIGHT_GRAY}; margin-top: 5px; font-style: italic;">{remix_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")

            # --- Conditional In-App Player ---
            if st.session_state['show_player']:
                st.subheader("🎵 In-App Player")
                st.video(youtube_url)
                st.markdown("---")
            
            # --- Link Generation (Always show external links) ---
            spotify_query = urllib.parse.quote_plus(f"{song_title} {artist_name}")
            spotify_url = f"https://open.spotify.com/search/{spotify_query}" 

            col1, col2 = st.columns(2)

            with col1:
                # Open on YouTube Button
                st.markdown(f"""
                <div class="platform-link-container">
                    <a href="{youtube_url}" target="_blank">
                        <button class="platform-button" style="
                            background-color: {COLOR_DARK_GRAY}; color: {COLOR_WHITE_PURE};
                        ">
                            ▶️
                        </button>
                    </a>
                    <p class="platform-text-dark-bg">Open on YouTube</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                # Spotify Button
                st.markdown(f"""
                <div class="platform-link-container">
                    <a href="{spotify_url}" target="_blank">
                        <button class="platform-button" style="
                            background-color: {COLOR_DARK_GRAY}; color: {COLOR_WHITE_PURE};
                        ">
                            🎧
                        </button>
                    </a>
                    <p class="platform-text-dark-bg">Open on Spotify</p>
                </div>
                """, unsafe_allow_html=True)
            
        else:
            st.warning("Please select a mood first!")

# ----------------------------------------------------------------------
# --- 3. DEVELOPER FOOTER ---
# ----------------------------------------------------------------------
st.markdown("<div class='footer'>Developed by: ESHWAR ARENDALA<br>VIGNAN INSTITUTE OF TECHNOLOGY AND SCIENCE, HYDERABAD</div>", unsafe_allow_html=True)


# ----------------------------------------------------------------------
# --- 4. DYNAMIC & ENHANCED STYLING (CSS) ---
# ----------------------------------------------------------------------
st.markdown(f"""
<style>
    /* Overall App Styling */
    .stApp {{
        background: {current_theme['main_bg']}; 
        color: {current_theme['main_text']}; 
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
        padding: 20px;
    }}
    
    /* Title Styling - Prominent and readable */
    h1 {{
        text-align: center;
        color: {COLOR_WHITE_PURE}; 
        font-size: 3em; 
        margin-bottom: 30px;
        text-shadow: 
            2px 2px 4px rgba(0,0,0,0.5); 
    }}

    /* Main Content Container Styling - Card-like appearance */
    .stContainer {{
        padding: 40px;
        border-radius: 12px;
        background-color: {current_theme['container_bg']}; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); 
        margin-bottom: 30px; 
        border: 1px solid {COLOR_MEDIUM_GRAY}; 
    }}

    /* Header Styling within container */
    h2, h3, h4, .stText {{
        color: {current_theme['container_text']}; /* Black on White */
    }}
    
    /* Global H2/H3 for song title/artist text outside the container */
    .st-emotion-cache-1g2b1gn h2,
    .st-emotion-cache-1g2b1gn h3 {{
        color: {COLOR_LIGHT_GRAY} !important; 
    }}

    /* Selectbox Styling */
    .stSelectbox div[data-baseweb="select"] {{
        background-color: {COLOR_DARK_GRAY}; 
        color: {COLOR_BLACK_PURE};
        border-radius: 8px;
        padding: 8px 12px;
        border: 1px solid {COLOR_MEDIUM_GRAY};
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
        font-size: 16px;
        margin-top: -10px; 
    }}
    
    /* FIX: Color of the SELECTED text inside the dropdown */
    .stSelectbox div[data-baseweb="select"] > div[data-testid="stText"] {{
        color: {COLOR_LIGHT_GRAY} !important; 
    }}

    /* Dropdown arrow and current value */
    .stSelectbox div[data-baseweb="select"] > div {{ 
        color: {COLOR_LIGHT_GRAY}; 
    }}
    
    /* Primary Button Styling */
    div.stButton button[kind="primary"] {{
        background-color: {current_theme['primary_button_bg']}; 
        color: {current_theme['primary_button_text']}; 
        border-radius: 8px;
        height: 4em; 
        font-size: 1.1em; 
        font-weight: bold;
        letter-spacing: 0.05em; 
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); 
        margin-top: 20px; 
    }}
    div.stButton button[kind="primary"]:hover {{
        background-color: {COLOR_BLACK_PURE}; 
        transform: translateY(-3px) scale(1.01); 
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
    }}
    
    /* Success/Result Styling - Dynamic Accent Color */
    .stSuccess {{
        background-color: {COLOR_LIGHT_GRAY}; 
        border-left: 5px solid {current_accent_color}; 
        border-radius: 8px;
        padding: 15px;
        margin-top: 25px;
        font-weight: bold;
        text-align: center;
        color: {COLOR_BLACK_PURE}; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .stSuccess > div > strong {{ 
        color: {COLOR_BLACK_PURE}; 
    }}
    
    /* Horizontal Rule (Divider) Styling */
    hr {{
        border-top: 1px solid {current_accent_color} !important;
        margin: 30px 0;
    }}
    
    /* Footer Styling */
    .footer {{
        text-align: center;
        margin-top: 60px; 
        color: {current_theme['main_text']}; 
        font-size: 0.9em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
        opacity: 0.8;
        line-height: 1.5; 
    }}

    /* Container for platform link and text */
    .platform-link-container {{
        text-align: center;
        margin-bottom: 20px; 
    }}

    /* Platform Button Styling for larger, square logos */
    button.platform-button {{
        width: 100%; 
        height: 50px; 
        border-radius: 8px; 
        display: inline-flex; 
        justify-content: center; 
        align-items: center; 
        font-size: 1.0em; 
        font-weight: bold;
        border: none;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.25); 
        transition: all 0.2s ease-in-out;
        margin-top: 15px; 
    }}

    button.platform-button:hover {{
        transform: translateY(-2px) scale(1.02); 
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }}

    /* Platform Text Styling (below buttons on DARK BACKGROUND) */
    .platform-text-dark-bg {{
        color: {COLOR_LIGHT_GRAY}; 
        font-size: 0.85em; 
        font-weight: 700; 
        margin-top: 5px; 
        margin-bottom: 0; 
        text-transform: uppercase; 
        letter-spacing: 0.05em; 
    }}
    
    /* Toggle switch label color */
    .stToggle label {{
        color: {COLOR_LIGHT_GRAY} !important;
        font-weight: 600;
    }}

    /* Headings inside the white container */
    h2, h3, h4 {{
        color: {COLOR_BLACK_PURE}; 
    }}

    /* Selectbox label color (the text "Current Mood:" etc. on the white card) */
    label.st-emotion-cache-1rxv7cn.e16fv1u22 {{ 
        color: {COLOR_BLACK_PURE}; 
        font-weight: 700;
        font-size: 1.1em;
    }}

    /* Selectbox label color when in a column (on the dark background) */
    .st-emotion-cache-1rxv7cn.e16fv1u22 {{
        color: {COLOR_LIGHT_GRAY} !important;
    }}
    
    /* Force selectbox labels in columns to be centered/consistent */
    .st-emotion-cache-16ffz9o label {{
        color: {COLOR_LIGHT_GRAY} !important;
    }}
</style>
""", unsafe_allow_html=True)
