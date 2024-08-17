import re
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from loader import db, bot
from data.config import ADMINS
from keyboards.default.JobButton import send_contact
from keyboards.inline.HomeButton import allRegionsKvartira


router = Router()

# Regular expression for validating phone numbers
PHONE_NUMBER_PATTERN = r"^\+\d{12,15}$"

@router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username

    await message.answer(
        "Телефон рақамингизни тасдиқланг", 
        parse_mode=ParseMode.MARKDOWN_V2, 
        reply_markup=send_contact
    )

    try:
        user = await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        print(error)
        return

    if user:
        count = await db.count_users()
        msg = (
            f"[{user['full_name']}](tg://user?id={user['telegram_id']}) "
            f"bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        )

        for admin in ADMINS:
            try:
                await bot.send_message(
                    chat_id=admin,
                    text=msg,
                    parse_mode=ParseMode.MARKDOWN_V2
                )
            except Exception as error:
                print(f"Data did not send to admin: {admin}. Error: {error}")

@router.message(F.content_type == types.ContentType.CONTACT)
async def check_contact(message: types.Message):
    contact = message.contact

    if contact.user_id == message.from_user.id:
        await message.answer("Hududni tanlang", reply_markup=allRegionsKvartira)
    else:
        await message.answer(
            "Please enter your own number or press the button below to share it again.",
            reply_markup=send_contact
        )

@router.message(F.content_type == types.ContentType.TEXT)
async def check_phone_number(message: types.Message):
    text = message.text
    # print(text)

    # Check if the text matches the phone number pattern
    if re.match(PHONE_NUMBER_PATTERN, text):
        await message.answer("Hududni tanlang", reply_markup=allRegionsKvartira)
    else:
        await message.answer(
            "Please enter a valid phone number or press the button below to share it.",
            reply_markup=send_contact
        )
