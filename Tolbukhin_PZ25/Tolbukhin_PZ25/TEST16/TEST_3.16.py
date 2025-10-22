#Создать класс Person c одиним атрибутом класса (count), c конструктором __init__
#и одним статистическим методом.  Увеличение количества созданных экземпляров обеспечить в конструкторе __init__
#Статический метод total_people должен обеспечивать построение и вывод фразы
# о количестве созданных экземпляров.
class Person:
    count = 0


    # методы
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @staticmethod
    def total_people():
        return(f'Создано {Person.count} объектов')

bob=Person('bob')
Mark=Person('mark')
print(Person.total_people())