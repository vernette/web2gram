__all__ = ('router',)

from aiogram import Router

from routers.commands.base import router as base_commands_router
from routers.commands.user import router as user_commands_router

router = Router()
router.include_routers(base_commands_router, user_commands_router)
