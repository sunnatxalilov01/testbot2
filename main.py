import telebot
from telebot import types
bot = telebot.TeleBot('1028581280:AAGmb7zV9upBKnEuixnrFjnfZM8tQzzsvHs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("o'zbek tili")
    btn2 = types.KeyboardButton("русский язык")
    markup.add(btn1, btn2)
    send_mess = f"<b>Assalomu Alaykum {message.from_user.first_name} {message.from_user.last_name}"   \
                f"</b>\n\nBu Bot yordamida sizga kereli bolgan\nxar-xil turdegi mebellarni topishingiz mumkin" \
                f"<b>\n\nздрасвуйте. {message.from_user.first_name} {message.from_user.last_name}" \
                f"</b>\n\nДобро пожаловать в.\nС этим ботом вы можете найти все виды мебели, которые вам нужны"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("saytga kirin", callback_data="good")),
    bot.send_message(message.chat.id, "yaxshi tanlov", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['web'])
def open_web(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "https://telegra.ph/Katalog-Cvetov-12-08", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['catalog'])
def open_catalog(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "https://telegra.ph/Katalog-Cvetov-12-08", parse_mode='html',reply_markup=markup)



@bot.message_handler(content_types=['Sunnat'])
def open_Sunnat(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "https://telegra.ph/Katalog-Cvetov-12-08", parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()





# 1 bo'lim -------------------------------------------------------------------------------------------------------------
# uzb ------------------------------------------------------------------------------------------------------------------

    if get_message_bot == "o'zbek tili":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("tayyor mebellar")
        btn2 = types.KeyboardButton("zakaz mebel")
        btn3 = types.KeyboardButton("list ranglari")
        btn4 = types.KeyboardButton("manzillarimiz")
        btn5 = types.KeyboardButton("start")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "o'zbek tili"

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "русский язык":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("готовая мебель")
        btn2 = types.KeyboardButton("заказ мебель")
        btn3 = types.KeyboardButton("список цветов")
        btn4 = types.KeyboardButton("наши адреса")
        btn5 = types.KeyboardButton("start")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "русский язык."
# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("o'zbek tili")
        btn2 = types.KeyboardButton("русский язык")
        markup.add(btn1, btn2)
        final_message = f"<b>Assalomu Alaykum {message.from_user.first_name} {message.from_user.last_name}" \
                        f"</b>\n\nBu Bot yordamida sizga kereli bolgan\nxar-xil turdegi mebellarni topishingiz mumkin" \
                        f"<b>\n\nздрасвуйте. {message.from_user.first_name} {message.from_user.last_name}" \
                        f"</b>\n\nДобро пожаловать в.\nС этим ботом вы можете найти все виды мебели, которые вам нужны"

# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "tayyor mebellar":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("oshxona")
        btn2 = types.KeyboardButton("ofis")
        btn3 = types.KeyboardButton("garderop")
        btn4 = types.KeyboardButton("yotoq xona")
        btn5 = types.KeyboardButton("bolalar xonasi")
        btn6 = types.KeyboardButton("zal")
        btn7 = types.KeyboardButton("bog'cha")
        btn8 = types.KeyboardButton("maktab")
        btn9 = types.KeyboardButton("ishxonalar")
        btn10 = types.KeyboardButton("boshq turdegi")
        btn11 = types.KeyboardButton("orqaga")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "tayyor mebellar saxifasi tanlandi.\n\ntayyor mebellar kataloglari:\n" \
                        "bu yerda siz ozingizga kerak bolgan tayyor mebillar toplamini tanlashingiz mumkin."

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "готовая мебель":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("кухня")
        btn2 = types.KeyboardButton("офис")
        btn3 = types.KeyboardButton("гардероб")
        btn4 = types.KeyboardButton("спальная")
        btn5 = types.KeyboardButton("детская")
        btn6 = types.KeyboardButton("зал")
        btn7 = types.KeyboardButton("детский сад")
        btn8 = types.KeyboardButton("школа")
        btn9 = types.KeyboardButton("для бизнеса")
        btn10 = types.KeyboardButton("другой тип")
        btn11 = types.KeyboardButton("назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "выбрана страница готовой мебели.\n\nКаталоги готовой мебели:\n" \
                        "Здесь вы можете выбрать необходимый набор готовой мебели."

# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "zakaz mebel":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🇺🇿 sunnat\n+998935244188")
        btn2 = types.KeyboardButton("🇷🇺 aziz\n+998909090522")
        btn3 = types.KeyboardButton("orqaga")
        markup.add(btn1, btn2, btn3)
        final_message = "zakaz bermiqchisiz:\n\nbiz bilan boglaninig."

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "заказ мебель":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🇺🇿 Cуннат\n+998935244188")
        btn2 = types.KeyboardButton("🇷🇺 Азиз\n+998909090522")
        btn3 = types.KeyboardButton("назад")
        markup.add(btn1, btn2, btn3)
        final_message = "Вы хотите заказать:\n\nсвяжитесь с нами."

# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "list ranglari":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("orqaga")
        markup.add(btn1)
        final_message = "cataloglarimiz"
        bot.send_message(message.chat.id, "https://telegra.ph/Katalog-Cvetov-12-08", parse_mode='html', reply_markup=markup)

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "список цветов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("назад")
        markup.add(btn1)
        final_message = "наши каталоги"
        bot.send_message(message.chat.id, "https://telegra.ph/Katalog-Cvetov-12-08", parse_mode='html', reply_markup=markup)

# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "manzillarimiz":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("📍 sizning manzilingiz", request_location=True)
        btn2 = types.KeyboardButton("tel nomeringiz", request_contact=True)
        btn3 = types.KeyboardButton("orqaga")
        markup.add(btn1, btn2, btn3)
        final_message = "catalog."
        bot.send_message(message.chat.id, "https://maps.google.com/maps?q=41.218215,69.329599&ll=41.218215,69.329599&z=16", parse_mode='html', reply_markup=markup)

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "наши адреса":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("📍 ваш адрес", request_location=True)
        btn2 = types.KeyboardButton("ваш номер телефона", request_contact=True)
        btn3 = types.KeyboardButton("назад")
        markup.add(btn1, btn2, btn3)
        final_message = "наш адрес"
        bot.send_message(message.chat.id, "https://maps.google.com/maps?q=41.218215,69.329599&ll=41.218215,69.329599&z=16", parse_mode='html', reply_markup=markup)

# rus ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("готовая мебель")
        btn2 = types.KeyboardButton("заказ мебель")
        btn3 = types.KeyboardButton("список цветов")
        btn4 = types.KeyboardButton("наши адреса")
        btn5 = types.KeyboardButton("start")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "меню."

# 2 bo'lim -------------------------------------------------------------------------------------------------------------
# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "oshxona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("1 oshxona")
        btn2 = types.KeyboardButton("2 oshxona")
        btn3 = types.KeyboardButton("3 oshxona")
        btn4 = types.KeyboardButton("4 oshxona")
        btn5 = types.KeyboardButton("< orqaga")
        markup.add(btn1, btn2, btn3,btn4, btn5)
        final_message = "oshxona"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 oshxona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 oshxona"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/8",  "OS-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/9",  "OS-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/10", "OS-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/11", "OS-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/12", "OS-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/13", "OS-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/14", "OS-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/15", "OS-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/16", "OS-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/17", "OS-10", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/18", "OS-11", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/19", "OS-12", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/20", "OS-13", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/21", "OS-14", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 oshxona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 oshxona"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/23", "OS-15", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/24", "OS-16", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/25", "OS-17", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/26", "OS-18", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/27", "OS-19", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/28", "OS-20", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/29", "OS-21", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/30", "OS-22", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/31", "OS-23", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/32", "OS-24", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/33", "OS-25", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/34", "OS-26", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/35", "OS-27", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/36", "OS-28", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 oshxona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 oshxona"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/38", "OS-29", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/39", "OS-30", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/40", "OS-31", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/41", "OS-32", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/42", "OS-33", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/43", "OS-34", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/44", "OS-35", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/45", "OS-36", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/46", "OS-37", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/47", "OS-38", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/48", "OS-39", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/49", "OS-40", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/50", "OS-41", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/51", "OS-42", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 oshxona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 oshxona"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/53", "OS-43", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/54", "OS-44", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/55", "OS-45", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/56", "OS-46", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/57", "OS-47", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/58", "OS-48", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/59", "OS-49", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/60", "OS-50", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/61", "OS-51", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/62", "OS-52", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/63", "OS-53", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/64", "OS-54", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/65", "OS-55", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/66", "OS-56", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "< orqaga":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("oshxona")
        btn2 = types.KeyboardButton("ofis")
        btn3 = types.KeyboardButton("garderop")
        btn4 = types.KeyboardButton("yotoq xona")
        btn5 = types.KeyboardButton("bolalar xonasi")
        btn6 = types.KeyboardButton("zal")
        btn7 = types.KeyboardButton("bog'cha")
        btn8 = types.KeyboardButton("maktab")
        btn9 = types.KeyboardButton("ishxonalar")
        btn10 = types.KeyboardButton("boshq turdegi")
        btn11 = types.KeyboardButton("orqaga")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "tayyor mebellar saxifasi tanlandi.\n\ntayyor mebellar kataloglari:\n" \
                        "bu yerda siz ozingizga kerak bolgan tayyor mebillar toplamini tanlashingiz mumkin."

# 2 bo'lim -------------------------------------------------------------------------------------------------------------
# uzb ------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 ofis")
        btn2 = types.KeyboardButton("2 ofis")
        btn3 = types.KeyboardButton("3 ofis")
        btn4 = types.KeyboardButton("4 ofis")
        btn5 = types.KeyboardButton("5 ofis")
        btn6 = types.KeyboardButton("6 ofis")
        btn7 = types.KeyboardButton("< orqaga")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "ofis"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/68", "Of-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/69", "Of-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/70", "Of-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/71", "Of-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/72", "Of-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/73", "Of-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/74", "Of-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/75", "Of-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/76", "Of-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/77", "Of-10", parse_mode='html', reply_markup=markup)  # 10
        #bot.send_photo(message.chat.id, "https://t.me/svsvgf/18", "OS-11", parse_mode='html', reply_markup=markup)  # 11
        #bot.send_photo(message.chat.id, "https://t.me/svsvgf/19", "OS-12", parse_mode='html', reply_markup=markup)  # 12
        #bot.send_photo(message.chat.id, "https://t.me/svsvgf/20", "OS-13", parse_mode='html', reply_markup=markup)  # 13
        #bot.send_photo(message.chat.id, "https://t.me/svsvgf/21", "OS-14", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/79", "Of-11", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/80", "Of-12", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/81", "Of-13", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/82", "Of-14", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/83", "Of-15", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/84", "Of-16", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/85", "Of-17", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/86", "Of-18", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/87", "Of-19", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/88", "Of-20", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/90", "Of-31", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/91", "Of-32", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/92", "Of-33", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/93", "Of-34", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/94", "Of-35", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/95", "Of-36", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/96", "Of-37", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/97", "Of-38", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/98", "Of-39", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/99", "Of-40", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/101", "Of-41", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/102", "Of-42", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/103", "Of-43", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/104", "Of-44", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/105", "Of-45", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/106", "Of-46", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/107", "Of-47", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/108", "Of-48", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/109", "Of-49", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/110", "Of-50", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/112", "Of-51", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/113", "Of-52", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/114", "Of-53", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/115", "Of-54", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/116", "Of-55", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/117", "Of-56", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/118", "Of-57", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/119", "Of-58", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/120", "Of-59", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/121", "Of-60", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 ofis":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 ofis"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/123", "Of-61", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/124", "Of-62", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/125", "Of-63", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/126", "Of-64", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/127", "Of-65", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/128", "Of-66", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/129", "Of-67", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/130", "Of-68", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/131", "Of-69", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/132", "Of-70", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 garderop")
        btn2 = types.KeyboardButton("2 garderop")
        btn3 = types.KeyboardButton("3 garderop")
        btn4 = types.KeyboardButton("4 garderop")
        btn5 = types.KeyboardButton("5 garderop")
        btn6 = types.KeyboardButton("6 garderop")
        btn7 = types.KeyboardButton("7 garderop")
        btn8 = types.KeyboardButton("8 garderop")
        btn9 = types.KeyboardButton("9 garderop")
        btn10 = types.KeyboardButton("10 garderop")
        btn11 = types.KeyboardButton("< orqaga")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "garderop"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/134", "GA-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/135", "GA-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/136", "GA-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/137", "GA-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/138", "GA-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/139", "GA-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/140", "GA-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/141", "GA-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/142", "GA-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/143", "GA-10", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/145", "GA-11", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/146", "GA-12", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/147", "GA-13", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/148", "GA-14", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/149", "GA-15", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/150", "GA-16", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/151", "GA-17", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/152", "GA-18", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/153", "GA-19", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/154", "GA-20", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/156", "GA-31", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/157", "GA-32", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/158", "GA-33", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/159", "GA-34", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/160", "GA-35", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/161", "GA-36", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/162", "GA-37", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/163", "GA-38", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/164", "GA-39", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/165", "GA-40", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/167", "GA-41", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/168", "GA-42", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/169", "GA-43", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/170", "GA-44", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/171", "GA-45", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/172", "GA-46", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/173", "GA-47", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/174", "GA-48", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/175", "GA-49", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/176", "GA-50", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/199", "GA-51", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/179", "GA-52", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/180", "GA-53", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/181", "GA-54", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/182", "GA-55", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/183", "GA-56", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/184", "GA-57", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/185", "GA-58", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/186", "GA-59", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/187", "GA-60", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/189", "GA-61", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/190", "GA-62", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/191", "GA-63", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/192", "GA-64", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/193", "GA-65", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/194", "GA-66", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/195", "GA-67", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/196", "GA-68", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/197", "GA-69", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/198", "GA-70", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "7 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 7 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/201", "GA-71", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/202", "GA-72", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/203", "GA-73", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/204", "GA-74", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/205", "GA-75", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/206", "GA-76", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/207", "GA-77", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/208", "GA-78", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/209", "GA-79", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/210", "GA-80", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "8 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 8 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/212", "GA-81", parse_mode='html', reply_markup=markup)  #1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/213", "GA-82", parse_mode='html', reply_markup=markup)  #2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/214", "GA-83", parse_mode='html', reply_markup=markup)  #3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/215", "GA-84", parse_mode='html', reply_markup=markup)  #4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/216", "GA-85", parse_mode='html', reply_markup=markup)  #5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/217", "GA-86", parse_mode='html', reply_markup=markup)  #6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/218", "GA-87", parse_mode='html', reply_markup=markup)  #7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/219", "GA-88", parse_mode='html', reply_markup=markup)  #8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/120", "GA-89", parse_mode='html', reply_markup=markup)  #9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/221", "GA-90", parse_mode='html', reply_markup=markup)  #10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "9 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 9 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/223", "GA-91", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/224", "GA-92", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/225", "GA-93", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/226", "GA-94", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/227", "GA-95", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/228", "GA-96", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/229", "GA-97", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/230", "GA-98", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/231", "GA-99", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/232", "GA-100", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "10 garderop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 10 garderop"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/234", "GA-101", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/235", "GA-102", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/236", "GA-103", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/237", "GA-104", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/238", "GA-105", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/239", "GA-106", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/240", "GA-107", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/241", "GA-108", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/242", "GA-109", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/243", "GA-110", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "yotoq xona":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 spalniy")
        btn2 = types.KeyboardButton("2 spalniy")
        btn3 = types.KeyboardButton("3 spalniy")
        btn4 = types.KeyboardButton("4 spalniy")
        btn5 = types.KeyboardButton("5 spalniy")
        btn6 = types.KeyboardButton("6 spalniy")
        btn7 = types.KeyboardButton("7 spalniy")
        btn8 = types.KeyboardButton("8 spalniy")
        btn11 = types.KeyboardButton("< orqaga")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn11)
        final_message = "spalniy"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/246", "SP-01", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/247", "SP-02", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/248", "SP-03", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/249", "SP-04", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/250", "SP-05", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/251", "SP-06", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/252", "SP-07", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/253", "SP-08", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/254", "SP-09", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/255", "SP-10", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/258", "SP-11", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/259", "SP-12", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/260", "SP-13", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/261", "SP-14", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/262", "SP-15", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/263", "SP-16", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/264", "SP-17", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/265", "SP-18", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/266", "SP-19", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/267", "SP-20", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/268", "SP-21", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/269", "SP-22", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/270", "SP-23", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/271", "SP-24", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/272", "SP-25", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/273", "SP-26", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/274", "SP-27", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/275", "SP-28", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/276", "SP-29", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/277", "SP-30", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/279", "SP-31", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/280", "SP-32", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/281", "SP-33", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/282", "SP-34", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/283", "SP-35", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/284", "SP-36", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/285", "SP-37", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/286", "SP-38", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/287", "SP-39", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/288", "SP-40", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/290", "SP-41", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/291", "SP-42", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/292", "SP-43", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/293", "SP-44", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/294", "SP-45", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/295", "SP-46", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/296", "SP-47", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/297", "SP-48", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/298", "SP-49", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/299", "SP-50", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/301", "SP-51", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/302", "SP-52", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/303", "SP-53", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/304", "SP-54", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/305", "SP-55", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/306", "SP-56", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/307", "SP-57", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/308", "SP-58", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/309", "SP-59", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/310", "SP-60", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "7 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 7 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/312", "SP-61", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/313", "SP-62", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/314", "SP-63", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/315", "SP-64", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/316", "SP-65", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/317", "SP-66", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/318", "SP-67", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/319", "SP-68", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/320", "SP-69", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/321", "SP-70", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "8 spalniy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 8 spalniy"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/323", "SP-71", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/324", "SP-72", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/325", "SP-73", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/326", "SP-74", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/327", "SP-75", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/328", "SP-76", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/329", "SP-77", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/330", "SP-78", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/331", "SP-79", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/332", "SP-80", parse_mode='html', reply_markup=markup)











