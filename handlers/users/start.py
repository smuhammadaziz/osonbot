from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.JobButton import button
from aiogram.dispatcher.filters import Text
from loader import dp

from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher import FSMContext

start_word = "START"


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("<b> Категорияни танланг  </b>", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="START"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Категорияни танланг </b>", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="start"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Категорияни танланг </b>", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="/start"), state="*")
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Категорияни танланг </b>", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="/stop"), state="*")
async def stop(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Bot is stopping", reply_markup=button, parse_mode="HTML")


@dp.message_handler(Text(startswith="/restart"), state="*")
async def restart(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b> Категорияни танланг </b>", reply_markup=button, parse_mode="HTML")
