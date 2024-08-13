import os

import telebot
from PIL import Image
import io
from config import TELEGRAM_BOT_TOKEN

from dotenv import load_dotenv
from telebot import types

load_dotenv()

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

user_states = {}  # тут будем хранить информацию о действиях пользователя

# набор символов из которых составляем изображение
ASCII_CHARS = '@%#*+=-:. '


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))


def grayify(image):
    return image.convert("L")


def image_to_ascii(image_stream, new_width=40, custom_chars=None):
    # Переводим в оттенки серого
    image = Image.open(image_stream).convert('L')

    # меняем размер сохраняя отношение сторон
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(
        aspect_ratio * new_width * 0.55)  # 0,55 так как буквы выше чем шире
    img_resized = image.resize((new_width, new_height))

    if custom_chars:
        ASCII_CHARS = custom_chars

    img_str = pixels_to_ascii(img_resized)
    img_width = img_resized.width

    max_characters = 4000 - (new_width + 1)
    max_rows = max_characters // (new_width + 1)

    ascii_art = ""
    for i in range(0, min(max_rows * img_width, len(img_str)), img_width):
        ascii_art += img_str[i:i + img_width] + "\n"

    return ascii_art


def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        characters += ascii_chars[pixel * len(ASCII_CHARS) // 256]
    return characters


# Огрубляем изображение
def pixelate_image(image, pixel_size):
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправьте мне изображение, и я предоставлю варианты обработки!")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Я получил ваше фото! Пожалуйста, выберите, что вы хотите с ним сделать",
                 reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


def get_options_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Пикселизация", callback_data="pixelate")
    ascii_btn = types.InlineKeyboardButton("ASCII Art", callback_data="ascii")
    keyboard.add(pixelate_btn, ascii_btn)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'pixelate':
        bot.answer_callback_query(call.id, 'Пикселизирую ваше изображение...')
        pixelate_and_send(call.message)
    elif call.data == 'ascii':
        bot.answer_callback_query(call.id, 'Преобразую ваше изображение в ASCII-арт...')
        ask_ascii_chars(call.message)


def ask_ascii_chars(message):
    msg = bot.send_message(message.chat.id, 'Введите свой набор символов для ASCCII-арта:')
    bot.register_next_step_handler(msg, process_custom_chars)


def process_custom_chars(message):
    custom_chars = message.text.strip()
    if not custom_chars:
        bot.send_message(message.chat.id, 'Вы не ввели набор символов. Используется символы по умолчанию')
        custom_chars = None
    ascii_and_send(message, custom_chars)


def pixelate_and_send(message):
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    pixelated = pixelate_image(image, 20)

    output_stream = io.BytesIO()
    pixelated.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def ascii_and_send(message, custom_chars=None):
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    ascii_art = image_to_ascii(image_stream, custom_chars=custom_chars)
    bot.send_message(message.chat.id, f"```\n{ascii_art}\n```", parse_mode="MarkdownV2")


bot.polling(none_stop=True)