import streamlit as st
import random

# 🎵 Mood-based songs with working YouTube links
songs_db = {
    "Happy": {
        "Telugu": [
            ("Rowdy Baby - Maari 2", "https://www.youtube.com/watch?v=x6Q7c9RyMzk&list=RDx6Q7c9RyMzk&start_radio=1"),
            ("My Name Is Billa - Billa", "https://www.youtube.com/watch?v=pfNF2Vqr3l0&list=RDpfNF2Vqr3l0&start_radio=1"),
            ("Bommali - billa", "https://www.youtube.com/watch?v=YLcCryHUNOg&list=RDYLcCryHUNOg&start_radio=1"),
            ("Vibe Undi - Mirai", "https://www.youtube.com/watch?v=sUuLY8-LjKM&list=RDsUuLY8-LjKM&start_radio=1"),
            ("Koyila Music  - Maari 2", "https://www.youtube.com/watch?v=uhY2fqU_1yA&list=RDuhY2fqU_1yA&start_radio=1"),
            ("Monica - COOLIE", "https://www.youtube.com/watch?v=K3nRKezdDIM&list=RDK3nRKezdDIM&start_radio=1"),
            ("Ma Ma Mahesha - Sarkaru Vaari Paata", "https://www.youtube.com/watch?v=3kcadMVFolY&list=RD3kcadMVFolY&start_radio=1"),
            ("Kurchi Madathapetti -Guntur Kaaram", "https://www.youtube.com/watch?v=gh3FyLT7WVg&list=RDgh3FyLT7WVg&start_radio=1")
        ],
        "Hindi": [
            ("Kala Chashma - Baar Baar Dekho", "https://www.youtube.com/watch?v=k4yXQkG2s1E"),
            ("Kar Gayi Chull - Kapoor & Sons", "https://www.youtube.com/watch?v=5AqOjl8lC6Q"),
            ("Dil Dhadakne Do - Zindagi Na Milegi Dobara", "https://www.youtube.com/watch?v=GQ3AcPEPyT8")
        ],
        "Tamil": [
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=NKz1j8ZzAcg"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=ObxBja3r3tQ"),
            ("Jimikki Kammal - Velipadinte Pusthakam", "https://www.youtube.com/watch?v=I4Xxr8b_Yns")
        ]
    },
    "Sad": {
        "Telugu": [
            ("Nee Kallu Neeli Samudram - Uppena", "https://www.youtube.com/watch?v=7kjb0WvPq1s"),
            ("The Life of Ram - Jaanu", "https://www.youtube.com/watch?v=zFZbHjPl4g0"),
            ("Samajavaragamana - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=4J1RbhM7b8c")
        ],
        "Hindi": [
            ("Channa Mereya - Ae Dil Hai Mushkil", "https://www.youtube.com/watch?v=284Ov7ysmfA"),
            ("Agar Tum Saath Ho - Tamasha", "https://www.youtube.com/watch?v=-OnO4bQMuX0"),
            ("Tera Ban Jaunga - Kabir Singh", "https://www.youtube.com/watch?v=3eUl2TQ1D_c")
        ],
        "Tamil": [
            ("Vaseegara - Minnale", "https://www.youtube.com/watch?v=4TSJhIZmL0A"),
            ("Pogiren - Anniyan", "https://www.youtube.com/watch?v=ZHDxje7zX5I"),
            ("Enna Solla Pogirai - Kandukondain Kandukondain", "https://www.youtube.com/watch?v=6e6zvJ6r8nc")
        ]
    },
    "Romantic": {
        "Telugu": [
            ("Inkem Inkem Inkem Kaavaale - Geetha Govindam", "https://www.youtube.com/watch?v=3vLm-Lwibx0"),
            ("Butta Bomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=1J76wN0TPI4"),
            ("Priyathama Priyathama - Majili", "https://www.youtube.com/watch?v=yIw2Y6sONJU")
        ],
        "Hindi": [
            ("Tum Hi Ho - Aashiqui 2", "https://www.youtube.com/watch?v=Umqb9KENgmk"),
            ("Raabta - Agent Vinod", "https://www.youtube.com/watch?v=Q8q0vFjzv-8"),
            ("Pehla Nasha - Jo Jeeta Wohi Sikandar", "https://www.youtube.com/watch?v=3yYw2e4aGGE")
        ],
        "Tamil": [
            ("Anbe En Anbe - Dhaam Dhoom", "https://www.youtube.com/watch?v=kGiOytZtJmE"),
            ("Kanave Kanave - David", "https://www.youtube.com/watch?v=5O9q8IPlu6U"),
            ("Munbe Vaa - Sillunu Oru Kadhal", "https://www.youtube.com/watch?v=Zp9HUcFZ6N8")
        ]
    },
    "Energetic": {
        "Telugu": [
            ("Ramuloo Ramulaa - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=Gx_B0YzqjDs"),
            ("Mind Block - Sarileru Neekevvaru", "https://www.youtube.com/watch?v=jKthYgm1JzE"),
            ("Naatu Naatu - RRR", "https://www.youtube.com/watch?v=OsU0CGZoV8E")
        ],
        "Hindi": [
            ("Malhari - Bajirao Mastani", "https://www.youtube.com/watch?v=UoFzG7w6n8E"),
            ("Zinda - Bhaag Milkha Bhaag", "https://www.youtube.com/watch?v=4tiVPffH0Tg"),
            ("Jai Jai Shivshankar - War", "https://www.youtube.com/watch?v=YxWlaYCA8MU")
        ],
        "Tamil": [
            ("Aalaporan Thamizhan - Mersal", "https://www.youtube.com/watch?v=qzOeGW1gWVQ"),
            ("Surviva - Vivegam", "https://www.youtube.com/watch?v=sAhK9Vd214c"),
            ("Verithanam - Bigil", "https://www.youtube.com/watch?v=GQ8_0NQYlJQ")
        ]
    }
}

