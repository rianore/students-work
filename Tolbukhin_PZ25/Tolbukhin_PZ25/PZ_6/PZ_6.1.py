#Дан целочисленный список размера 10.
#Вывести вначале все содержащиеся в данном списке четные числа в порядке возрастания их индексов,
# а затем - все нечетные числа в порядке убывания их индексов.
import random
spisok = []
numbers = [random.randint(0, 999) for _ in range(11)]
print(numbers)

even_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 == 0] #поход по индексам ч
odd_numbers = [numbers[i] for i in range(len(numbers)-1, -1, -1) if numbers[i] % 2 != 0]

print("Четные числа (в порядке возрастания индексов):", even_numbers)
print("Нечетные числа (в порядке убывания индексов):", odd_numbers)