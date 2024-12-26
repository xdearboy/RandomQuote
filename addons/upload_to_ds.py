import logging
import os
import re

import aiohttp
from dotenv import load_dotenv

load_dotenv(dotenv_path="addons/.env")


async def update_discord_bio(lyrics):
    token = os.getenv("DISCORD_TOKEN")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }

    url = "https://discord.com/api/v9/users/@me/profile"

    clean_lyrics = re.sub(r"\[.*?\]", "", lyrics)

    bio_content = clean_lyrics[:190]

    payload = {"bio": bio_content}

    async with aiohttp.ClientSession() as session:
        async with session.patch(url, json=payload, headers=headers) as response:
            if response.status == 200:
                logging.info("Дискорд био удачно было обновлено.")
            else:
                logging.error(
                    f"Дискорд био не удалось обновить: {await response.text()}"
                )
