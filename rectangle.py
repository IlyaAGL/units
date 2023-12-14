def area(a,b):
    # Входные данные: a, b (float64) - стороны прямоугольника
    # Выходные данные: Площадь прямоугольника (a * b)
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool):
        if a >= 0 and b >= 0:
            return a * b
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"

def perimeter(a,b):
    # Входные данные: a, b (float64) - стороны прямоугольника
    # Выходные данные: Периметр прямоугольника (2 * (a + b))
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool):
        if a > 0 and b > 0:
            return (a + b) * 2
        if a == 0 and b == 0:
            return 0
        return "ONLY POSITIVE NUMBERS OR ALL ARE ZERO"
    else:
        return "WRONG ARGUMENT TYPE"