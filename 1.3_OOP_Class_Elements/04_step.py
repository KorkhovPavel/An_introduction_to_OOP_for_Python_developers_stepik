# Создайте класс Book, в котором будут атрибуты name и author, со значениями из input.
# Затем выведите значения.
#
# Input  и Output должны быть в следующем формате:
#
# Sample Input:
#
# Преступление и наказание
# Федор Михайлович Достоевский
# Страх и Трепет
# Сёрен Кьеркегор
# Голова профессора Доуэля
# Александр Романович Беляев
# Sample Output:
#
# Преступление и наказание - Федор Михайлович Достоевский
# Страх и Трепет - Сёрен Кьеркегор
# Голова профессора Доуэля - Александр Романович Беляев


from sys import stdin

lst = []
for line in stdin:
    lst.append(line.rstrip())


class Book:
    name = lst[0]
    author = lst[1]
    name_author = f"{name} - {author}"

    def f(self):
        lst_1 = [lst[i:i + 2] for i in range(0, len(lst), 2)]
        for i in lst_1:
            Book.name = i[0]
            Book.author = i[1]
            if Book.name is not None and Book.author is not None:
                print(f'{Book.name} - {Book.author}')


f1 = Book()
f1.f()
