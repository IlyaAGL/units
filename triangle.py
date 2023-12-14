def area(a,h):
    # Входные данные: a, h (float64) - сторона и высота, падающая на эту сторону, треугольника
    # Выходные данные: Площадь прямоугольника (0.5 * a * h)
    if isinstance(a, int) and isinstance(h, int) and not isinstance(a, bool) and not isinstance(h, bool):
        if a >= 0 and h >= 0:
            return a * h * 0.5
        return "ONLY POSITIVE NUMBERS"
    else:
        return "WRONG ARGUMENT TYPE"

def perimeter(a,b,c):
    # Входные данные: a, b, c (float64) - стороны треугольника
    # Выходные данные: Площадь прямоугольника (a + b + c)
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and not isinstance(a, bool) and not isinstance(b, bool) and not isinstance(c, bool):
        if (a + b <= c) + (b + c <= a) + (a + c <= b) >= 1:
            return "THIS TRIANGLE DOESN'T EXIST"
        if a > 0 and b > 0 and c > 0:
            return a + b + c
        if a == 0 and b == 0 and c == 0:
            return 0
    else:
        return "WRONG ARGUMENT TYPE"