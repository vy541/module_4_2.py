def test_function():
    def inner_function():
        print(f"Я в области видимости функции test_function")

    inner_function()


test_function()


#Вызов функции inner_function() вне функции test_function приводит к появлению ошибки из-за различия пространства имён