""" Этот бот для Telegram позволяет пользователям обрабатывать свои изображения различными эффектами и
преобразованиями, включая пикселизацию, преобразование в ASCII-арт, инверсию цветов, зеркальное отражение,
преобразование в тепловую карту, создание стикеров и многое другое. Кроме того, он предоставляет возможности
для развлечений, такие как отправка случайных шуток, комплиментов и подбрасывание монетки. """
#!/usr/bin/python
# -*- coding: utf8 -*-
import telebot
from PIL import Image, ImageOps
import io
from telebot import types
from token_ import TOKEN_
from random import choice

bot = telebot.TeleBot(TOKEN_)

# тут будем хранить информацию о действиях пользователя
user_states = {}

# набор стандартных символов для эффекта ASCII по умолчанию
ascii_symbols_stock = '@$%#*+=-:. '


def resize_image(image: Image.Image, new_width: int = 100) -> Image.Image:
    """
    Изменение размера изображения
    :param image: (Image.Image) Исходное изображение
    :param new_width: (int) Новая ширина изображения
    :return: Image.Image Измененное изображение
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))


def grayify(image: Image.Image) -> Image.Image:
    """Преобразование в оттенки серого"""
    return image.convert("L")


def convert_to_heatmap(image: Image.Image) -> Image.Image:
    """
    Преобразование изображения в тепловую карту
    :param image: (Image.Image) Исходное изображение
    :return: (Image.Image) Изображение в виде тепловой карты
    """
    grayscale_image = grayify(image)
    heatmap_image = ImageOps.colorize(grayscale_image, black="blue", white="red")
    return heatmap_image


def image_to_ascii(image_stream: io.BytesIO, ascii_chars: str, new_width: int = 40) -> str:
    """Конвертация изображения в ASCII-арт.
    :param image_stream: (io.BytesIO) поток байтов изображения
    :param new_width: (int) Новая ширина изображения для ASCII
    :param ascii_chars: (str) Набор символов для ASCII-арта
    :return: (str) Строка символов  c артом ASCII
    """
    # Переводим в оттенки серого
    image = Image.open(image_stream).convert('L')

    # меняем размер сохраняя отношение сторон
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)  # 0,55 так как буквы выше чем шире
    img_resized = image.resize((new_width, new_height))

    img_str = pixels_to_ascii(img_resized, ascii_chars)
    img_width = img_resized.width

    max_characters = 4000 - (new_width + 1)
    max_rows = max_characters // (new_width + 1)

    ascii_art = ""
    for i in range(0, min(max_rows * img_width, len(img_str)), img_width):
        ascii_art += img_str[i:i + img_width] + "\n"

    return ascii_art


def pixels_to_ascii(image: Image.Image, ascii_chars: str) -> str:
    """Преобразование пикселей в ASCII-symbols
    :param image: (Image.Image) Изображение в оттенках
    :param ascii_chars: (str) Набор символов для ASCII-арта
    :return (str) Строка символов ASCII
    """
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        characters += ascii_chars[pixel * len(ascii_chars) // 256]
    return characters


def pixelate_image(image: Image.Image, pixel_size: int) -> Image.Image:
    """Пикселизация изображения
    :param image: (Image.Image) Исходное изображение
    :param pixel_size: (int) Размер пикселя для пикселизации
    :return: Image.Image Пикселизированное изображение
    """
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image


def invert_colors(image: Image.Image) -> Image.Image:
    """
    Инверсия цветов изображения
    :param image: (Image.Image) Исходное изображение
    :return: (Image.Image)  Изображение с инверсией цветов
    """
    return ImageOps.invert(image)


def mirror_image(image: Image.Image, mode: str) -> Image.Image:
    """
    Отражение изображения
    :param image: (Image.Image) Исходное изображение
    :param mode: (str) Режим отражения ("horizontal" или "vertical")
    :return: (image.Image) Отраженнное изображения
    """
    if mode == "horizontal":
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == "vertical":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Invalid mode for mirroring image. Use 'vertical' or 'horizontal'")


def resize_for_sticker(image: Image.Image, max_dimension: int = 512) -> Image.Image:
    """
    Изменение размера изображения для использования в качестве стикера в Telegram.
    :param image: (Image.Image) Исходное изображение
    :param max_dimension: (int) Максимальный размер измерения (по умолчанию 512 пикселей)
    :return: (Image.Image) Изображение с измененными размерами
    """
    width, height = image.size
    if width > height:
        new_width = max_dimension
        new_height = int(height * (max_dimension / width))
    else:
        new_height = max_dimension
        new_width = int(width * (max_dimension / height))
    return image.resize((new_width, new_height))


JOKES = [
    "Самое лучшее средство для ухода - ноги.",
    "Фотография жены в моём бумажнике напоминает мне о том, что на этом месте могли бы быть деньги...",
    "Женатые мужчины живут мучительно дольше...",
    "Старость - это когда не можешь помыть пятки в раковине.",
    "Человек проводит во сне 30% жизни. Остальные 70% мечтает выспаться.",
    "Зрелость - возраст, когда мы все еще молоды, но с гораздо большим трудом.",
    "Интеллектуал - этот тот, кто может найти занятие более интересное, чем секс.",
    "Немногие мужчины умеют правильно подать руку даме, вылезающей из погреба с мешком картошки!",
    "Нельзя быть одновременно веселым, трезвым и умным.",
    "Установлено, что холостяки приносят в семью больше денег, чем женатые.",
    "Практика - это когда все работает, но непонятно как. Теория - это когда все понятно, но ничего не работает. "
    "Но все же иногда теория с практикой совмещаются: ничего не работает и ничего не понятно.",
    "Если бы спорт был действительно полезен, то на каждом турнике висело бы по пять евреев...",
    "Сколько водки ни пей, а организм все равно на 80% состоит из воды!",
    "Возможности медицины безграничны. Ограничены возможности больных.",
    "Однажды известный русский исследователь Пржевальский встретил лошадь... Через год она взяла его фамилию.",
    "Нервный не тот, кто стучит пальцами по столу, а тот, кого это раздражает.",
    "Иногда будильник помогает проснуться, но чаще мешает спать.",
    "Два одесских слова, о которые разбиваются все доказательства: «И шо?»",
    ]
COMPLIMENTS = [
    "Вы прекрасны сегодня!",
    "У вас замечательный вкус!",
    "Вы делаете мир лучше!",
    "Ваша улыбка заразительна!",
    "Ваши достижения впечатляют!",
    "Вас окружает так много позитивной энергии!",
    "Вы вдохновляете других!",
    "Сегодня - ваш день!",
    "Вы достойны любви и уважения!",
    "Ваши идеи уникальны и ценны!",
]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    """Обработка команд /start и /help.
    :param message: (telebot.types.Message) Сообщение от пользоваиеля
    """
    bot.reply_to(message, "Пришлите мне изображение, и я предложу вам варианты!")


@bot.message_handler(content_types=['photo'])
def handle_photo(message: telebot.types.Message):
    """ Обработка фотографий
    :param message: (telebot.types.Message) Сообщение с фотографией от пользоваиеля
    """
    bot.reply_to(message,
                 "Я получил Ваше изображение! Выберите, что бы Вы хотите с ней сделать?",
                 reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


def get_options_keyboard():
    """Клавиатура с варинтами обработок
    :return (types.InlineKeyboardMarkup) клава с кнопками для выбора оброботки
    """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Пикселизировать", callback_data="pixelate")  # кнопка для pixelate
    ascii_btn = types.InlineKeyboardButton("ASCII-творчество", callback_data="ascii")  # кнопка для ascii
    invert_btn = types.InlineKeyboardButton("Инвертировать цвета", callback_data="invert")  # кнопка для invert
    mirror_horizont_btn = types.InlineKeyboardButton("Зеркально по горизонтали",
                                                     callback_data="mirror_horizontal")  # кнопка для mirror horizontal
    mirror_vert_btn = types.InlineKeyboardButton("Зеркально по вертикали",
                                                 callback_data="mirror_vertical")  # кнопка для mirror vertical
    heatmap_btn = types.InlineKeyboardButton("Теплые цвета", callback_data="heatmap")  # кнопка для тепловой карты
    sticker_btn = types.InlineKeyboardButton("Преобразовать в стикер", callback_data="sticker")  # кнопка для стикера
    random_joke_btn = types.InlineKeyboardButton("Случайная шутка", callback_data="random_joke")  # кнопка для шутки
    compliment_btn = types.InlineKeyboardButton("Случайный комплимент",
                                                callback_data="compliment")  # кнопка для комплимента
    coin_flip_btn = types.InlineKeyboardButton("Орел или Решка", callback_data="coin_flip")

    keyboard.add(pixelate_btn, ascii_btn, invert_btn, mirror_horizont_btn,
                 mirror_vert_btn, heatmap_btn, sticker_btn, random_joke_btn, compliment_btn, coin_flip_btn
                 )
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: telebot.types.CallbackQuery):
    """Обработка выбора пользователя
    :return (telebot.types.CallbackQuery) Объект с инфо о нажатой кнопке
    """
    if call.data == "pixelate":
        bot.answer_callback_query(call.id, "Пикселизация изображения...")
        pixelate_and_send(call.message)
    elif call.data == "ascii":
        bot.answer_callback_query(call.id, "Converting your image to ASCII art...")
        bot.send_message(call.message.chat.id, "Введите набор символов для ASCII-арта, "
                                               "начиная с самых темных к самым светлым,"
                                               "например @%#*+=-:,"
                                               "\nИли напишите 'default' для использования стандартного набора символов")
        bot.register_next_step_handler(call.message, ask_for_ascii_chairs)

    elif call.data == "invert":
        bot.answer_callback_query(call.id, "Inverting colors of your image...")
        invert_and_send(call.message)
    elif call.data == "mirror_horizontal":
        bot.answer_callback_query(call.id, "Mirroring your image horizontally...")
        mirror_and_send(call.message, "horizontal")
    elif call.data == "mirror_vertical":
        bot.answer_callback_query(call.id, "Mirroring your image vertically...")
        mirror_and_send(call.message, "vertical")
    elif call.data == "heatmap":
        bot.answer_callback_query(call.id, "Converting your image to a heatmap...")
        heatmap_and_send(call.message)
    elif call.data == "sticker":
        bot.answer_callback_query(call.id, "Преобразование вашего изображения в стикер...")
        sticker_and_send(call.message)
    elif call.data == "random_joke":
        bot.answer_callback_query(call.id, "Выбираю случайную шутку...")
        send_random_joke(call.message)
    elif call.data == "compliment":
        bot.answer_callback_query(call.id, "Sending you a random compliment...")
        send_random_compliment(call.message)
    elif call.data == "coin_flip":
        bot.answer_callback_query(call.id, "Flipping a coin...")
        flip_coin_and_send(call.message)


def ask_for_ascii_chairs(message: telebot.types.Message):
    """Запрос набора символов для арта ASCII
    :param message: (telebot.types.Message) Сообщение от пользователя с набором символов
    """
    ascii_chars = message.text
    if ascii_chars.lower() == 'default':
        ascii_chars = ascii_symbols_stock
    user_states[message.chat.id]['ascii_chairs'] = ascii_chars
    ascii_and_send(message)


def pixelate_and_send(message: telebot.types.Message):
    """
    Пикслелизация и отправка изображения
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    pixelated = pixelate_image(image, 5)

    output_stream = io.BytesIO()
    pixelated.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def ascii_and_send(message: telebot.types.Message):
    """Конвертация изображения в ASCII-арт и отправка результата.
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    ascii_chars = user_states[message.chat.id].get('ascii_chairs', '@%#*+=-:. ')
    ascii_art = image_to_ascii(image_stream, ascii_chars)
    bot.send_message(message.chat.id, f"```\n{ascii_art}\n```", parse_mode="MarkdownV2")


def invert_and_send(message: telebot.types.Message):
    """
    Инверсия цветов  и отправка изображения
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    inverted = invert_colors(image)

    output_stream = io.BytesIO()
    inverted.save(output_stream, format='JPEG')
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def mirror_and_send(message: telebot.types.Message, mode: str):
    """Отражение и отправка изображения
    :param message: (telebot.types.Message) Сообщение от пользователя
    :param mode: (str) Режим отражения ("horizontal", "vertical" )
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    mirrored = mirror_image(image, mode)

    output_stream = io.BytesIO()
    mirrored.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def heatmap_and_send(message: telebot.types.Message):
    """
    Преобразование и отправка изображения в тепловую карту
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    heatmap_image = convert_to_heatmap(image)

    output_stream = io.BytesIO()
    heatmap_image.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def sticker_and_send(message: telebot.types.Message):
    """
    Преобразование изображения в стикер и отправка результата
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    sticker = resize_for_sticker(image)

    output_stream = io.BytesIO()
    sticker.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def send_random_joke(message: telebot.types.Message):
    """Отправка случайной шутки
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    joke = choice(JOKES)
    bot.send_message(message.chat.id, joke)


def send_random_compliment(message: telebot.types.Message):
    """Отправка случайного комплимента
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    compliment = choice(COMPLIMENTS)
    bot.send_message(message.chat.id, compliment)


def flip_coin_and_send(message: telebot.types.Message):
    """Подбрасывание монетки и отправка результата
    :param message: (telebot.types.Message) Сообщение от пользователя
    """
    result = choice(["Орел", "Решка"])
    bot.send_message(message.chat.id, f"Выпало: {result}")


bot.polling(none_stop=True)
