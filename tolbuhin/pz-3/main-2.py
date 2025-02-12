#Вариант 26.2. Даны целые числа a, b, c. Проверить истинность высказывания: «Существует треугольник со сторонами a, b, c».

def check_triangle_existence(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "Треугольник существует."
    else:
        return "Треугольник не существует."

def main():
    try:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        
        result = check_triangle_existence(a, b, c)
        print(result)
    except ValueError:
        print("Ошибка: введите корректные целые числа.")

if __name__ == "__main__":
    main()