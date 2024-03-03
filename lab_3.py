#Создаем класс, который будет представлять трехмерный массив, но хранить данные в одномерном массиве
class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.__dim0 = dim0
        self.__dim1 = dim1
        self.__dim2 = dim2
        self.__data = [None] * (dim0 * dim1 * dim2)   #создаем одномерный список, который может хранить все элементы трехмерного массива

    # метод позволяет получить значение элемента массива по его индексам в трехмерном пространстве
    def __getitem__(self, indices):
        i, j, k = indices
        return self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]

    # метод позволяет установить значение элемента массива по его индексам в трехмерном пространстве
    def __setitem__(self, indices, value):
        i, j, k = indices
        self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = value

    # Индексатор для доступа к элементам массива по трехмерным координатам(i, j, k)
    def __get_slice(self, coord1, coord2, coord3):
        slice = []
        for i in range(self.__dim0):
            for j in range(self.__dim1):
                for k in range(self.__dim2):
                    if coord1 is not None and i != coord1:
                        continue
                    if coord2 is not None and j != coord2:
                        continue
                    if coord3 is not None and k != coord3:
                        continue
                    slice.append(self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k])
        return slice

    # методы возвращают срез массива по заданным координатам
    def GetValues0(self, i):
        return self.__get_slice(i, None, None)

    def GetValues1(self, j):
        return self.__get_slice(None, j, None)

    def GetValues2(self, k):
        return self.__get_slice(None, None, k)

    def GetValues01(self, i, j):
        return self.__get_slice(i, j, None)

    def GetValues02(self, i, k):
        return self.__get_slice(i, None, k)

    def GetValues12(self, j, k):
        return self.__get_slice(None, j, k)


    # устанавливают значения в массиве для заданных координат
    def SetValues0(self, i, arr):
        for j in range(self.__dim1):
            for k in range(self.__dim2):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[j][k]

    def SetValues1(self, j, arr):
        for i in range(self.__dim0):
            for k in range(self.__dim2):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[i][k]

    def SetValues2(self, k, arr):
        for i in range(self.__dim0):
            for j in range(self.__dim1):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[i][j]

    def SetValues01(self, i, j, arr):
        for k in range(self.__dim2):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[k]

    def SetValues02(self, i, k, arr):
        for j in range(self.__dim1):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[j]

    def SetValues12(self, j, k, arr):
        for i in range(self.__dim0):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = arr[i]


# функции для создания массива с элементами
def ones(dim0, dim1, dim2):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = 1
    return arr


def zeros(dim0, dim1, dim2):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = 0
    return arr


def fill(dim0, dim1, dim2, value):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = value
    return arr

# Создание массива с единичными элементами
arr_ones = ones(3, 3, 3)
print(arr_ones.GetValues0(0))  # Возвращает срез массива по первой координате (i, .., ..)
print(arr_ones.GetValues1(1))  # Возвращает срез массива по второй координате (.., j, ..)
print(arr_ones.GetValues2(2))  # Возвращает срез массива по третьей координате (.., .., k)
print(arr_ones.GetValues01(0, 1))  # Возвращает срез массива по первой и второй координатам (i, j, ..)
print(arr_ones.GetValues02(0, 2))  # Возвращает срез массива по первой и третьей координатам (i, .., k)
print(arr_ones.GetValues12(1, 2))  # Возвращает срез массива по второй и третьей координатам (.., j, k)

# Создание массива с нулевыми элементами
arr_zeros = zeros(2, 2, 2)
print(arr_zeros.GetValues0(1))
print(arr_zeros.GetValues1(0))
print(arr_zeros.GetValues2(1))
print(arr_zeros.GetValues01(1, 0))
print(arr_zeros.GetValues02(1, 1))
print(arr_zeros.GetValues12(0, 1))

# Создание массива с заданным значением
arr_fill = fill(2, 3, 4, 5)
print(arr_fill.GetValues0(1))
print(arr_fill.GetValues1(2))
print(arr_fill.GetValues2(3))
print(arr_fill.GetValues01(1, 2))
print(arr_fill.GetValues02(1, 3))
print(arr_fill.GetValues12(2, 3))

arr = Array3d(3, 4, 5)

values = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

arr.SetValues0(1, values)

print(arr.GetValues0(1))