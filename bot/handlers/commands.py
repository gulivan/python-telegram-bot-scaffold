from telegram import Update, ForceReply
from telegram.ext import ContextTypes
from bot.database.actions import add_or_update_user
from bot.models import get_db
from bot.utils.logger import logger
from bot.utils.translations import get_translation


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued and save user data."""
    user = update.effective_user

    async with get_db() as db:
        try:
            await add_or_update_user(
                db,
                telegram_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            message = get_translation("start_message", user=user.mention_html())
            await update.message.reply_html(
                message,
                reply_markup=ForceReply(selective=True),
            )
            logger.info(f"Sent message to {user.id}: {message}")
        except Exception as e:
            await update.message.reply_text(
                get_translation("error_message", error=str(e))
            )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(get_translation("help_message"))


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
