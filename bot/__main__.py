from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import bot.settings as settings
from bot.utils.logger import logger
from bot.handlers.commands import start, help_command, echo


def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    logger.info("Starting bot")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
