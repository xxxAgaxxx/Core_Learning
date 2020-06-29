class MutableString(str):
    def __init__(self, text):
        self.mut_string = text

    def __str__(self):
        return self.mut_string

    def __getitem__(self, item):
        if isinstance(item, slice):
            return MutableString(self.mut_string[item.start:item.stop:item.step])
        else:
            return MutableString(self.mut_string[item])

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            # если срез с шагом не единица
            if key.step not in (1, None):
                temp_list = list(self.mut_string)
                # пытаемся заменить не пустой строкой
                if value != '':
                    # если число символов в строке равно числу символов в срезе — заменяем
                    if len(self.mut_string[key.start:key.stop:key.step]) == len(value):
                        temp_list[key.start:key.stop:key.step] = value
                        self.mut_string = MutableString(''.join(temp_list))
                    else:
                        raise ValueError(f'Нельзя заменить срез длины {len(self.mut_string[key.start:key.stop:key.step])} '
                                         f'на строку длины {len(value)}')
            else:
                # шаг единица, не пустая строка — заменяем срез исходной строки
                if value != '':
                    self.mut_string = list(self.mut_string)
                    self.mut_string[key.start:key.stop:key.step] = value
                    self.mut_string = MutableString(''.join(self.mut_string))
                # шаг единица, не пустая строка — удаляем срез исходной строки
                else:
                    self.mut_string = list(self.mut_string)
                    del self.mut_string[key.start:key.stop:key.step]
                    self.mut_string = MutableString(''.join(self.mut_string))
        elif value == '':
            self.mut_string = list(self.mut_string)
            del self.mut_string[key]
            self.mut_string = MutableString(''.join(self.mut_string))
        elif len(value) == 1:
            self.mut_string[key] = value
        else:
            self.mut_string = self.mut_string[:key] + value + self.mut_string[key + 1:]

    def __delitem__(self, key):
        if isinstance(key, slice):
            self.mut_string = list(self.mut_string)
            del self.mut_string[key.start:key.stop:key.step]
            self.mut_string = MutableString(''.join(self.mut_string))
        else:
            self.mut_string = list(self.mut_string)
            del self.mut_string[key]
            self.mut_string = MutableString(''.join(self.mut_string))

    def __add__(self, other):
        return MutableString(self.mut_string + other)

    def __radd__(self, other):
        return MutableString(list(other) + self.mut_string)




string = MutableString('mutable')  # инициализация mut_string = ['m', 'u', 't', 'a', 'b', 'l', 'e']
print(string, len(string))  # mutable 7
string[1] = 'foo'  # замена символа на подстроку mut_string = ['m', 'f', 'o', 'o', 't', 'a', 'b', 'l', 'e']
print(string, string[1])  # mfootable f
string[1] = ''  # замена символа на пустую подстроку mut_string = ['m', 'o', 'o', 't', 'a', 'b', 'l', 'e']
print(string)  # mootable
del string[1]  # удаление символа mut_string = ['m', 'o', 't', 'a', 'b', 'l', 'e']
print(string)  # motable
string += 'lol'  # конкатенация строк mut_string = ['m', 'o', 't', 'a', 'b', 'l', 'e', 'l', 'o', 'l']
print(string)  # motablelol
string = string[::-1]  # получение символов срезом mut_string = ['l', 'o', 'l', 'e', 'l', 'b', 'a', 't', 'o', 'm']
print(string[:3])  # получение символов срезом lol
del string[::2]  # удаление символов срезом mut_string = ['o', 'e', 'b', 't', 'm']
print(string)  # oebtm
print(string * 2)  # питоновское умножение строк oebtmoebtm
string[::2] = '123'  # замена среза на строку mut_string = ['1', 'e', '2', 't', '3']
print(string)  # 1e2t3
print(string.capitalize())