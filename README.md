# Telegram Bot Scaffold

A Telegram bot using python-telegram-bot.
Included:
- PostgreSQL Database & SQLAlchemy models
- Migrations with Alembic
- Pre-commit hooks with ruff

## Local development
Set up poetry:
```
poetry install --no-root && poetry shell
```

Get Telegram Bot Token from @BotFather.
Create `env.sh` file from `env_example.sh`.
Execute `source env.sh` to set environment variables.

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
