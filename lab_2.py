class Fract:
    # инициализация данных в классе
    # используем магические методы

    def __init__(self, num, denom):   #Метод инициализации класса
        self.__num = num              #приватное поле класса
        self.__denom = denom

    #Метод для преобразования объекта класса в строку
    def __str__(self):  # вызывается print (чтобы печаетались данные, а не обьекты)
        return str(self.__num) + '/' + str(self.__denom)

    def decimal_fract(self):  # перевод в десячиную дробь
        return round(self.__num / self.__denom, 6)

    def __add__(self, other):  # сложение
        new_num = self.__num * other.__denom + other.__num * self.__denom
        new_denom = self.__denom * other.__denom
        degree = reduction(new_num, new_denom)  #НОД для сокращения
        return Fract(new_num // degree, new_denom // degree)

    def __sub__(self, other):  # вычитание
        new_num = self.__num * other.__denom - other.__num * self.__denom
        new_denom = self.__denom * other.__denom
        degree = reduction(new_num, new_denom)
        return Fract(new_num // degree, new_denom // degree)

    def __mul__(self, other):  # умножение
        new_num = self.__num * other.__num
        new_denom = self.__denom * other.__denom
        degree = reduction(new_num, new_denom)
        return Fract(new_num // degree, new_denom // degree)

    def __floordiv__(self, other):  # деление
        new_num = self.__num * other.__denom
        new_denom = self.__denom * other.__num
        degree = reduction(new_num, new_denom)
        return Fract(new_num // degree, new_denom // degree)

    #   Сравнение дробей
    def __ne__(self, other):  # проверка на неравенство
        return (self.__num * other.__denom) != (other.__num * self.__denom)

    def __eq__(self, other):  # проверка на равенство
        return (self.__num * other.__denom) == (other.__num * self.__denom)

    def __gt__(self, other):  # проверка на 1 дробь > 2 дробь
        return str(self.__num * other.__denom) > str(other.__num * self.__denom)

    def __lt__(self, other):  # проверка на 1 дробь < 2 дробь
        return self.__num * other.__denom < other.__num * self.__denom


def reduction(m, n):  # НОД для сокращения дробей
    while m % n != 0:
        m, n = n, m % n
    return n


def CorrectlyNumber():
    while True:
        try:
            num = int(input())
            return num
        except Exception:
            print("Неправильный ввод")
            print("Введите дробь 2 числами")
            print("Первое число это числитель")
            print("Второе знаменатель")


if __name__ == "__main__":
    print("Введите дробь 2 числами")
    f1 = Fract(CorrectlyNumber(), CorrectlyNumber())
    print("Введите дробь 2 числами")
    f2 = Fract(CorrectlyNumber(), CorrectlyNumber())
    print(f" f1 = {f1}   f2 = {f2} ")
    print(f" Сумма = {f1 + f2}")
    print(f" Десятичная дробь от суммы = {(f1 + f2).decimal_fract()}")
    print(f" Разность = {f1 - f2}")
    print(f" Произведение = {f1 * f2}")
    print(f" Деление = {f1 // f2}")
    print(f" Функция f1 не равна f2 = {f1 != f2}")
    print(f" Функция f1 равна f2 = {f1 == f2}")
    print(f" Функция f1 больше f2 = {f1 > f2}")
    print(f" Функция f1 меньше f2 = {f1 < f2}")