# 🌈 Mood-based gradient colors
gradients = {
    "Happy": ["linear-gradient(135deg, #FFD54F, #FF8A65)", "linear-gradient(135deg, #FFF176, #FFB74D)"],
    "Sad": ["linear-gradient(135deg, #90CAF9, #4A148C)", "linear-gradient(135deg, #7986CB, #3F51B5)"],
    "Romantic": ["linear-gradient(135deg, #F48FB1, #F06292)", "linear-gradient(135deg, #FFCDD2, #E91E63)"],
    "Energetic": ["linear-gradient(135deg, #FF7043, #FFEE58)", "linear-gradient(135deg, #FF5722, #FFC107)"]
}

# 🎨 Pick random gradient based on mood
def random_gradient(mood):
    return random.choice(gradients[mood])

# 🌈 Apply background gradient
mood_placeholder = st.empty()

# 🎧 App title
st.markdown("<h1 style='text-align:center; color:#FF4081;'>🎶 Play It Bro - Mood Based Song Recommender 🎵</h1>", unsafe_allow_html=True)
st.write("#### Let's find the perfect song for your vibe!")

# 🎭 Mood selection
mood = st.radio("Select your mood:", list(songs_db.keys()), horizontal=True)

# 🌐 Language multiselect (Telugu, Hindi, Tamil only)
languages = st.multiselect("Choose languages:", ["Telugu", "Hindi", "Tamil"], default=["Telugu"])

# 🖼️ Apply mood gradient background dynamically
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

# 🎵 Recommend button
if st.button("🎧 Recommend Me a Song"):
    selected = []
    for lang in languages:
        selected += songs_db[mood].get(lang, [])
    if selected:
        song_name, song_link = random.choice(selected)
        st.markdown(f"""
        <div style="text-align:center; background-color:rgba(0,0,0,0.6); color:white; padding:25px; border-radius:15px;">
            <h2>🎵 Mood: <span style="color:#FFD700;">{mood}</span></h2>
            <h3>✨ Song: <a href="{song_link}" target="_blank" style="color:#4CAF50; text-decoration:none;">{song_name}</a></h3>
            <iframe width="360" height="215" src="{song_link.replace('watch?v=', 'embed/')}" frameborder="0" allowfullscreen></iframe>
            <p style="color:#ccc;">Enjoy the beat 🎧</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("No songs found for your selected mood and language!")

# 🎨 Footer
st.markdown("<hr><p style='text-align:center; color:gray;'>Built with ❤️ by Prem Kumar | Play It Bro 🎶</p>", unsafe_allow_html=True)

