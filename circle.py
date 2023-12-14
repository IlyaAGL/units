import math

def area(r):
    # Входные данные: r (float64) - радиус окружности
    # Выходные данные: Площадь окружности (r**2 * math.pi)
    if isinstance(r, int) and not isinstance(r, bool):
        if r >= 0:
            return math.pi * r * r
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"


def perimeter(r):
    # Входные данные: r (float64) - радиус окружности
    # Выходные данные: Длина окружности (2 * r * math.pi)
    if isinstance(r, int) and not isinstance(r, bool):
        if r >= 0:
            return 2 * math.pi * r
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"