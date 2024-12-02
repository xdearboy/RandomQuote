import logging
import re

from telethon import TelegramClient, functions


async def update_profile_description(lyrics, api_id, api_hash, phone_number):
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
