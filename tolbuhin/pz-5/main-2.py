#Вариант 26.2. Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный (K — параметр целого типа, являющийся одновременно входным и выходным). С помощью этой функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.

def InvertDigits(K):
    # Преобразуем число в строку, переворачиваем и возвращаем обратно в целое число
    K = int(str(K)[::-1])
    return K

def main():
    numbers = []
    
    print("Введите 5 целых положительных чисел:")
    for _ in range(5):
        while True:
            try:
                num = int(input())
                if num <= 0:
                    print("Ошибка: число должно быть положительным.")
                else:
                    numbers.append(num)
                    break
            except ValueError:
                print("Ошибка: введите корректное целое число.")
    
    # Применяем функцию InvertDigits к каждому числу
    inverted_numbers = [InvertDigits(num) for num in numbers]
    
    print("Обратный порядок цифр для введенных чисел:")
    for original, inverted in zip(numbers, inverted_numbers):
        print(f"{original} -> {inverted}")

if __name__ == "__main__":
    main()