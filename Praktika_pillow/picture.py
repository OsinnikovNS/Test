# https://python-scripts.com/pillow?ysclid=lxmxgc481f449187824#open-image
# from PIL import Image
#
# im = Image.open('foto.jpg')
# print(im.format, im.size, im.mode)  # определение параметров картинки
# # im.show()  # показать картинку на экране
# out = im.resize((300, 400)) # изменение размера картинки
# out.show()
# ---------------------------------------------------
"""TODO"""
# -*- coding: utf-8 -*-

# Пример использования сторонней библиотеки на примере Pillow
# Задача: сделать поздравительную открытку другу

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class PostCardMaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = "foto.jpg" if template is None else template
        if font_path is None:
            self.font_path = os.path.join("fonts", "font_ru_DS Eraser2.ttf")
        else:
            self.font_path = font_path

    def make(self, resize=False, out_path=None):
        im = Image.open(self.template)
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=24)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"Привет, {self.name}!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        y = im.size[1] - 20 - font.size
        message = f"С Днем рождения тебя!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        im.show()
        out_path = out_path if out_path else 'foto1.jpg'
        im.save(out_path)
        print(f'Post card saved az {out_path}')


if __name__ == '__main__':
    maker = PostCardMaker(name='foto_1.jpg')
    maker.make(resize=True)
