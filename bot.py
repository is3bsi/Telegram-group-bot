import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 أهلاً بك في بوت المجموعة.\n"
        "البوت يعمل بنجاح ✅"
    )


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("""
📋 الأوامر الحالية

/start
/help

سيتم إضافة أوامر الإدارة والرتب قريبًا.
""")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
