from aiogram.bot.bot import types
from aiogram.dispatcher.filters import Text

from keyboards.default.JobButton import button
from keyboards.inline.HomeButton import allRegionsKvartira, toshkentShHome, toshkentVilHome, andijonHome, \
    namanganHome, \
    fargonaHome, samarqandHome, buxoroHome, sirdaryoHome, qashqadaryoHome, surxonHome, navoiyHome, jizzaxHome, \
    xorazmHome, qoraqalpoqHome
from loader import dp, bot
from check_user import check_andijon, button_andijon, check_buxoro, check_fargona, check_jizzax, check_namangan, \
    check_navoiy, check_qashqadaryo, check_qoraqalpoq, check_samarqand, check_sirdaryo, check_surxondaryo, \
    check_toshkentShUyBozor, check_toshkentVil, check_xorazm, button_buxoro, button_fargona, button_jizzax, \
    button_toshkentShUyBozor, button_namangan, button_navoiy, button_qashqadaryo, button_qoraqalpoq, button_samarqand, \
    button_sirdaryo, button_surxondaryo, button_toshkentVil, button_xorazm
from config import andijonLink, buxoroLink, fargonaLink, jizzaxLink, namanganLink, navoiyLink, qashqadaryoLink, \
    qoraqalpoqLink, samarqandLink, sirdaryoLink, surxondaryoLink, toshkentShUyBozorLink, toshkentVilLink, xorazmLink

mode = "Markdown"


@dp.message_handler(Text(startswith="УЙ-ЖОЙ БОЗОРИ"))
async def first(message: types.Message):
    await message.answer("<b> Ҳудудни танланг: </b>", reply_markup=allRegionsKvartira)


