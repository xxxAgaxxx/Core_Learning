class MutableString:
    def __init__(self, text):
        self.mut_string = list(text)

    def __str__(self):
        return ''.join(self.mut_string)

    def __len__(self):
        return len(self.mut_string)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return MutableString(self.mut_string[item.start:item.stop:item.step])
        else:
            return self.mut_string[item]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            # если срез с шагом не единица
            if key.step not in (1, None):
                # пытаемся заменить не пустой строкой
                if value != '':
                    # если число символов в строке равно числу символов в срезе — заменяем
                    if len(self.mut_string[key.start:key.stop:key.step]) == len(value):
                        self.mut_string[key.start:key.stop:key.step] = value
                    else:
                        raise ValueError(f'Нельзя заменить срез длины {len(self.mut_string[key.start:key.stop:key.step])} '
                                         f'на строку длины {len(value)}')
            else:
                # шаг единица, не пустая строка — заменяем срез исходной строки
                if value != '':
                    self.mut_string[key.start:key.stop:key.step] = value
                # шаг единица, не пустая строка — удаляем срез исходной строки
                else:
                    del self.mut_string[key.start:key.stop:key.step]
        elif value == '':
            del self.mut_string[key]
        elif len(value) == 1:
            self.mut_string[key] = value
        else:
            self.mut_string = self.mut_string[:key] + list(value) + self.mut_string[key + 1:]

    def __delitem__(self, key):
        if isinstance(key, slice):
            del self.mut_string[key.start:key.stop:key.step]
        else:
            del self.mut_string[key]

    def __add__(self, other):
        return MutableString(self.mut_string + list(other))

    def __radd__(self, other):
        return MutableString(list(other) + self.mut_string)

    def __mul__(self, other):
        return MutableString(self.mut_string + self.mut_string)


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
print('kek' + string)  # конкатенация с другой стороны kekoebtm
print(string * 2)  # питоновское умножение строк oebtmoebtm
string[::2] = '123'  # замена среза на строку mut_string = ['1', 'e', '2', 't', '3']
print(string)  # 1e2t3
