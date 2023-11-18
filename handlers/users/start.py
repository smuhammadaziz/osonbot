from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.JobButton import button
from aiogram.dispatcher.filters import Text
from loader import dp, bot

from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher import FSMContext

from keyboards.inline.HomeButton import start_button, allRegionsKvartira

start_word = "START"


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    pinned_message = await message.answer(text="ЭЪЛОН БЕРИШ", reply_markup=start_button)

    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    await bot.pin_chat_message(chat_id=message.chat.id, message_id=pinned_message.message_id)

    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@dp.callback_query_handler(text="botstarter", chat_type="private", state="*")
async def starter_bot(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Bot ishga tushdi")
    await state.finish()
    await call.message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@dp.message_handler(Text(startswith="START"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@dp.message_handler(Text(startswith="start"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@dp.message_handler(Text(startswith="/start"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@dp.message_handler(Text(startswith="/stop"), state="*")
async def stop(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Bot is stopping", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="/restart"), state="*")
async def restart(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Ҳудудни танланг:  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