@dp.callback_query_handler(text="hometypeortgabutton", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    await call.answer("Категорияни танланг")
    await call.message.answer("<b> Категорияни танланг  </b>", reply_markup=button, parse_mode="HTML")


# =======================================1=======================================

@dp.callback_query_handler(text="andijon", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{andijonLink}", call.message.chat.id)

    if check_andijon(get_chat):
        await call.answer("Andijon tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=andijonHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_andijon())


@dp.callback_query_handler(text="check_andijon", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{andijonLink}", call.message.chat.id)
    if check_andijon(get_chat):
        await call.answer("Andijon tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=andijonHome, parse_mode="HTML")
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================2========================================
@dp.callback_query_handler(text="buxoro", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{buxoroLink}", call.message.chat.id)

    if check_buxoro(get_chat):
        await call.answer("Buxoro tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=buxoroHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_buxoro())


@dp.callback_query_handler(text="check_buxoro", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{buxoroLink}", call.message.chat.id)
    if check_buxoro(get_chat):
        await call.answer("Buxoro tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=buxoroHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================3========================================
@dp.callback_query_handler(text="fargona", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{fargonaLink}", call.message.chat.id)

    if check_fargona(get_chat):
        await call.answer("Fargona tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=fargonaHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_fargona())


@dp.callback_query_handler(text="check_fargona", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{fargonaLink}", call.message.chat.id)
    if check_fargona(get_chat):
        await call.answer("Fargona tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", parse_mode="HTML", reply_markup=fargonaHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================4========================================
@dp.callback_query_handler(text="jizzax", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{jizzaxLink}", call.message.chat.id)

    if check_jizzax(get_chat):
        await call.answer("Jizzax tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=jizzaxHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_jizzax())


@dp.callback_query_handler(text="check_jizzax", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{jizzaxLink}", call.message.chat.id)
    if check_jizzax(get_chat):
        await call.answer("Jizzax tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=jizzaxHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================5========================================
@dp.callback_query_handler(text="namangan", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{namanganLink}", call.message.chat.id)

    if check_namangan(get_chat):
        await call.answer("Namangan tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=namanganHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_namangan())


@dp.callback_query_handler(text="check_namangan", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{namanganLink}", call.message.chat.id)
    if check_namangan(get_chat):
        await call.answer("Namangan tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=namanganHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================6========================================
@dp.callback_query_handler(text="navoiy", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{navoiyLink}", call.message.chat.id)

    if check_navoiy(get_chat):
        await call.answer("Navoiy tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=navoiyHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_navoiy())


@dp.callback_query_handler(text="check_navoiy", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{navoiyLink}", call.message.chat.id)
    if check_navoiy(get_chat):
        await call.answer("Navoiy tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=navoiyHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================7========================================
@dp.callback_query_handler(text="qashqadaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{qashqadaryoLink}", call.message.chat.id)

    if check_qashqadaryo(get_chat):
        await call.answer("Qashqadaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qashqadaryoHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_qashqadaryo())


@dp.callback_query_handler(text="check_qashqadaryo", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{qashqadaryoLink}", call.message.chat.id)
    if check_qashqadaryo(get_chat):
        await call.answer("Qashqadaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=qashqadaryoHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================8========================================
@dp.callback_query_handler(text="qoraqalpoq", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{qoraqalpoqLink}", call.message.chat.id)

    if check_qoraqalpoq(get_chat):
        await call.answer("Qoraqalpog'iston tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=qoraqalpoqHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_qoraqalpoq())


@dp.callback_query_handler(text="check_qoraqalpoq", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{qoraqalpoqLink}", call.message.chat.id)
    if check_qoraqalpoq(get_chat):
        await call.answer("Qoraqalpog'iston tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=qoraqalpoqHome)

    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================9========================================
@dp.callback_query_handler(text="samarqand", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{samarqandLink}", call.message.chat.id)

    if check_samarqand(get_chat):
        await call.answer("Samarqand tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=samarqandHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_samarqand())


@dp.callback_query_handler(text="check_samarqand", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{samarqandLink}", call.message.chat.id)
    if check_samarqand(get_chat):
        await call.answer("Samarqand bosildi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=samarqandHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================10========================================
@dp.callback_query_handler(text="sirdaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{sirdaryoLink}", call.message.chat.id)

    if check_sirdaryo(get_chat):
        await call.answer("Sirdaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=sirdaryoHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_sirdaryo())


@dp.callback_query_handler(text="check_sirdaryo", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{sirdaryoLink}", call.message.chat.id)
    if check_sirdaryo(get_chat):
        await call.answer("Sirdaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=sirdaryoHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================11========================================
@dp.callback_query_handler(text="surxondaryo", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{surxondaryoLink}", call.message.chat.id)

    if check_surxondaryo(get_chat):
        await call.answer("Surxondaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=surxonHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_surxondaryo())


@dp.callback_query_handler(text="check_surxondaryo", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{surxondaryoLink}", call.message.chat.id)
    if check_surxondaryo(get_chat):
        await call.answer("Surxondaryo tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=surxonHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================12========================================
@dp.callback_query_handler(text="toshkentsh", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{toshkentShUyBozorLink}", call.message.chat.id)

    if check_toshkentShUyBozor(get_chat):
        await call.answer("Toshkent Shahar tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentShHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_toshkentShUyBozor())


@dp.callback_query_handler(text="check_toshkentShUyBozor", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{toshkentShUyBozorLink}", call.message.chat.id)
    if check_toshkentShUyBozor(get_chat):
        await call.answer("Toshkent Shahar tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=toshkentShHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================13========================================
@dp.callback_query_handler(text="toshkentvil", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{toshkentVilLink}", call.message.chat.id)

    if check_toshkentVil(get_chat):
        await call.answer("Toshkent Viloyati tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=toshkentVilHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_toshkentVil())


@dp.callback_query_handler(text="check_toshkentVil", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{toshkentVilLink}", call.message.chat.id)
    if check_toshkentVil(get_chat):
        await call.answer("Toshkent Viloyati tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=toshkentVilHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# =======================================14========================================
@dp.callback_query_handler(text="xorazm", chat_type="private")
async def kvartirasotish(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{xorazmLink}", call.message.chat.id)

    if check_xorazm(get_chat):
        await call.answer("Xorazm tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг!  </b>", reply_markup=xorazmHome, parse_mode="HTML")
    else:
        await bot.send_message(call.message.chat.id,
                               "Ботдан фойдаланиш учун каналга уланинг.",
                               parse_mode=mode, reply_markup=button_xorazm())


@dp.callback_query_handler(text="check_xorazm", chat_type="private")
async def check(call: types.CallbackQuery):
    get_chat = await bot.get_chat_member(f"@{xorazmLink}", call.message.chat.id)
    if check_xorazm(get_chat):
        await call.answer("Xorazm tanlandi")
        await call.message.answer("<b> Уй-жой турини танланг! </b>", parse_mode="HTML", reply_markup=xorazmHome)
    else:
        await call.answer("Каналга уланмадингиз ! ", show_alert=True)


# ===================================--finish--=====================================


@dp.message_handler(Text(startswith="⬅️ Ортга"))
async def ortga(message: types.Message):
    await message.answer("<b> Эълон бериш учун керакли бўлимни танланг! </b>", reply_markup=button, parse_mode="HTML")
