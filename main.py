def fun():
    global y, x
    while True:

        data = input("Введите пример: ").split(" ")  # пользователь вводит данные
        try:

            x = int(data[0])
            y = int(data[-1])
        except Exception:  # проверка ошибки(Если в строке есть буква)
            print("Калькулятор обрабатывает только числа")

        operation = data[1]

        if operation == "+":
            print(x + y)


        elif operation == "-":
            print(x - y)

        elif operation == "*":
            print(x * y)

        elif operation == "/":
            print(x / y)

        else:
            print("Нет такого операнда!")


fun()

