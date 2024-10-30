def test_function():  # облемлющая  функция для функции inner_function()
    def inner_function():
        print(f"Я в области видимости функции test_function")

    inner_function()


test_function()
# Вызов функции  вне функции test_function приводит к появлению ошибки из-за различия пространства имён