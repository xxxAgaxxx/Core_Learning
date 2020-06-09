from MutableInteger import MutableInteger


def preincrement(num):
    num.add(1)
    return num


def postincrement(num):
    tmp = MutableInteger(num)
    num.add()
    return tmp


def predecrement(num):
    num.sub()
    return num


def postdecrement(num):
    tmp = MutableInteger(num)
    num.sub()
    return tmp


number = MutableInteger(5)
print('Число', number.get())
print('Постинкремент', postincrement(number).get())
print('Число', number.get())
print('Преинкремент', preincrement(number).get())
print('Число', number.get())
print('Предекремент', predecrement(number).get())
print('Число', number.get())
print('Постдекремент', postdecrement(number).get())
print('Число', number.get())
