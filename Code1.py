num = int(input("Введите значение: "))


# декоратор cash, который применяется к функции func
def cash(func):
    # считает количество вызовов нашей функции
    counter = 0
    cash = func()

    def deco():
        # проверяется значение counter, если оно меньше или =3, то значение
        # cash возращается
        nonlocal counter
        counter += 1
        if counter <= 3:
            return cash

        else:
            counter = 1
            return func()

    return deco


@cash
def func():
    # умножает наше число на 1000
    x = num * 1000
    print("Кеш")
    return x


# я написала свой коммантарий. Катюня
print(func())
print(func())

print(func())
