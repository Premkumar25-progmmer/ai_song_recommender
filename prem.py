"""
fetch_100_songs.py

Produces songs_100.csv with columns:
title,artist,youtube_url,spotify_id,mood

Requires:
pip install spotipy pandas
A Spotify developer client id/secret (set below).
"""

import os
import csv
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from typing import List, Tuple

# ---------- CONFIG ----------
SPOTIFY_CLIENT_ID = "YOUR_CLIENT_ID_HERE"
SPOTIFY_CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
OUTPUT_CSV = "songs_100.csv"

# Moods and example search keywords (used to find relevant tracks)
MOOD_KEYWORDS = {
    "Happy": [
        "happy", "feel good", "party", "dance", "uplifting", "pop hit", "summer"
    ],
    "Sad": [
        "sad", "ballad", "melancholy", "heartbreak", "slow", "emotional"
    ],
    "Energetic": [
        "energetic", "upbeat", "workout", "party banger", "hit", "dance"
    ],
    "Romantic": [
        "romantic", "love song", "romance", "romantic ballad", "slow love"
    ]
}

# How many songs per mood to collect (sum should be >= 100)
PER_MOOD = 25  # 25 * 4 = 100

# ---------- Spotify client ----------
if SPOTIFY_CLIENT_ID == "YOUR_CLIENT_ID_HERE" or SPOTIFY_CLIENT_SECRET == "YOUR_CLIENT_SECRET_HERE":
    raise SystemExit("Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in this script before running.")

auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=10, retries=3, status_retries=3)

def search_tracks_for_keyword(keyword: str, limit: int = 20) -> List[dict]:
    """Search Spotify for tracks matching a keyword."""
    q = f"{keyword}"
    try:
        res = sp.search(q=q, type="track", limit=limit)
    except Exception as e:
        print("Spotify search error:", e)
        return []
    items = res.get("tracks", {}).get("items", [])
    return items

def collect_mood_tracks(mood: str, keywords: List[str], need: int) -> List[Tuple[str,str,str,str]]:
    """Collect unique tracks for a mood using several keywords.
    Returns list of tuples: (title, artist, spotify_track_id, youtube_search_url)
    """
    collected = []
    seen_track_ids = set()
    # Try each keyword (broaden search)
    for kw in keywords:
        if len(collected) >= need:
            break
        items = search_tracks_for_keyword(kw, limit=30)
        for it in items:
            tid = it.get("id")
            if not tid or tid in seen_track_ids:
                continue
            name = it.get("name", "").strip()
            artists = ", ".join([a["name"] for a in it.get("artists", [])])
            # Construct YouTube search URL (safe fallback)
            yt_search_query = f"{name} {artists}"
            youtube_search_url = f"https://www.youtube.com/results?search_query={requests_quote(yt_search_query)}"
            collected.append((name, artists, youtube_search_url, tid))
            seen_track_ids.add(tid)
            if len(collected) >= need:
                break
        # small pause to be polite
        time.sleep(0.25)
    return collected

def requests_quote(s: str) -> str:
    # simple URL-encoding for query
    from urllib.parse import quote_plus
    return quote_plus(s)

def main():
    all_rows = []
    print("Collecting songs from Spotify...")
    for mood, keywords in MOOD_KEYWORDS.items():
        print(f" - Mood: {mood}")
        targets = PER_MOOD
        mood_tracks = collect_mood_tracks(mood, keywords, targets)
        print(f"   collected {len(mood_tracks)} for {mood}")
        for (title, artist, yt_search, spid) in mood_tracks:
            # Save as: title, artist, youtube_url (search), spotify_id, mood
            all_rows.append({
                "title": title,
                "artist": artist,
                "youtube_url": yt_search,
                "spotify_id": spid,
                "mood": mood
            })

    # If we didn't reach 100 exactly (due to de-duping), pad by searching top playlists
    total = len(all_rows)
    print(f"Total collected: {total}")
    if total < 100:
        # try fetching top tracks from global playlists
        need_more = 100 - total
        print(f"Need {need_more} more tracks — pulling from 'Top 50 Global' playlist")
        try:
            # Spotify's Top 50 global playlist id
            top50_playlist_id = "37i9dQZEVXbMDoHDwVN2tF"  # may change; fallback to charts
            playlist = sp.playlist_tracks(top50_playlist_id, limit=100)
            for item in playlist.get("items", []):
                track = item.get("track")
                if not track:
                    continue
                tid = track.get("id")
                if tid in [r["spotify_id"] for r in all_rows]:
                    continue
                name = track.get("name")
                artists = ", ".join([a["name"] for a in track.get("artists", [])])
                yt_search = f"https://www.youtube.com/results?search_query={requests_quote(name + ' ' + artists)}"
                # assign leftover tracks to 'Happy' by default (or cycle moods)
                mood_assign = "Happy" if len(all_rows) % 4 == 0 else ["Happy","Sad","Energetic","Romantic"][len(all_rows) % 4]
                all_rows.append({
                    "title": name,
                    "artist": artists,
                    "youtube_url": yt_search,
                    "spotify_id": tid,
                    "mood": mood_assign
                })
                if len(all_rows) >= 100:
                    break
            print(f"After padding, total = {len(all_rows)}")
        except Exception as e:
            print("Could not fetch playlist for padding:", e)

    # Trim to exactly 100
    all_rows = all_rows[:100]

    # Write CSV
    df = pd.DataFrame(all_rows, columns=["title","artist","youtube_url","spotify_id","mood"])
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Wrote {len(df)} rows to {OUTPUT_CSV} — open that CSV and upload to your Streamlit app.")

if __name__ == "__main__":
    main()
