import asyncio
import importlib.util
import logging
import os

from dotenv import load_dotenv

from clients.lyrics_genius_client import LyricsGeniusClient
from clients.yandex_music_client import YandexMusicClient
from services.random_quote import RandomQuote

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="[ # RandomQuote ] %(message)s",
)


def load_addons(addons_folder="Addons"):
    addons = {}
    for filename in os.listdir(addons_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(addons_folder, filename)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            addons[module_name] = module
    return addons


async def main():
    logging.info("Запускаем RandomQuote by xdearboy...")
    yandex_token = os.getenv("YANDEX_TOKEN")
    genius_access_token = os.getenv("GENIUS_ACCESS_TOKEN")
    enable_lyrics_to_tg = os.getenv("ENABLE_LYRICS_TO_TG", "false").lower() == "true"
    yandex_client = YandexMusicClient(yandex_token)
    genius_client = LyricsGeniusClient(genius_access_token)
    random_quote = RandomQuote(yandex_client, genius_client)
    random_quote.generate_quote()

    addons = load_addons()
    if enable_lyrics_to_tg and "lyrics_to_tg" in addons:
        api_id = int(os.getenv("TELEGRAM_API_ID"))
        api_hash = os.getenv("TELEGRAM_API_HASH")
        phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")

        with open("random_lyrics.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        lyrics = " ".join(lines[2:])

        if lyrics:
            await addons["lyrics_to_tg"].update_profile_description(
                lyrics, api_id, api_hash, phone_number
            )
        else:
            print("[ # RandomQuote ] Текст не найден, не отправляем в Telegram.")


if __name__ == "__main__":
    asyncio.run(main())
