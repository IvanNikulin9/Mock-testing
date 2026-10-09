import unittest ### - встроенный модуль для написания тестов
from unittest.mock import patch
from unittest.mock import MagicMock

from main import len_joke, get_joke

class TestJoke(unittest.TestCase): ### - класс TestJoke, который наследуется от TestCase

    @patch('main.get_joke') ### - подменяет функцию get_joke внутри модуля main на мок на время выполнения теста
    def test_len_joke(self, mock_get_joke): ### - объявляет тестовый метод. Имя начинается с test_ — так unittest понимает, что это тест. mock_get_joke - это сам мок
        mock_get_joke.return_value = 'one' ### - настраивает мок(в тестировании вернет 'one')
        self.assertEqual(len_joke(), 3) ### - assertEqual - проверяет совпали значения или нет(первым аргументом вызывает функцию len_joke())

    @patch('main.requests') ### - теперь это мок, а не реальная библиотека
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock() ### - отдельный мок для имитации объекта Response
        mock_response.status_code = 200 ### - устанавливает атрибут status_code у мока равным 200, чтобы условие в main было истинным
        mock_response.json.return_value = { 'value' : 'Hello world' } ### - имитация ответа API
        mock_requests.get.return_value = mock_response ### - когда код вызовет mock_requests.get(url), вернётся mock_response — тот самый мок-ответ, который мы настроили выше
        self.assertEqual(get_joke(), 'Hello world') ### -  вызывает get_joke() (уже с моками) и проверяет, что результат равен 'Hello world'


if __name__ == '__main__':
    unittest.main()