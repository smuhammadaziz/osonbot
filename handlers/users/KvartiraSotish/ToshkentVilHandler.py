import logging
from typing import List

from aiogram.bot.bot import types
from aiogram.dispatcher.dispatcher import FSMContext

from keyboards.default.JobButton import checkbtn, button, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq, link_button
from loader import dp, bot
from states.KvartiraState.ToshVilState import ToshkentVilHomeSotish
from transliterate import to_cyrillic

mode = "Markdown"


@dp.callback_query_handler(text="toshvilkv", state=None, chat_type="private")
async def first(callback_query: types.CallbackQuery):
    await callback_query.answer("Kvartira tanlandi")
    await callback_query.message.answer("<b> Расмларни жойлаш (2 - 10  тагача) </b>", parse_mode="HTML")
    await ToshkentVilHomeSotish.images.set()


@dp.message_handler(is_media_group=True, state=ToshkentVilHomeSotish.images, content_types=types.ContentTypes.ANY)
async def starter(message: types.Message, album: List[types.Message], state: FSMContext):
    file_ids = []

    for photo in album:
        if photo:
            file_id = photo.photo[-1].file_id
            file_ids.append(file_id)

    await state.update_data({
        "images": file_ids
    })

    await message.answer("<b> Умумий майдонини ёзинг </b>", parse_mode="HTML")
    await ToshkentVilHomeSotish.next()


@dp.message_handler(lambda message: not message.text.replace('.', '').replace(',', '').isdigit(), state=ToshkentVilHomeSotish.umumiyMaydon)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotish.umumiyMaydon)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Хоналар сонини ёзинг: </b>", parse_mode="HTML")
    await ToshkentVilHomeSotish.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotish.xonalar)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotish.xonalar)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Нечанчи қаватда жойлашган?  </b>", parse_mode="HTML")
    await ToshkentVilHomeSotish.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotish.qavat)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotish.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Неча қаватлик бино?  </b>", parse_mode="HTML")
    await ToshkentVilHomeSotish.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotish.qavatlik)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotish.qavatlik)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qavatlik": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Ремонти қандай? </b>", parse_mode="HTML",
                           reply_markup=remontButton)
    await ToshkentVilHomeSotish.next()


# ====================================================================
@dp.callback_query_handler(text='Evroremont', state=ToshkentVilHomeSotish.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Евроремонт"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="Ta'mirlangan", state=ToshkentVilHomeSotish.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирланган"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="O'rtacha", state=ToshkentVilHomeSotish.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Ўртача"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="Ta'mirsiz", state=ToshkentVilHomeSotish.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирсиз"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotish.next()


# ===============================================================

@dp.callback_query_handler(text='Mavjud', state=ToshkentVilHomeSotish.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text='Jihozlarsiz', state=ToshkentVilHomeSotish.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()


# ================================================================

@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()

    # ========================================================================


@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotish.next()


# ============================================================================

@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Сув ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await ToshkentVilHomeSotish.next()
    else:
        await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await ToshkentVilHomeSotish.next()
    else:
        await ToshkentVilHomeSotish.next()


# ==============================================================

@dp.message_handler(state=ToshkentVilHomeSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text="Қайси валютада нарх белгиламоқчисиз?",
                         reply_markup=valyutaButton)

    await ToshkentVilHomeSotish.next()


# ==========================================

@dp.callback_query_handler(text='USD', state=ToshkentVilHomeSotish.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await ToshkentVilHomeSotish.next()


@dp.callback_query_handler(text='SUM', state=ToshkentVilHomeSotish.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await ToshkentVilHomeSotish.next()


# =================================

@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotish.narxi)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })
    await message.answer(text="Манзилни ёзинг: ")

    await ToshkentVilHomeSotish.next()


@dp.message_handler(state=ToshkentVilHomeSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text="Мўлжални ёзинг: ")

    await ToshkentVilHomeSotish.next()


@dp.message_handler(state=ToshkentVilHomeSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text="Телефон рақамини ёзинг: ")

    await ToshkentVilHomeSotish.next()


@dp.message_handler(state=ToshkentVilHomeSotish.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text="Зарур бўлса 2-рақамни киритинг,  \n\n  ёки 'Кейингиси'  тугмасини босинг",
                         reply_markup=otkazishButton)
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await ToshkentVilHomeSotish.next()
    else:
        await ToshkentVilHomeSotish.next()


@dp.message_handler(state=ToshkentVilHomeSotish.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = types.MediaGroup()

    data = await state.get_data()

    photos = data['images']

    data1 = "#Тошкент__Вилояти \n"
    data2 = "#Квартира__Сотилади \n\n"

    check_text = "Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг"

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await ToshkentVilHomeSotish.next()
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await ToshkentVilHomeSotish.next()

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await ToshkentVilHomeSotish.next()

    else:
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.attach_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.attach_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await ToshkentVilHomeSotish.next()


@dp.message_handler(state=ToshkentVilHomeSotish.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    channel_id = -1001916481063

    data1 = "#Тошкент__Вилояти \n"
    data2 = "#Квартира__Сотилади \n\n"

    bot_link = "ЭЪЛОН БЕРИШ"

    success_text = "✅ Эълон каналга жойланди!"

    media_group = types.MediaGroup()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            media_group.attach_photo(photos[0], caption=cyrillic_text)

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            media_group.attach_photo(photos[0], caption=cyrillic_text)

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            media_group.attach_photo(photos[0], caption=cyrillic_text)

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        else:
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            media_group.attach_photo(photos[0], caption=cyrillic_text)

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.finish()
