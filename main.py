import math
import tkinter as tk


class CanvasApp(tk.Tk):
    """
    Класс CanvasApp представляет приложение для рисования равносторонних
    треугольников с использованием библиотеки tkinter.

    Атрибуты:
    - canvas: холст для рисования треугольников
    - side_length: длина стороны треугольника
    - x: координата x вершины треугольника
    - y: координата y вершины треугольника
    - triangles: список идентификаторов созданных треугольников на холсте

    Методы:
    - draw: рисует треугольник на холсте и обновляет координаты для следующего
    - delete: удаляет последний нарисованный треугольник и восстанавливает предыдущие координаты
    - close: закрывает приложение
    """

    def __init__(self):
        """
        Инициализирует приложение, создает холст, задает начальные параметры
        треугольника и привязывает события.
        """
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.side_length = 700
        self.x = 50
        self.y = 700
        self.triangles = []
        self.canvas.pack(fill=tk.BOTH, expand=1)

        self.bind('<Return>', self.draw)
        self.bind('<Escape>', self.close)
        self.bind('<KeyPress-d>', self.delete)

    def draw(self, event):
        """
        Рисует треугольник на холсте и обновляет координаты для следующего треугольника.

        :param event: событие, вызывается при нажатии клавиши Enter
        """

        if self.side_length > 0:
            x1 = self.x
            y1 = self.y

            x2 = x1 + self.side_length
            y2 = y1

            x3 = x1 + (self.side_length / 2)
            y3 = y1 - (self.side_length * math.sqrt(3) / 2)

            triangle = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="")
            self.triangles.append(triangle)

            self.x += 20
            self.y -= 10

            self.side_length -= 40

    def delete(self, event):
        """
        Удаляет последний нарисованный треугольник и восстанавливает предыдущие координаты.

        :param event: событие, вызывается при нажатии клавиши "D"
        """
        if len(self.triangles) != 0:
            last_triangle = self.triangles.pop()
            self.canvas.delete(last_triangle)

            self.x -= 20
            self.y += 10

            self.side_length += 40

    def close(self, event):
        """
        Закрывает приложение при нажатии клавиши Escape.

        :param event: событие, вызывается при нажатии клавиши Escape
        """
        self.destroy()


if __name__ == "__main__":
    app = CanvasApp()
    app.mainloop()
