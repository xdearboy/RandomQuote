import logging
import os
import re

from dotenv import load_dotenv
from telethon import TelegramClient, functions

load_dotenv(dotenv_path="addons/.env")


async def update_profile_description(lyrics):
    api_id = int(os.getenv("TELEGRAM_API_ID"))
    api_hash = os.getenv("TELEGRAM_API_HASH")
    phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")

    client = TelegramClient(
        "RandomQuote",
        api_id,
        api_hash,
        device_model="Desktop",
        system_version="Windows 10",
        app_version="5.8.2",
        system_lang_code="ru",
        lang_code="ru",
    )
    await client.start()
    await client.sign_in(phone_number)

    lyrics = re.sub(r"\[.*?\]", "", lyrics)
    await client(functions.account.UpdateProfileRequest(about=lyrics[:70]))

    logging.info(f"Профиль обновлен с текстом: {lyrics[:70]}")

    await client.disconnect()
