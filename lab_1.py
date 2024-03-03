import numpy as np
from abc import ABC, abstractmethod

# код определяет абстрактный базовый класс Интеграл и два его подкласса - Sympsons и Trapezoidal
# Оба они реализуют метод calc() численного интегрирования
# для указанной функции func на промежутке [lower_bound, upper_bound] с использованием метода Симпсона и метода Трапеции.
# __init__ является конструктором класса. Он инициализирует кол-во точек, шаг и точность
# Ключевое слово self используется для ссылки на экземпляр класса внутри методов класса
# и для обращения к этим атрибутам в методах.

class Integral(ABC):
    def __init__(self, num_points, step, precision):  # конструктор используется для создания объекта класса
        self.num_points = num_points                  # определение и установка атрибутов внутри класса
        self.step = step
        self.precision = precision

    @abstractmethod                                   # Декоратор, который определяет метод calc() как абстрактный
    def calc(self, func, lower_bound, upper_bound):   # т.е. метод должен быть реализован в подклассах Integral
        pass

# Определение классов, которые являются подклассами Integral
class Trapezoidal(Integral):
    def calc(self, func, lower_bound, upper_bound):   # Метод calc(), который реализует вычисление приближенного значения определенного интеграла
        x = np.linspace(lower_bound, upper_bound, self.num_points)  # функция создает последовательность данных, равномерно расположенных на числовой прямой в заданном интервале
        y = func(x)
        integral = self.step * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
        return integral

class Simpson(Integral):
    def calc(self, func, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound, self.num_points)
        y = func(x)
        integral = self.step / 3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
        return integral

def f(x):
    return x**2


#Выведет приближенное значение определенного интеграла функции x^2 на промежутке [0, 1]
#методми Симпсона Трапеции
trapezoidal_i = Trapezoidal(num_points=1000, step=0.001, precision=0.0001)
print(trapezoidal_i.calc(f, 0, 1))

simpson_i = Simpson(num_points=1000, step=0.001, precision=0.0001)
print(simpson_i.calc(f, 0, 1))