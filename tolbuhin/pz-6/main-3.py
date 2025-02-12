#Вариант 26.3. Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти такую точку из данного множества, сумма расстояний от которой до остальных его точек минимальна, и саму эту сумму. Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2. Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс, второй — для хранения ординат.

import math

def main():
    try:
        N = int(input("Введите количество точек N (N > 2): "))
        
        if N <= 2:
            print("Ошибка: количество точек должно быть больше 2.")
            return
        
        x_coords = []
        y_coords = []
        
        print("Введите координаты точек (x, y):")
        for i in range(N):
            x = float(input(f"Точка {i + 1} - x: "))
            y = float(input(f"Точка {i + 1} - y: "))
            x_coords.append(x)
            y_coords.append(y)
        
        min_sum_distance = float('inf')
        best_point_index = -1
        
        # Находим точку с минимальной суммой расстояний
        for i in range(N):
            sum_distance = 0
            for j in range(N):
                if i != j:  # Не учитываем расстояние до самой себя
                    distance = math.sqrt((x_coords[j] - x_coords[i]) ** 2 + (y_coords[j] - y_coords[i]) ** 2)
                    sum_distance += distance
            
            if sum_distance < min_sum_distance:
                min_sum_distance = sum_distance
                best_point_index = i
        
        # Выводим результат
        print(f"Точка с минимальной суммой расстояний: ({x_coords[best_point_index]}, {y_coords[best_point_index]})")
        print(f"Минимальная сумма расстояний: {min_sum_distance:.2f}")
    
    except ValueError:
        print("Ошибка: введите корректные значения.")

if __name__ == "__main__":
    main()