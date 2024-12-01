import logging
import yandex_music


class YandexMusicClient:
    def __init__(self, token):
        self.client = yandex_music.Client(token).init()

    def get_favorite_tracks(self):
        logging.info("Ищем любимые треки...")
        favorite_tracks = self.client.users_likes_tracks()
        track_ids = [item.track_id for item in favorite_tracks]
        tracks = self.client.tracks(track_ids)
        return tracks
