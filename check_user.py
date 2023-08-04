from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import andijonLink, buxoroLink, fargonaLink, jizzaxLink, namanganLink, navoiyLink, qashqadaryoLink, qoraqalpoqLink, samarqandLink, sirdaryoLink, surxondaryoLink, toshkentShUyBozorLink, toshkentVilLink, xorazmLink

andijonLink = f"https://t.me/{andijonLink}"
buxoroLink = f"https://t.me/{buxoroLink}"
fargonaLink = f"https://t.me/{fargonaLink}"
jizzaxLink = f"https://t.me/{jizzaxLink}"
namanganLink = f"https://t.me/{namanganLink}"
navoiyLink = f"https://t.me/{navoiyLink}"
qashqadaryoLink = f"https://t.me/{qashqadaryoLink}"
qoraqalpoqLink = f"https://t.me/{qoraqalpoqLink}"
samarqandLink = f"https://t.me/{samarqandLink}"
sirdaryoLink = f"https://t.me/{sirdaryoLink}"
surxondaryoLink = f"https://t.me/{surxondaryoLink}"
toshkentShUyBozorLink = f"https://t.me/{toshkentShUyBozorLink}"
toshkentVilLink = f"https://t.me/{toshkentVilLink}"
xorazmLink = f"https://t.me/{xorazmLink}"


def check_andijon(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_andijon():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=andijonLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_andijon")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_buxoro(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_buxoro():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=buxoroLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_buxoro")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_fargona(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_fargona():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=fargonaLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_fargona")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_jizzax(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_jizzax():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=jizzaxLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_jizzax")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_namangan(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_namangan():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=namanganLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_namangan")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_navoiy(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_navoiy():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=navoiyLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_navoiy")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_qashqadaryo(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_qashqadaryo():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=qashqadaryoLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_qashqadaryo")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_qoraqalpoq(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_qoraqalpoq():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=qoraqalpoqLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_qoraqalpoq")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_samarqand(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_samarqand():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=samarqandLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_samarqand")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_sirdaryo(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_sirdaryo():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=sirdaryoLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_sirdaryo")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_surxondaryo(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_surxondaryo():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=surxondaryoLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_surxondaryo")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_toshkentShUyBozor(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_toshkentShUyBozor():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=toshkentShUyBozorLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_toshkentShUyBozor")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_toshkentVil(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_toshkentVil():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=toshkentVilLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_toshkentVil")
    main.add(button1, button2)
    return main


# =============================================================================================

def check_xorazm(member):
    if member["status"] != "left":
        return True
    else:
        return False


def button_xorazm():
    main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text="✅ Каналга обуна бўлинг", url=xorazmLink)
    button2 = InlineKeyboardButton(text="✅ Тасдиқланг", callback_data="check_xorazm")
    main.add(button1, button2)
    return main

# =============================================================================================