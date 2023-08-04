import logging
from typing import List

from aiogram.bot.bot import types
from aiogram.dispatcher.dispatcher import FSMContext

from keyboards.default.JobButton import checkbtn, button, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq, link_button
from loader import dp, bot
from states.HovliState.ToshVilState import ToshkentVilHomeSotishHovli
from transliterate import to_cyrillic

mode = "Markdown"


@dp.callback_query_handler(text="toshvilhovli", state=None, chat_type="private")
async def first(callback_query: types.CallbackQuery):
    await callback_query.answer("Hovli tanlandi")
    await callback_query.message.answer("<b> Умумий майдонини ёзинг </b>", parse_mode="HTML")
    await ToshkentVilHomeSotishHovli.umumiyMaydon.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotishHovli.umumiyMaydon)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotishHovli.umumiyMaydon)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Хоналар сонини ёзинг: </b>", parse_mode="HTML")
    await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotishHovli.xonalar)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotishHovli.xonalar)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Ошхона борми?  </b>", parse_mode="HTML",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


# =================================================
@dp.callback_query_handler(text='bor', state=ToshkentVilHomeSotishHovli.oshxona, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Ҳаммоми борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text='yoq', state=ToshkentVilHomeSotishHovli.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "oshxona": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Ҳаммоми борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text='bor', state=ToshkentVilHomeSotishHovli.hammom, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Неча қаватлик?")
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text='yoq', state=ToshkentVilHomeSotishHovli.hammom, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "hammom": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Неча қаватлик?")
    await ToshkentVilHomeSotishHovli.next()


# ==============================================================


@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotishHovli.qavat)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotishHovli.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> Ремонти қандай?  </b>", parse_mode="HTML",
                           reply_markup=remontButton)
    await ToshkentVilHomeSotishHovli.next()


# ====================================================================
@dp.callback_query_handler(text='Evroremont', state=ToshkentVilHomeSotishHovli.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Евроремонт"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="Ta'mirlangan", state=ToshkentVilHomeSotishHovli.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирланган"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="O'rtacha", state=ToshkentVilHomeSotishHovli.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Ўртача"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="Ta'mirsiz", state=ToshkentVilHomeSotishHovli.remont, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Таъмирсиз"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Жиҳозлари борми?",
                           reply_markup=jihozlarButton)
    await ToshkentVilHomeSotishHovli.next()


# ===============================================================

@dp.callback_query_handler(text='Mavjud', state=ToshkentVilHomeSotishHovli.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text='Jihozlarsiz', state=ToshkentVilHomeSotishHovli.jihozlar, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="🔥 Газ борми?",
                           reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


# ================================================================

@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotishHovli.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()

    # ========================================================================


@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotishHovli.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await ToshkentVilHomeSotishHovli.next()


# ============================================================================

@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Сув ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotishHovli.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="bor", state=ToshkentVilHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Канализация  ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await ToshkentVilHomeSotishHovli.next()
    else:
        await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text="yoq", state=ToshkentVilHomeSotishHovli.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(
        text="Қўшимча маълумотингиз бўлса,  ёзишингиз мумкин.  \n\n Йўқ бўлса 'Кейингиси' тугмасини босинг",
        reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await ToshkentVilHomeSotishHovli.next()
    else:
        await ToshkentVilHomeSotishHovli.next()


# ==============================================================

@dp.message_handler(state=ToshkentVilHomeSotishHovli.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text="Қайси валютада нарх белгиламоқчисиз?",
                         reply_markup=valyutaButton)

    await ToshkentVilHomeSotishHovli.next()


# ==========================================

@dp.callback_query_handler(text='USD', state=ToshkentVilHomeSotishHovli.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await ToshkentVilHomeSotishHovli.next()


@dp.callback_query_handler(text='SUM', state=ToshkentVilHomeSotishHovli.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await ToshkentVilHomeSotishHovli.next()


# =================================

@dp.message_handler(lambda message: not message.text.isdigit(), state=ToshkentVilHomeSotishHovli.narxi)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=ToshkentVilHomeSotishHovli.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "narxi": text
    })
    await message.answer(text="Манзилни ёзинг: ")

    await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(state=ToshkentVilHomeSotishHovli.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text="Мўлжални ёзинг: ")

    await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(state=ToshkentVilHomeSotishHovli.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text="Телефон рақамини ёзинг: ")

    await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(state=ToshkentVilHomeSotishHovli.telNumberOne)
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
        await ToshkentVilHomeSotishHovli.next()
    else:
        await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(state=ToshkentVilHomeSotishHovli.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })
    await message.answer(text="Расмларни жойлаш (10 - тагача)")

    await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(is_media_group=True, state=ToshkentVilHomeSotishHovli.images,
                    content_types=types.ContentTypes.PHOTO)
async def images(message: types.Message, album: List[types.Message], state: FSMContext):
    chat_id = message.chat.id
    media_group = types.MediaGroup()

    for obj in album:
        if obj.content_type == 'photo':
            if obj.photo:
                file_id = obj.photo[-1].file_id
            else:
                file_id = obj[obj.content_type].file_id
            try:
                media_group.attach({"media": file_id,
                                    "type": obj.content_type,
                                    "caption": obj.caption})

            except Exception as err:
                logging.exception(err)
                return await message.answer("Бундай файл юклаб бўлмайди")
        else:
            await message.reply("❗ Расмдан бошқа файл турини юклай олмайсиз")

    await state.update_data({
        'images': media_group
    })

    data = await state.get_data()

    data1 = "#Тошкент__Вилояти \n"
    data2 = "#Ҳовли_Уй__Сотилади \n\n"

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
        await bot.send_message(chat_id=chat_id,
                               text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
        await ToshkentVilHomeSotishHovli.next()
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
        await bot.send_message(chat_id=chat_id,
                               text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
        await ToshkentVilHomeSotishHovli.next()

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
        await bot.send_message(chat_id=chat_id,
                               text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
        await ToshkentVilHomeSotishHovli.next()

    else:
        data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
        hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
        data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
        data7 = "🔷 Ремонти: " + data['remont'] + "\n"
        data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔷 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                  data10,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text, reply_markup=checkbtn)
        await bot.send_message(chat_id=chat_id,
                               text="Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг")
        await ToshkentVilHomeSotishHovli.next()


@dp.message_handler(state=ToshkentVilHomeSotishHovli.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    channel_id = -1001916481063

    data1 = "#Тошкент__Вилояти \n"
    data2 = "#Ҳовли_Уй__Сотилади \n\n"

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        media_group = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text, parse_mode="HTML", reply_markup=link_button)
            await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=start)
            await state.finish()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text, parse_mode="HTML", reply_markup=link_button)
            await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=start)
            await state.finish()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text, parse_mode="HTML", reply_markup=link_button)
            await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=start)
            await state.finish()
        else:
            data3 = "🔷 Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data4 = "🔷 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            oshxona = "🔷 Ошхонаси: " + data['oshxona'] + "\n"
            hammom = "🔷 Ҳаммоми: " + data['hammom'] + "\n"
            data6 = "🔷 Неча қаватли: " + data['qavat'] + "-қаватли уй" + "\n"
            data7 = "🔷 Ремонти: " + data['remont'] + "\n"
            data8 = "🔷 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔷 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            data11 = "🔷 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💰 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data4, oshxona, hammom, data6, data7, data8, data9, gaz, svet, suv, kanal,
                      data10,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text, parse_mode="HTML", reply_markup=link_button)
            await bot.send_message(chat_id=chat_id, text="✅ Эълон каналга жойланди!", reply_markup=start)
            await state.finish()

    else:
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.finish()
