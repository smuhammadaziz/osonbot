from aiogram.bot.bot import types
from aiogram.dispatcher.filters import Text

from keyboards.default.JobButton import button
from keyboards.inline.HomeButton import allRegionsKvartira, toshkentShHome, toshkentVilHome, andijonHome, \
    namanganHome, \
    fargonaHome, samarqandHome, buxoroHome, sirdaryoHome, qashqadaryoHome, surxonHome, navoiyHome, jizzaxHome, \
    xorazmHome, qoraqalpoqHome
from loader import dp, bot

mode = "Markdown"


# =======================================1=======================================
@dp.callback_query_handler(text="andijon", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Andijon tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=andijonHome, parse_mode="HTML")

# =======================================2========================================
@dp.callback_query_handler(text="buxoro", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Buxoro tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=buxoroHome, parse_mode="HTML")

# =======================================3========================================
@dp.callback_query_handler(text="fargona", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Farg'ona tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=fargonaHome, parse_mode="HTML")

# =======================================4========================================
@dp.callback_query_handler(text="jizzax", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Jizzax tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=jizzaxHome, parse_mode="HTML")

# =======================================5========================================
@dp.callback_query_handler(text="namangan", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Namangan tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=namanganHome, parse_mode="HTML")

# =======================================6========================================
@dp.callback_query_handler(text="navoiy", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Navoiy tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=navoiyHome, parse_mode="HTML")

# =======================================7========================================
@dp.callback_query_handler(text="qashqadaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Qashqadaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qashqadaryoHome, parse_mode="HTML")

# =======================================8========================================
@dp.callback_query_handler(text="qoraqalpoqosh", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Qoraqalpog'iston tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qoraqalpoqHome, parse_mode="HTML")

# =======================================9========================================
@dp.callback_query_handler(text="samarqand", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Samarqand tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=samarqandHome, parse_mode="HTML")

# =======================================10========================================
@dp.callback_query_handler(text="sirdaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Sirdaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=sirdaryoHome, parse_mode="HTML")

# =======================================11========================================
@dp.callback_query_handler(text="surxondaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Surxondaryo tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=surxonHome, parse_mode="HTML")

# =======================================12========================================
@dp.callback_query_handler(text="toshkentsh", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Toshkent Shahar tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentShHome, parse_mode="HTML")

# =======================================13========================================
@dp.callback_query_handler(text="toshkentvil", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Toshkent Viloyati tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentVilHome, parse_mode="HTML")

# =======================================14========================================
@dp.callback_query_handler(text="xorazm", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Xorazm tanlandi")
    await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=xorazmHome, parse_mode="HTML")

# ===================================--finish--=====================================



