import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, simpledialog
from PIL import Image, ImageDraw


class DrawingApp:
    """
    Класс DrawingApp представляет собой простое приложение для рисования с использованием
    библиотеки TKinter
    """
    def __init__(self, root):
        """
        Инициализация приложения рисования
        :param root: Корневой виджет TKinter, который служит контейнером для всего интерфейса прилоения
        """
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.brush_size = tk.IntVar()
        self.brush_size.set(1)

        self.pen_color = 'black'
        self.setup_ui()

        self.last_x, self.last_y = None, None
        self.text_mode = False

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.canvas.bind('<Button-3>', self.pick_color)

    def setup_ui(self):
        """
        Создаёт и настраивает элементы управления интерфейса
        """
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        eraser_button = tk.Button(control_frame, text="Ластик", command=self.toggle_eraser)
        eraser_button.pack(side=tk.LEFT)

        save_button = tk.Button(control_frame, text="Сохранить", command=self.save_image)
        save_button.pack(side=tk.LEFT)

        resize_button = tk.Button(control_frame, text="Изменить размер", command=self.resize_canvas)
        resize_button.pack(side=tk.LEFT)

        text_button = tk.Button(control_frame, text="Текст", command=self.toggle_text_mode)
        text_button.pack(side=tk.LEFT)

        dg_color_button = tk.Button(control_frame, text="Изменить фон", command=self.change_background_color)
        dg_color_button.pack(side=tk.LEFT)

        sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        size_menu = tk.OptionMenu(control_frame, self.brush_size, *sizes)
        size_menu.pack(side=tk.LEFT)

        self.root.bind('<Control-s>', self.save_image)
        self.root.bind('<Control-c>', self.choose_color)

        self.color_preview = tk.Label(control_frame, width=3, bg=self.pen_color)
        self.color_preview.pack(side=tk.LEFT, padx=5)

    def toggle_eraser(self):
        """
        Переключает режим на ластик (цвет фона) или обратно на предыдущий цвет рисования
        """
        if self.pen_color != 'white':
            self.previous_color = self.pen_color
            self.pen_color = 'white'
        else:
            self.pen_color = self.previous_color

    def paint(self, event):
        """
        Функция вызывается при движении мыши с нажатой левой кнопкой по холсту.
        Рисует линии на холсте TKinter и параллельно на объекте Image из Pillow
        :param event: Событие содержит координаты мыши, которые тспользуются для рисования
        """
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size.get(), fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            if self.pen_color != 'white':
                self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color,
                               width=self.brush_size.get())

        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        """
         Сбрасывает последние координаты кисти. Это необходимо для корректного начала новой линии после того, как пользователь отпустил кнопку мыши и снова начал рисовать.

        :param event: Событие, которое происходит при отпускании кнопки мыши
        """
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        """
         Очищает холст, удаляя все нарисованное, и пересоздает объекты Image и ImageDraw для нового изображения.
        """
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self, event=None):
        """
         Открывает стандартное диалоговое окно выбора цвета и устанавливает выбранный цвет как текущий для кисти.
         Обновляет цвет предварительного просмотра.
        """
        new_color = colorchooser.askcolor(color=self.pen_color)[1]
        if new_color:
            self.pen_color = new_color
            self.color_preview.config(bg=self.pen_color)

    def pick_color(self, event):
        """
        Функция вызывается при щелчке правой кнопкой мыши по холсту.
        Получает цвет пикселя по координатам и устанавливает его как текущий цвет кисти.
        :param event: Событие содержит координаты щелчка мыши
        """
        x, y = event.x, event.y
        pixel_color = self.image.getpixel((x, y))
        self.pen_color = '#%02x%02x%02x' % pixel_color

    def save_image(self, event=None):
        """
        Позволяет пользователю сохранить изображение, используя стандартное диалоговое окно для сохранения файла. Поддерживает только формат PNG.
        В случае успешного сохранения выводится сообщение об успешном сохранении
        """
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")

    def resize_canvas(self):
        """Открывает диалоговое окно для ввода новых размеров холста и изменяет размеры холста и изображения"""
        new_width = simpledialog.askinteger("Изменить размер", "Введите новую ширину:",
                                            initialvalue=self.canvas.winfo_width())
        new_height = simpledialog.askinteger("Изменить размер", "Введите новую высоту:",
                                            initialvalue=self.canvas.winfo_height())

        if new_width and new_height:
            self.canvas.config(width=new_width, height=new_height)
            self.image = Image.new("RGB", (new_width, new_height), "white")
            self.draw = ImageDraw.Draw(self.image)
            self.clear_canvas()

    def toggle_text_mode(self):
        """Переключает режим на добавление текста"""
        self.text_mode = not self.text_mode

    def add_text(self, event):
        """Добавляет текст на холст и изображение при клике, если включен режим добавления текста"""
        if self.text_mode:
            text = simpledialog.askinteger("Ввидите текст", "Ввидите текст для добавления:")
            if text:
                x, y = event.x, event.y
                self.canvas.create_text(x, y, text=text, fill=self.pen_color,font=("Arial", self.brush_size.get() * 2))
                self.draw.text((x, y), text, fill=self.pen_color)

    def change_background_color(self):
        """Изменяет цвет фона"""
        new_color = colorchooser.askcolor()[1]
        if new_color:
            self.canvas.config(bg=new_color)
            self.image.paste(new_color, [0, 0, self.image.size[0], self.image.size[1]])
            self.clear_canvas()