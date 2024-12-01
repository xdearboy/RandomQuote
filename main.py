import logging
import os
from dotenv import load_dotenv
from clients.yandex_music_client import YandexMusicClient
from clients.lyrics_genius_client import LyricsGeniusClient
from services.random_quote import RandomQuote

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="[ # RandomQuote ] %(message)s",
)


def main():
    logging.info("Запускаем RandomQuote by xdearboy...")
    yandex_token = os.getenv("YANDEX_TOKEN")
    genius_access_token = os.getenv("GENIUS_ACCESS_TOKEN")
    yandex_client = YandexMusicClient(yandex_token)
    genius_client = LyricsGeniusClient(genius_access_token)
    random_quote = RandomQuote(yandex_client, genius_client)
    random_quote.generate_quote()


if __name__ == "__main__":
    main()
