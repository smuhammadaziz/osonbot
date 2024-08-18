from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS
from utils.extra_datas import make_title

from keyboards.default.JobButton import send_contact
from keyboards.inline.HomeButton import allRegionsKvartira

router = Router()

@router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = str(message.chat.id)

    user = await db.get_one_user(chat_id=telegram_id)

    if user:
        await bot.send_message(chat_id=message.chat.id, text='Hududni tanlang:', reply_markup=allRegionsKvartira)
    else:
        await message.answer(f"Telefon raqamni tasdiqlang:", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=send_contact)

@router.message(F.content_type == types.ContentType.CONTACT)
async def check_contact(message: types.Message):
    if not message.contact:
        logger.info("No contact information found in the message.")
        return

    contact = str(message.contact.phone_number)  # Convert to string
    telegram_id = str(message.chat.id)
    full_name = message.from_user.full_name
    username = message.from_user.username if message.from_user.username else "null"  # Provide default value

    logger.info(f"Attempting to add user: {full_name}, {username}, {telegram_id}, {contact}")
    user = None

    try:
        user = await db.add_user(name=full_name, username=username, chat_id=telegram_id, phone=contact)
        if user:
            await bot.send_message(chat_id=message.chat.id, text='Hududni tanlang:', reply_markup=allRegionsKvartira)
        else:
            await bot.send_message(chat_id=message.chat.id, text='Telefon raqamni tasdiqlang', reply_markup=send_contact)
    except Exception as error:
        await bot.send_message(chat_id=message.chat.id, text='Telefon raqamni yuborish tugmasi orqali yuboring.')
