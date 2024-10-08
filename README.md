# TelegramAssistant

A Telegram bot assistant using python-telegram-bot.

## Local development

Run database:
```
docker-compose up -d db
```

Run migrations:
```
poetry run alembic upgrade head
```

Run bot:
```
poetry run python3 -m bot
```

## If models changed

Run migrations:
```
poetry run alembic revision --autogenerate -m "Migration: 0## Title"
poetry run alembic upgrade head
```


## Project Structure

- `__main__.py`: Entry point of the application
- `models.py`: SQLAlchemy models
- `settings.py`: Configuration and environment variables
- `handlers/`: Folder for bot command handlers

## Development


```
poetry run pre-commit run --all-files
```