#----------------------------------------------rus versiya--------------------------------------------------------------

    elif get_message_bot == "кухня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("1 кухня")
        btn2 = types.KeyboardButton("2 кухня")
        btn3 = types.KeyboardButton("3 кухня")
        btn4 = types.KeyboardButton("4 кухня")
        btn5 = types.KeyboardButton("< назад")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "кухня"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 кухня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 кухня"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/8", "OS-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/9", "OS-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/10", "OS-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/11", "OS-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/12", "OS-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/13", "OS-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/14", "OS-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/15", "OS-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/16", "OS-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/17", "OS-10", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/18", "OS-11", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/19", "OS-12", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/20", "OS-13", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/21", "OS-14", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 кухня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 кухня"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/23", "OS-15", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/24", "OS-16", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/25", "OS-17", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/26", "OS-18", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/27", "OS-19", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/28", "OS-20", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/29", "OS-21", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/30", "OS-22", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/31", "OS-23", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/32", "OS-24", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/33", "OS-25", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/34", "OS-26", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/35", "OS-27", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/36", "OS-28", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 кухня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 кухня"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/38", "OS-29", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/39", "OS-30", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/40", "OS-31", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/41", "OS-32", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/42", "OS-33", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/43", "OS-34", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/44", "OS-35", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/45", "OS-36", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/46", "OS-37", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/47", "OS-38", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/48", "OS-39", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/49", "OS-40", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/50", "OS-41", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/51", "OS-42", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 кухня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 кухня"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/53", "OS-43", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/54", "OS-44", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/55", "OS-45", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/56", "OS-46", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/57", "OS-47", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/58", "OS-48", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/59", "OS-49", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/60", "OS-50", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/61", "OS-51", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/62", "OS-52", parse_mode='html', reply_markup=markup)  # 10
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/63", "OS-53", parse_mode='html', reply_markup=markup)  # 11
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/64", "OS-54", parse_mode='html', reply_markup=markup)  # 12
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/65", "OS-55", parse_mode='html', reply_markup=markup)  # 13
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/66", "OS-56", parse_mode='html', reply_markup=markup)  # 14

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "< назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("кухня")
        btn2 = types.KeyboardButton("офис")
        btn3 = types.KeyboardButton("гардероб")
        btn4 = types.KeyboardButton("спальная")
        btn5 = types.KeyboardButton("детская")
        btn6 = types.KeyboardButton("зал")
        btn7 = types.KeyboardButton("детский сад")
        btn8 = types.KeyboardButton("школа")
        btn9 = types.KeyboardButton("для бизнеса")
        btn10 = types.KeyboardButton("другой тип")
        btn11 = types.KeyboardButton("назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "выбрана страница готовой мебели.\n\nКаталоги готовой мебели:\n" \
                        "Здесь вы можете выбрать необходимый набор готовой мебели."

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 офис")
        btn2 = types.KeyboardButton("2 офис")
        btn3 = types.KeyboardButton("3 офис")
        btn4 = types.KeyboardButton("4 офис")
        btn5 = types.KeyboardButton("5 офис")
        btn6 = types.KeyboardButton("6 офис")
        btn7 = types.KeyboardButton("< назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "офис"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/68", "Of-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/69", "Of-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/70", "Of-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/71", "Of-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/72", "Of-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/73", "Of-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/74", "Of-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/75", "Of-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/76", "Of-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/77", "Of-10", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/79", "Of-11", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/80", "Of-12", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/81", "Of-13", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/82", "Of-14", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/83", "Of-15", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/84", "Of-16", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/85", "Of-17", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/86", "Of-18", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/87", "Of-19", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/88", "Of-20", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/90", "Of-31", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/91", "Of-32", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/92", "Of-33", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/93", "Of-34", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/94", "Of-35", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/95", "Of-36", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/96", "Of-37", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/97", "Of-38", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/98", "Of-39", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/99", "Of-40", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/101", "Of-41", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/102", "Of-42", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/103", "Of-43", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/104", "Of-44", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/105", "Of-45", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/106", "Of-46", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/107", "Of-47", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/108", "Of-48", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/109", "Of-49", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/110", "Of-50", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/112", "Of-51", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/113", "Of-52", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/114", "Of-53", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/115", "Of-54", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/116", "Of-55", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/117", "Of-56", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/118", "Of-57", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/119", "Of-58", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/120", "Of-59", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/121", "Of-60", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 офис":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 офис"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/123", "Of-61", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/124", "Of-62", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/125", "Of-63", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/126", "Of-64", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/127", "Of-65", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/128", "Of-66", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/129", "Of-67", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/130", "Of-68", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/131", "Of-69", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/132", "Of-70", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 гардероб")
        btn2 = types.KeyboardButton("2 гардероб")
        btn3 = types.KeyboardButton("3 гардероб")
        btn4 = types.KeyboardButton("4 гардероб")
        btn5 = types.KeyboardButton("5 гардероб")
        btn6 = types.KeyboardButton("6 гардероб")
        btn7 = types.KeyboardButton("7 гардероб")
        btn8 = types.KeyboardButton("8 гардероб")
        btn9 = types.KeyboardButton("9 гардероб")
        btn10 = types.KeyboardButton("10 гардероб")
        btn11 = types.KeyboardButton("< назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        final_message = "гардероб"

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "1 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/134", "GA-01", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/135", "GA-02", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/136", "GA-03", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/137", "GA-04", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/138", "GA-05", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/139", "GA-06", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/140", "GA-07", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/141", "GA-08", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/142", "GA-09", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/143", "GA-10", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/145", "GA-11", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/146", "GA-12", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/147", "GA-13", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/148", "GA-14", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/149", "GA-15", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/150", "GA-16", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/151", "GA-17", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/152", "GA-18", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/153", "GA-19", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/154", "GA-20", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/156", "GA-31", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/157", "GA-32", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/158", "GA-33", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/159", "GA-34", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/160", "GA-35", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/161", "GA-36", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/162", "GA-37", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/163", "GA-38", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/164", "GA-39", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/165", "GA-40", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/167", "GA-41", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/168", "GA-42", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/169", "GA-43", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/170", "GA-44", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/171", "GA-45", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/172", "GA-46", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/173", "GA-47", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/174", "GA-48", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/175", "GA-49", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/176", "GA-50", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/199", "GA-51", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/179", "GA-52", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/180", "GA-53", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/181", "GA-54", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/182", "GA-55", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/183", "GA-56", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/184", "GA-57", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/185", "GA-58", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/186", "GA-59", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/187", "GA-60", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/189", "GA-61", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/190", "GA-62", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/191", "GA-63", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/192", "GA-64", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/193", "GA-65", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/194", "GA-66", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/195", "GA-67", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/196", "GA-68", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/197", "GA-69", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/198", "GA-70", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "7 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 7 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/201", "GA-71", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/202", "GA-72", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/203", "GA-73", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/204", "GA-74", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/205", "GA-75", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/206", "GA-76", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/207", "GA-77", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/208", "GA-78", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/209", "GA-79", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/210", "GA-80", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "8 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 8 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/212", "GA-81", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/213", "GA-82", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/214", "GA-83", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/215", "GA-84", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/216", "GA-85", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/217", "GA-86", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/218", "GA-87", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/219", "GA-88", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/120", "GA-89", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/221", "GA-90", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "9 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 9 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/223", "GA-91", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/224", "GA-92", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/225", "GA-93", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/226", "GA-94", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/227", "GA-95", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/228", "GA-96", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/229", "GA-97", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/230", "GA-98", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/231", "GA-99", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/232", "GA-100", parse_mode='html',
                       reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "10 гардероб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 10 гардероб"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/234", "GA-101", parse_mode='html', reply_markup=markup)  # 1
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/235", "GA-102", parse_mode='html', reply_markup=markup)  # 2
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/236", "GA-103", parse_mode='html', reply_markup=markup)  # 3
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/237", "GA-104", parse_mode='html', reply_markup=markup)  # 4
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/238", "GA-105", parse_mode='html', reply_markup=markup)  # 5
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/239", "GA-106", parse_mode='html', reply_markup=markup)  # 6
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/240", "GA-107", parse_mode='html', reply_markup=markup)  # 7
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/241", "GA-108", parse_mode='html', reply_markup=markup)  # 8
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/242", "GA-109", parse_mode='html', reply_markup=markup)  # 9
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/243", "GA-110", parse_mode='html', reply_markup=markup)  # 10

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("1 спальная")
        btn2 = types.KeyboardButton("2 спальная")
        btn3 = types.KeyboardButton("3 спальная")
        btn4 = types.KeyboardButton("4 спальная")
        btn5 = types.KeyboardButton("5 спальная")
        btn6 = types.KeyboardButton("6 спальная")
        btn7 = types.KeyboardButton("7 спальная")
        btn8 = types.KeyboardButton("8 спальная")
        btn11 = types.KeyboardButton("< назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn11)
        final_message = "спальная"

# ----------------------------------------------------------------------------------------------------------------------


    elif get_message_bot == "1 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 1 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/246", "SP-01", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/247", "SP-02", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/248", "SP-03", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/249", "SP-04", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/250", "SP-05", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/251", "SP-06", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/252", "SP-07", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/253", "SP-08", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/254", "SP-09", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/255", "SP-10", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "2 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 2 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/258", "SP-11", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/259", "SP-12", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/260", "SP-13", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/261", "SP-14", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/262", "SP-15", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/263", "SP-16", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/264", "SP-17", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/265", "SP-18", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/266", "SP-19", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/267", "SP-20", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "3 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 3 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/268", "SP-21", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/269", "SP-22", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/270", "SP-23", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/271", "SP-24", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/272", "SP-25", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/273", "SP-26", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/274", "SP-27", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/275", "SP-28", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/276", "SP-29", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/277", "SP-30", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "4 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 4 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/279", "SP-31", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/280", "SP-32", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/281", "SP-33", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/282", "SP-34", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/283", "SP-35", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/284", "SP-36", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/285", "SP-37", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/286", "SP-38", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/287", "SP-39", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/288", "SP-40", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "5 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 5 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/290", "SP-41", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/291", "SP-42", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/292", "SP-43", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/293", "SP-44", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/294", "SP-45", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/295", "SP-46", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/296", "SP-47", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/297", "SP-48", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/298", "SP-49", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/299", "SP-50", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "6 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 6 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/301", "SP-51", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/302", "SP-52", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/303", "SP-53", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/304", "SP-54", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/305", "SP-55", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/306", "SP-56", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/307", "SP-57", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/308", "SP-58", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/309", "SP-59", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/310", "SP-60", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "7 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 7 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/312", "SP-61", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/313", "SP-62", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/314", "SP-63", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/315", "SP-64", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/316", "SP-65", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/317", "SP-66", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/318", "SP-67", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/319", "SP-68", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/320", "SP-69", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/321", "SP-70", parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

    elif get_message_bot == "8 спальная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        final_message = "👆 8 спальная"
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/323", "SP-71", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/324", "SP-72", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/325", "SP-73", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/326", "SP-74", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/327", "SP-75", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/328", "SP-76", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/329", "SP-77", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/330", "SP-78", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/331", "SP-79", parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, "https://t.me/svsvgf/332", "SP-80", parse_mode='html', reply_markup=markup)





# ----------------------------------------------------------------------------------------------------------------------
















# ----------------------------------------------------------------------------------------------------------------------

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("tayyor mebellar")
        btn2 = types.KeyboardButton("zakaz mebel")
        btn3 = types.KeyboardButton("list ranglari")
        btn4 = types.KeyboardButton("manzillarimiz")
        btn5 = types.KeyboardButton("start")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "menu"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

# ----------------------------------------------------------------------------------------------------------------------

bot.polling(none_stop=True)