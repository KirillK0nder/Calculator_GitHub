def fun():
    global y, x
    while True:

        data = input("Введите пример: ").split(" ")  # пользователь вводит данные/

        if len(data) != 3:
            return "Каждый символ разделяется пробелом!"

        try:

            x = int(data[0])
            y = int(data[-1])
        except Exception:  # проверка ошибки(Если в строке есть буква)
            return "Калькулятор обрабатывает только числа"

        operation = data[1]

        if operation == "+":
            print(x + y)

        elif operation == "-":
            print(x - y)

        elif operation == "*" or operation == "x" or operation == "X":
            print(x * y)

        elif operation == "/" or operation == ":":
            print(x / y)

        else:
            print("Нет такого операнда!")


print(fun())
