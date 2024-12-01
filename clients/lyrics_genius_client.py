import logging
import random
import lyricsgenius


class LyricsGeniusClient:
    def __init__(self, access_token):
        self.genius = lyricsgenius.Genius(access_token)

    def get_random_lyrics(self, track, num_lines=3):
        logging.info(f"Ищем текст для {track.title} от {track.artists[0].name}...")
        song = self.genius.search_song(track.title, track.artists[0].name)
        if song and song.lyrics:
            lyrics = song.lyrics.split("\n")
            if len(lyrics) < num_lines:
                return "\n".join(lyrics)
            start_idx = random.randint(0, len(lyrics) - num_lines)
            random_lines = lyrics[start_idx : start_idx + num_lines]
            return "\n".join(random_lines)
        return None
