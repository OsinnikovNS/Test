# -*- coding: utf-8 -*-
import os.path
# Пример использования сторонней библиотеки на примере Pillow
# Задача: сделать поздравительную открытку другу на праздник

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class PostCardMarker:
    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = 'post_card.jpg' if template is None else template
        if font_path is None:
            self.font_path = os.path.join('fonts', 'font_ru_DS Eraser2.ttf')
        else:
            self.font_path = font_path

    def make(self, resize=False, out_path=None):
        im = Image.open('post_card.jpg')
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw(im)
        font = ImageFont.truetype(self.font_path, size=26)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f'Привет, {self.name}!'
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        out_path = out_path if out_path else 'probe.jpg'
        im.save(out_path)
        print(f'Post card saved as {out_path}')


if __name__ == '__main__':
    maker = PostCardMarker(name='Мария')
    maker.make(resize=True)
