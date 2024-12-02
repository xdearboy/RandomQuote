# RandomQuote

[![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000?style=for-the-badge)](https://github.com/charliermarsh/ruff)

## Описание

RandomQuote — это проект, который генерирует случайные цитаты из текстов песен, используя API Yandex Music и Genius. Программа ищет любимые треки пользователя на Yandex Music, получает текст песни с Genius и сохраняет случайные строки из текста в файл.
## Установка

1. **Клонируйте репозиторий:**

      ```bash
   git clone https://github.com/yourusername/RandomQuote.git
   cd RandomQuote
   ```

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установите необходимые зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env` в корне проекта и добавьте следующие переменные:**

   ```env
   YANDEX_TOKEN=your_yandex_music_api_token
   GENIUS_ACCESS_TOKEN=your_genius_api_access_token
   TELEGRAM_API_ID=your_telegram_api_id
   TELEGRAM_API_HASH=your_telegram_api_hash
   TELEGRAM_PHONE_NUMBER=your_phone_number
   ENABLE_LYRICS_TO_TG=true  # Или false, если не хотите включать аддон для Telegram.
   ```

## Использование

Запустите приложение, выполнив следующую команду:

```bash
python main.py
```

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробнее читайте в файле [LICENSE](LICENSE).

## Вклад в проект

Будем рады вашим улучшениям! Пожалуйста, создайте форк репозитория и отправьте pull request с вашими изменениями.



