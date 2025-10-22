#Дана строка, содержащая полное имя файла. Выделить из этой строки название последнего каталога (без символов "\").
#Если файл содержится ы корневом каталоге, то вывести символ "\".
def extract_last_directory(full_path):
    directories = full_path.split("\\")
    if len(directories) == 1:  # Если только один элемент, значит файл в корневом каталоге
        return "\\"
    else:
        return directories[-2]

file_path = "C:\\Users\\Username\\file.txt"
result = extract_last_directory(file_path)
print(result)
