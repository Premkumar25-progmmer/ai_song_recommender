import streamlit as st
import random

# 🎵 Mood-based songs with working YouTube links
songs_db = {
    "Happy": {
        "Telugu": [
            ("Rowdy Baby - Maari 2", "https://www.youtube.com/watch?v=x6Q7c9RyMzk"),
            ("Vibe Undi - Mirai", "https://www.youtube.com/watch?v=sUuLY8-LjKM"),
            ("Ma Ma Mahesha - Sarkaru Vaari Paata", "https://www.youtube.com/watch?v=3kcadMVFolY"),
            ("Kurchi Madathapetti - Guntur Kaaram", "https://www.youtube.com/watch?v=gh3FyLT7WVg")
        ],
        "Hindi": [
            ("Kala Chashma - Baar Baar Dekho", "https://www.youtube.com/watch?v=k4yXQkG2s1E"),
            ("Kar Gayi Chull - Kapoor & Sons", "https://www.youtube.com/watch?v=5AqOjl8lC6Q")
        ],
        "Tamil": [
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=NKz1j8ZzAcg"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=ObxBja3r3tQ")
        ]
    },
    "Sad": {
        "Telugu": [
            ("Nee Kallu Neeli Samudram - Uppena", "https://www.youtube.com/watch?v=7kjb0WvPq1s"),
            ("The Life of Ram - Jaanu", "https://www.youtube.com/watch?v=zFZbHjPl4g0")
        ],
        "Hindi": [
            ("Channa Mereya - Ae Dil Hai Mushkil", "https://www.youtube.com/watch?v=284Ov7ysmfA"),
            ("Agar Tum Saath Ho - Tamasha", "https://www.youtube.com/watch?v=-OnO4bQMuX0")
        ],
        "Tamil": [
            ("Vaseegara - Minnale", "https://www.youtube.com/watch?v=4TSJhIZmL0A"),
            ("Enna Solla Pogirai - Kandukondain Kandukondain", "https://www.youtube.com/watch?v=6e6zvJ6r8nc")
        ]
    },
    "Romantic": {
        "Telugu": [
            ("Inkem Inkem Inkem Kaavaale - Geetha Govindam", "https://www.youtube.com/watch?v=3vLm-Lwibx0"),
            ("Butta Bomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=1J76wN0TPI4")
        ],
        "Hindi": [
            ("Tum Hi Ho - Aashiqui 2", "https://www.youtube.com/watch?v=Umqb9KENgmk"),
            ("Raabta - Agent Vinod", "https://www.youtube.com/watch?v=Q8q0vFjzv-8")
        ],
        "Tamil": [
            ("Munbe Vaa - Sillunu Oru Kadhal", "https://www.youtube.com/watch?v=Zp9HUcFZ6N8"),
            ("Anbe En Anbe - Dhaam Dhoom", "https://www.youtube.com/watch?v=kGiOytZtJmE")
        ]
    },
    "Energetic": {
        "Telugu": [
            ("Ramuloo Ramulaa - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=Gx_B0YzqjDs"),
            ("Mind Block - Sarileru Neekevvaru", "https://www.youtube.com/watch?v=jKthYgm1JzE"),
            ("Naatu Naatu - RRR", "https://www.youtube.com/watch?v=OsU0CGZoV8E")
        ],
        "Hindi": [
            ("Malhari - Bajirao Mastani", "https://www.youtube.com/watch?v=UoFzG7w6n8E")
        ],
        "Tamil": [
            ("Aalaporan Thamizhan - Mersal", "https://www.youtube.com/watch?v=qzOeGW1gWVQ")
        ]
    }
}

# 🌈 Gradient backgrounds by mood
gradients = {
    "Happy": ["linear-gradient(135deg, #FFD54F, #FF8A65)", "linear-gradient(135deg, #FFF176, #FFB74D)"],
    "Sad": ["linear-gradient(135deg, #90CAF9, #4A148C)", "linear-gradient(135deg, #7986CB, #3F51B5)"],
    "Romantic": ["linear-gradient(135deg, #F48FB1, #F06292)", "linear-gradient(135deg, #FFCDD2, #E91E63)"],
    "Energetic": ["linear-gradient(135deg, #FF7043, #FFEE58)", "linear-gradient(135deg, #FF5722, #FFC107)"]
}

def random_gradient(mood):
    return random.choice(gradients[mood])

# 🌈 Page Setup
st.markdown("<h1 style='text-align:center; color:#FF4081;'>🎶 Play It Bro - Mood Based Song Recommender 🎵</h1>", unsafe_allow_html=True)
st.write("#### Let's find the perfect song for your vibe!")

# 🎭 Mood select
mood = st.radio("Select your mood:", list(songs_db.keys()), horizontal=True)

# 🌐 Language multiselect
languages = st.multiselect("Choose languages:", ["Telugu", "Hindi", "Tamil"], default=["Telugu"])

# 🎨 Background color based on mood
bg_gradient = random_gradient(mood)
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
background: {bg_gradient};
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🎧 Recommend Button
if st.button("🎧 Recommend Me a Song"):
    selected = []
    for lang in languages:
        selected += songs_db[mood].get(lang, [])
    if selected:
        song_name, song_link = random.choice(selected)
        embed_link = song_link.replace("watch?v=", "embed/")
        st.markdown(f"""
        <div style="text-align:center; background-color:rgba(0,0,0,0.6); color:white; padding:25px; border-radius:15px;">
            <h2>🎵 Mood: <span style="color:#FFD700;">{mood}</span></h2>
            <h3>✨ {song_name}</h3>
            <iframe width="360" height="215" src="{embed_link}" frameborder="0" allowfullscreen></iframe>
            <p><a href="{song_link}" target="_blank" style="color:#4CAF50;">▶️ Open on YouTube</a></p>
            <p style="color:#ccc;">Enjoy the beat 🎧</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("No songs found for your selected mood and language!")

st.markdown("<hr><p style='text-align:center; color:gray;'>Built with ❤️ by Prem Kumar | Play It Bro 🎶</p>", unsafe_allow_html=True)
