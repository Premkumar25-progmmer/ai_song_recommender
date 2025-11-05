import streamlit as st
import random

# 🎵 Mood-based song database (expand later as needed)
songs_db = {
    "Happy": {
        "Telugu": ["Ma Ma Mahesha - Sarkaru Vaari Paata", "Whattey Beauty - Bheeshma", "Rowdy Baby - Maari 2"],
        "Hindi": ["Kala Chashma - Baar Baar Dekho", "Kar Gayi Chull - Kapoor & Sons", "Dil Dhadakne Do - Zindagi Na Milegi Dobara"],
        "Tamil": ["Vaathi Coming - Master", "Jimikki Kammal - Velipadinte Pusthakam", "Arabic Kuthu - Beast"]
    },
    "Sad": {
        "Telugu": ["Samajavaragamana - Ala Vaikunthapurramuloo", "Nee Kallu Neeli Samudram - Uppena", "The Life of Ram - Jaanu"],
        "Hindi": ["Channa Mereya - Ae Dil Hai Mushkil", "Agar Tum Saath Ho - Tamasha", "Tera Ban Jaunga - Kabir Singh"],
        "Tamil": ["Enna Solla Pogirai - Kandukondain Kandukondain", "Vaseegara - Minnale", "Pogiren - Anniyan"]
    },
    "Romantic": {
        "Telugu": ["Inkem Inkem Inkem Kaavaale - Geetha Govindam", "Butta Bomma - Ala Vaikunthapurramuloo", "Priyathama Priyathama - Majili"],
        "Hindi": ["Tum Hi Ho - Aashiqui 2", "Raabta - Agent Vinod", "Pehla Nasha - Jo Jeeta Wohi Sikandar"],
        "Tamil": ["Anbe En Anbe - Dhaam Dhoom", "Kanave Kanave - David", "Munbe Vaa - Sillunu Oru Kadhal"]
    },
    "Energetic": {
        "Telugu": ["Ramuloo Ramulaa - Ala Vaikunthapurramuloo", "Mind Block - Sarileru Neekevvaru", "Dhinka Chika - Ready"],
        "Hindi": ["Naatu Naatu - RRR", "Malhari - Bajirao Mastani", "Zinda - Bhaag Milkha Bhaag"],
        "Tamil": ["Aalaporan Thamizhan - Mersal", "Surviva - Vivegam", "Verithanam - Bigil"]
    }
}

# 🎧 App title
st.markdown("""
    <h1 style='text-align:center; color:#FF4081;'>
        🎶 Play It Bro - Mood Based Song Recommender 🎵
    </h1>
""", unsafe_allow_html=True)

st.write("#### Let's find the perfect song for your mood!")

# 🎭 Mood selection
mood = st.radio(
    "Select your mood:",
    list(songs_db.keys()),
    horizontal=True,
    key="mood_selector"
)

# 🌐 Language selection - multiselect with attractive tags
languages = st.multiselect(
    "Choose your preferred languages:",
    ["Telugu", "Hindi", "Tamil"],
    default=["Telugu"]
)

# 🎵 Generate button
if st.button("🎧 Recommend Me a Song"):
    selected_songs = []
    for lang in languages:
        if lang in songs_db[mood]:
            selected_songs += songs_db[mood][lang]
    
    if selected_songs:
        song = random.choice(selected_songs)
        st.markdown(f"""
        <div style="text-align:center; background-color:#2C2C2C; color:#FFFFFF; padding:25px; border-radius:15px; margin-top:20px;">
            <h2>🎶 Your Mood: <span style="color:#FFD700;">{mood}</span></h2>
            <h3>✨ Suggested Song: <span style="color:#4CAF50;">{song}</span></h3>
            <p style="font-size:14px; color:#AAAAAA;">Enjoy your vibe! 🎧</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("No songs available for the selected mood and language combination. Try another one!")

# 🎨 Footer
st.markdown("""
    <hr>
    <p style='text-align:center; color:gray;'>
        Built with ❤️ by Prem Kumar | Play It Bro 🎶
    </p>
""", unsafe_allow_html=True)
