import unittest
from unittest.mock import MagicMock

from main import TriangleDrawerApp


class TestTriangleDrawerApp(unittest.TestCase):
    """
    Класс TestTriangleDrawerApp содержит юнит-тесты для класса TriangleDrawerApp.

    Атрибуты:
    - app: экземпляр TriangleDrawerApp для тестирования

    Методы:
    - setUp: подготовка к запуску тестов, создает экземпляр TriangleDrawerApp
    - test_draw: тестирование метода draw
    - test_delete: тестирование метода delete
    """

    def setUp(self):
        """
        Подготавливает приложение для запуска тестов.
        """
        self.app = TriangleDrawerApp()

    def test_draw(self):
        """
        Тестирование метода draw.

        Создает событие, имитирующее нажатие Enter, записывает начальные значения,
        вызывает метод draw и проверяет, что координаты и длина стороны изменены.
        """
        # Создаем событие, имитирующее нажатие Enter
        event = MagicMock()
        event.keysym = 'Return'

        # Записываем начальные значения
        initial_x = self.app.x
        initial_y = self.app.y
        initial_side_length = self.app.side_length

        # Вызываем метод draw
        self.app.draw(event)

        # Проверяем, что координаты и длина стороны изменены
        self.assertNotEqual(initial_x, self.app.x)
        self.assertNotEqual(initial_y, self.app.y)
        self.assertNotEqual(initial_side_length, self.app.side_length)

    def test_delete(self):
        """
        Тестирование метода delete.

        Создает событие, имитирующее нажатие "D", проверяет, что удаление не происходит,
        когда список пуст, добавляет треугольник и убеждается, что он удаляется.
        """
        # Создаем событие, имитирующее нажатие "D"
        event = MagicMock()
        event.keysym = 'd'

        # Проверяем, что удаление не происходит, когда список пуст
        initial_x = self.app.x
        initial_y = self.app.y
        initial_side_length = self.app.side_length
        initial_triangle_count = len(self.app.triangles)

        self.app.delete(event)

        self.assertEqual(initial_x, self.app.x)
        self.assertEqual(initial_y, self.app.y)
        self.assertEqual(initial_side_length, self.app.side_length)
        self.assertEqual(initial_triangle_count, len(self.app.triangles))

        # Добавим треугольник и убедимся, что он удаляется
        self.app.draw(event)

        initial_triangle_count = len(self.app.triangles)

        self.app.delete(event)

        self.assertEqual(initial_triangle_count - 1, len(self.app.triangles))


if __name__ == '__test_main__':
    unittest.main()
