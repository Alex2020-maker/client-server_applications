# Практическое задание #

import locale
import subprocess
import chardet
from chardet import detect

print("\nЗАДАНИЕ 1\n")

"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

# Решение
print("Тип и содержание переменных представленых в строковом формате:")

words = ["разработка", "сокет", "декоратор"]

for i in words:
    print(f"Тип -> {type(i)}, содержимое -> {i}")

print("\nТип и содержание преобразованных переменных с\
помощью онлайн-конвертера в формат Unicode: ")

words_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for w in words_unicode:
    print(f"Тип -> {type(w)}, содержимое -> {w}")

print("\nЗАДАНИЕ 2\n")

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. 
Сделать это необходимо в автоматическом, а не ручном режиме, с помощью 
добавления литеры b к текстовому значению, (т.е. ни в коем случае не 
используя методы encode, decode или функцию bytes) и определить тип, 
содержимое и длину соответствующих переменных.
"""

# Решение 1
list_w = ["class", "function", "method"]


def conversion_to_byte_type_words():

    for i in list_w:
        eval_word = eval(f"b'{i}'")
        print(f'Тип переменной -> {type(eval_word)}, содержимое -> {eval_word},\
    Длина переменной -> {len(eval_word)}')


conversion_to_byte_type_words()

print("\n Второй вариант решения ЗАДАНИЯ 2 с ввода слов через клавиатуру\n")

# Решение 2


def conversion_to_byte():
    # я использовала ввод слов с клавиатуры через пробел
    words_b = list(str(input("")).split())
    for i in words_b:
        eval_word = eval(f"b'{i}'")
        print(f'Тип переменной -> {type(eval_word)}, содержимое -> {eval_word},\
    Длина переменной -> {len(eval_word)}')


conversion_to_byte()

print("\nЗАДАНИЕ 3\n")

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно 
записать в байтовом типе. Важно: решение должно быть универсальным, т.е. 
не зависеть от того, какие конкретно слова мы исследуем.
"""
# Решение


def conversion_to_b_type():
    list_words = list(str(input("")).split())
    for i in list_words:
        if not i.isascii():
            print(f'Невозможно записать в байтовом типе слово {i}')
        else:
            print(f'Можно записать в байтовом типе слово {i}')


conversion_to_b_type()


print("\nЗАДАНИЕ 4\n")

"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из 
строкового представления в байтовое и выполнить обратное преобразование 
(используя методы encode и decode).
"""
# Решение

var6 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in var6:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))

print("\nЗАДАНИЕ 5\n")

"""
5.Написать код, который выполняет пинг веб-ресурсов yandex.ru, 
youtube.com и преобразовывает результат из байтовового типа 
данных в строковый без ошибок для любой кодировки операционной системы.
"""
# Решение


ping_resurs = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in ping_resurs:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0
    for line in ping_process.stdout:
        ping_result = chardet.detect(line)
        line = line.decode(ping_result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if i == 4:
            break
        i += 1

print("\nЗАДАНИЕ 6\n")

"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». Далее забыть о том,
 что мы сами только что создали этот файл и исходить из того, что перед 
 нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК 
 вне зависимости от того, в какой кодировке он был создан.
"""
# Решение

list_w = ['сетевое программирование', 'сокет', 'декоратор']

# Создаем файл
with open('test_file.txt', 'w+') as file:
    for i in list_w:
        file.write(i + '\n')
    file.seek(0)

# Узнаем кодировку файла

with open('test_file.txt', 'rb') as file:
    result_cod = file.read()
file_encoding = detect(result_cod)['encoding']

# Чтение из файла
with open('test_file.txt', 'r', encoding=file_encoding) as file:
    for i in file:
        print(i)
    file.seek(0)
