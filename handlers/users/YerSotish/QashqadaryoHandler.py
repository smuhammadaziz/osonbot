from typing import List

from aiogram.bot.bot import types
from aiogram.dispatcher.dispatcher import FSMContext

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import valyutaButton, borYoq, documentButton
from loader import dp, bot
from states.YerSotish.QashqadaryoState import QashqadaryoYerSotish
from transliterate import to_cyrillic

mode = "Markdown"


@dp.callback_query_handler(text="qashqadaryoyer", state=None, chat_type="private")
async def first(callback_query: types.CallbackQuery):
    await callback_query.answer("Kvartira tanlandi")
    await callback_query.message.answer("<b> Расмларни жойлаш (2 - 10  тагача) </b>", parse_mode="HTML")
    await QashqadaryoYerSotish.images.set()


@dp.message_handler(is_media_group=True, state=QashqadaryoYerSotish.images, content_types=types.ContentTypes.ANY)
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
    await QashqadaryoYerSotish.next()


@dp.message_handler(lambda message: not message.text.replace('.', '').replace(',', '').isdigit(),
                    state=QashqadaryoYerSotish.umumiyMaydon)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=QashqadaryoYerSotish.umumiyMaydon)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text="<b> 🔥 Газ борми? </b>", parse_mode="HTML",
                           reply_markup=borYoq)
    await QashqadaryoYerSotish.next()


# ================================================================

@dp.callback_query_handler(text="bor", state=QashqadaryoYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text="yoq", state=QashqadaryoYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💡 Свет борми?", reply_markup=borYoq)
    await QashqadaryoYerSotish.next()

    # ========================================================================


@dp.callback_query_handler(text="bor", state=QashqadaryoYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text="yoq", state=QashqadaryoYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💦 Сув борми?", reply_markup=borYoq)
    await QashqadaryoYerSotish.next()


# ============================================================================

@dp.callback_query_handler(text="bor", state=QashqadaryoYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Сув ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text="yoq", state=QashqadaryoYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(
        text="Канализация борми?",
        reply_markup=borYoq)

    await QashqadaryoYerSotish.next()


# =============================================================

@dp.callback_query_handler(text="bor", state=QashqadaryoYerSotish.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Канализация ✔️"
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
        await QashqadaryoYerSotish.next()
    else:
        await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text="yoq", state=QashqadaryoYerSotish.kanal)
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
        await QashqadaryoYerSotish.next()
    else:
        await QashqadaryoYerSotish.next()


# ==============================================================

@dp.message_handler(state=QashqadaryoYerSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text="Ҳужжатлари борми?",
                         reply_markup=documentButton)

    await QashqadaryoYerSotish.next()


# ==========================================

@dp.callback_query_handler(text='dokumentBor', state=QashqadaryoYerSotish.hujjatlar, chat_type="private")
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = " Бор,  қонуний"
    await callback_query.answer("Dokument bor")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Қайси валютада нарх белгиламоқчисиз?",
                           reply_markup=valyutaButton)

    await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text='dokumentYoq', state=QashqadaryoYerSotish.hujjatlar, chat_type="private")
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = " Тайёр эмас"
    await callback_query.answer("dokumentYoq")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Қайси валютада нарх белгиламоқчисиз?",
                           reply_markup=valyutaButton)

    await QashqadaryoYerSotish.next()


# ==========================================

@dp.callback_query_handler(text='USD', state=QashqadaryoYerSotish.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await QashqadaryoYerSotish.next()


@dp.callback_query_handler(text='SUM', state=QashqadaryoYerSotish.valyuta, chat_type="private")
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text="Нархини ёзинг: ")

    await QashqadaryoYerSotish.next()


# =================================

@dp.message_handler(lambda message: not message.text.isdigit(), state=QashqadaryoYerSotish.narxi)
async def check_umumiy(message: types.Message):
    await message.reply("❗ Фақат рақамда ёзинг")


@dp.message_handler(state=QashqadaryoYerSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })
    await message.answer(text="Манзилни ёзинг: ")

    await QashqadaryoYerSotish.next()


@dp.message_handler(state=QashqadaryoYerSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text="Мўлжални ёзинг: ")

    await QashqadaryoYerSotish.next()


@dp.message_handler(state=QashqadaryoYerSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text="Телефон рақамини ёзинг: ")

    await QashqadaryoYerSotish.next()


@dp.message_handler(state=QashqadaryoYerSotish.telNumberOne)
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
        await QashqadaryoYerSotish.next()
    else:
        await QashqadaryoYerSotish.next()


@dp.message_handler(state=QashqadaryoYerSotish.telNumberTwo)
async def telNumbertwo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = types.MediaGroup()

    data = await state.get_data()

    photos = data['images']

    data1 = "#Қашқадарё__Вилояти \n"
    data2 = "#Ер_Участка__Сотилади \n\n"

    check_text = "Маълумотлар тўғрилигини тасдиқласангиз,  эълонни каналга жойланг"

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await QashqadaryoYerSotish.next()
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await QashqadaryoYerSotish.next()

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await QashqadaryoYerSotish.next()

    else:
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
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
        await QashqadaryoYerSotish.next()


@dp.message_handler(state=QashqadaryoYerSotish.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    channel_id = -1001964423395

    data1 = "#Қашқадарё__Вилояти \n"
    data2 = "#Ер_Участка__Сотилади \n\n"

    success_text = "✅ Эълон каналга жойланди!"

    data30 = "✅ <b>2-</b>Дақиқа ичида эълон беринг  \n\n"
    data31 = "✅ Ўзингиз Админ бўлинг  \n\n"
    data32 = "<b>✅ Эълон Бериш БЕПУЛ❗️  \n\n</b>"
    data33 = "       ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻\n"
    data34 = "    │<a href='https://t.me/OsonBozorBot'><b>    ЭЪЛОН БЕРИШ    </b></a>│\n"
    data35 = "       ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻\n\n"

    media_group = types.MediaGroup()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()
        else:
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [data1, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data30+data31+data32+data33+data34+data35

            media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.attach_photo(f"{file_id}")

            await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.finish()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.finish()
