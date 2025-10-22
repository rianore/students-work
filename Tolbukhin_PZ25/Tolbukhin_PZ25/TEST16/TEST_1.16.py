#Изменить консткруктор класса Note, добавив атрибут iscompleted (True/False).
#Создать экземпляр с новым атрибутом, вывести все значения собстсвенных
# атрибутов экземпляра (__dict__).
#Обеспечить увеличение count на величину, передаваемую в качестве аргумента
#Создать новую функцию reset_count, которачя будет обнулять счетчик выполненных задач
#Проверить содержимое магической пременной __dict__
class Note:
    def __init__(self, text, iscompleted):
        # получить доступ к атрибуту
        self.text = text
        self.iscompleted = iscompleted
        self.count = 0

    def upcount(self, int):
        self.count += int

    def reset_count(self):
        self.count = 0
note1 = Note("Задача 1", True)
print(note1.__dict__)
note1.upcount(3)
print(note1.__dict__)
note1.reset_count()
print(note1.__dict__)

