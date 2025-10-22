# 1 Создайте класс Image
# 2. У каждого экземпляра класса должно быть три собственных атрибута
# -resolution
# -title
# -extension
# 3. В классе должен быть метод resize, c помощью которого можно поменять разрешение изображения.
# 4. В классе должен быть метод title.upper, с помощью которого можно имя файла записать в верхнем регистре
# 5. Создайте несколько экземпляров класса Image и вызовите для каждого метод resize

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_size):
        self.resolution = new_size

    def title_upper(self):
        self.title = self.title.upper()

image1 = Image('200*200', 'cat', '.png')
image2 = Image('300*300', 'dog', '.jng')
image3 = Image('400*400', 'cow', '.jpeg')

print(image1.__dict__)
image1.resize('500*500')
image1.title_upper()
print(image1.__dict__)
