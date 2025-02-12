#Вариант 26.1. Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B (не включая числа A и B), а также количество N этих чисел.

def print_numbers_between(A, B):
    if A >= B:
        return "Ошибка: A должно быть меньше B."
    
    numbers = []
    
    for i in range(B - 1, A, -1):  # Идем от B-1 до A+1
        numbers.append(i)
    
    count = len(numbers)  # Количество чисел
    return numbers, count

def main():
    try:
        A = int(input("Введите целое число A: "))
        B = int(input("Введите целое число B: "))
        
        result = print_numbers_between(A, B)
        
        if isinstance(result, str):  # Если это сообщение об ошибке
            print(result)
        else:
            numbers, count = result
            print("Целые числа между A и B в порядке убывания:", numbers)
            print("Количество чисел:", count)
    except ValueError:
        print("Ошибка: введите корректные целые числа.")

if __name__ == "__main__":
    main()