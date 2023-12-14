def area(a):
    # Входные данные: a (float64) - сторона квадрата
    # Выходные данные: Площадь квадрата (a**2) 
    if isinstance(a, int) and not isinstance(a, bool):
        if a >= 0:
            return a**2
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"


def perimeter(a):
    # Входные данные: a (float64) - сторона квадрата
    # Выходные данные: Площадь квадрата (4 * a) 
    if isinstance(a, int) and not isinstance(a, bool):
        if a >= 0:
            return 4 * a
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"