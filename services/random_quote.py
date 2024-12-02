import logging
import os
import random


class RandomQuote:
    def __init__(self, yandex_client, genius_client, output_file="random_lyrics.txt"):
        self.yandex_client = yandex_client
        self.genius_client = genius_client
        self.output_file = output_file

    def save_to_file(self, data):
        logging.info(f"Сохраняем кусочек текста {self.output_file}...")
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(data)

    def generate_quote(self):
        tracks = self.yandex_client.get_favorite_tracks()
        random_track = random.choice(tracks)
        lyrics = self.genius_client.get_random_lyrics(random_track)

        if lyrics:
            output = f"[Название: {random_track.title}] [Исполнитель: {random_track.artists[0].name}]\n{lyrics}\n\n[Создано с помощью RandomQuote]"
            self.save_to_file(output)
            logging.info(f"Текст сохранен в {os.path.abspath(self.output_file)}")
        else:
            logging.info("Текст не найден на Genius.")
