def a(filename): # функция
    try:
        with open(filename, 'r', encoding='utf-8') as file: # открытие файла 
            text = file.read() # чтение содржимого файла
            words = text.split() # раздеение текста на слова
            return len(words) # возврат количества слов
    except FileNotFoundError:
        return "Файл не найден."
        # если файл не найден, то функция возвращает строку
filename = 'text.txt' # имя файла 
word = a(filename) # вызов функции
print(f'Количество слов в файле {filename}: {word}') # вывод