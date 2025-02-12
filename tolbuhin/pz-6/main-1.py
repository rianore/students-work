#Вариант 26.1. Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.

def check_alternation(A):
    N = len(A)
    
    if N < 2:
        return "Ошибка: размер списка должен быть не менее 2."
    
    for i in range(1, N):
        if (A[i] > 0 and A[i - 1] > 0) or (A[i] < 0 and A[i - 1] < 0):
            return i + 1  # Возвращаем порядковый номер (индекс + 1)
    
    return 0  # Если чередуются

def main():
    try:
        N = int(input("Введите размер списка N (N > 1): "))
        
        if N < 2:
            print("Ошибка: размер списка должен быть не менее 2.")
            return
        
        A = []
        print(f"Введите {N} ненулевых целых чисел:")
        for _ in range(N):
            while True:
                try:
                    element = int(input())
                    if element == 0:
                        print("Ошибка: число не должно быть нулевым.")
                    else:
                        A.append(element)
                        break
                except ValueError:
                    print("Ошибка: введите корректное целое число.")
        
        result = check_alternation(A)
        print(result)
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()