# Программа вывода банковских операций
В данной програме присутствует три папки: src, main, tests
_____
### Папка src
В данной папке содержится файл **utils.py** и **operations.json**. В файле **utils.py** реализованы 3 функции:
#### load_json_operations - открывает json файл с данными о операциях и выводит только успешные операции.
#### get_data_for_sort - сортирует наш json файл по дате.
#### get_date_format - данная функция выводит последние успешные 5 операций, и маскирует счета, так же сортирует вывод.
Так же operations.json это сам файл с данными о банковских операциях
_____
### Папка tests 
В данной папке содержится файл **test_utils.py**. В данном файле написаные функции для тестирования нашего **utils.py**, реализация тестов происходит через **pytest**
_____
### Папка main
В данной папке содержится файл **main.py**. В данном файле происходит вывод функции **get_date_format**, отсортированных 5 банковских операций.
_____
К данному проекту идет пакет зависимостей который содержится в **requirements.txt**.
Проект реализован в виртуальном окружении **Venv**
