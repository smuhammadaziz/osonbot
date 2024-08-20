from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Ботни ишга тушириш"),
    ]

    group_commands = [
        BotCommand(command='/show', description="All Commands")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=group_commands, scope=BotCommandScopeAllGroupChats())
