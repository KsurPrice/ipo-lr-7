def isCorrectRect(rect): #rect: список из двух кортежей [(x1, y1), (x2, y2)]
#первый кортеж — координаты левого нижнего угла
#второй кортеж — координаты правого верхнего угла
    (x1, y1), (x2, y2) = rect #True — если прямоугольник корректен (x1 < x2 и y1 < y2) False — если прямоугольник некорректен
    #первый кортеж — координаты левого нижнего угла
    #второй кортеж — координаты правого верхнего угла
    return x1 < x2 and y1 < y2

class RectCorrectError(Exception):     #Ошибка корректности прямоугольника
    pass


def isCollisionRect(rect1, rect2): #Аргументы:
#rect1, rect2: списки из двух кортежей [(x1, y1), (x2, y2)]
#первый кортеж: координаты левого нижнего угла
#второй кортеж: координаты правого верхнего угла
#Проверка пересечения двух прямоугольников.
# Возвращает:
#True — если прямоугольники пересекаются
#False — если не пересекаются
# Исключения:
#RectCorrectError — если хотя бы один прямоугольник некорректен
#Проверка корректности первого прямоугольника
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")

    # Проверка корректности второго прямоугольника
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    # Распаковка координат
    (x1, y1), (x2, y2) = rect1
    (a1, b1), (a2, b2) = rect2

    # Условие непересечения:
    # - один прямоугольник полностью слева
    # - или полностью справа
    # - или полностью выше
    # - или полностью ниже
    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return False

    return True

def intersectionAreaRect(rect1, rect2):
    # Проверка корректности входных данных
    if not isCorrectRect(rect1):
        raise ValueError("Первый прямоугольник некорректен")
    if not isCorrectRect(rect2):
        raise ValueError("Второй прямоугольник некорректен")

    # Распаковка координат
    (x1, y1), (x2, y2) = rect1
    (a1, b1), (a2, b2) = rect2

    # Вычисление ширины и высоты пересечения
    dx = min(x2, a2) - max(x1, a1)
    dy = min(y2, b2) - max(y1, b1)

    # Если пересечение есть — возвращаем площадь
    if dx > 0 and dy > 0:
        return dx * dy

    # Иначе — пересечения нет
    return 0

def intersectionAreaMultiRect(rectangles):
    # Проверка корректности всех прямоугольников
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"{i+1}-й прямоугольник некорректный")

    # Начинаем с координат первого прямоугольника
    (x1, y1), (x2, y2) = rectangles[0]

    # Последовательно пересекаем с остальными
    for (a1, b1), (a2, b2) in rectangles[1:]:
        x1 = max(x1, a1)
        y1 = max(y1, b1)
        x2 = min(x2, a2)
        y2 = min(y2, b2)

        # Если пересечения нет — сразу возвращаем 0
        if x1 >= x2 or y1 >= y2:
            return 0

    # Вычисляем площадь пересечения
    return (x2 - x1) * (y2 - y1)