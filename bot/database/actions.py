from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from bot.models import User
from bot.utils.logger import logger


async def add_or_update_user(
    session: AsyncSession,
    telegram_id: int,
    username: str,
    first_name: str,
    last_name: str,
) -> User:
    try:
        # Try to find the user
        stmt = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            # Update existing user
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
        else:
            # Create new user
            user = User(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            session.add(user)

        await session.commit()
        logger.info(f"User {user.telegram_id} added or updated in database")
        return user
    except IntegrityError:
        await session.rollback()
        raise
