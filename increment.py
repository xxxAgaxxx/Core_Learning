from MutableInteger import MutableInteger

def preincrement(num):
    num.add(1)
    return num.get()


def postincrement(num):
    tmp = num.get()
    num.add(1)
    return tmp


def predecrement(num):
    num.sub(1)
    return num.get()


def postdecrement(num):
    tmp = num.get()
    num.sub(1)
    return tmp


number = MutableInteger(1)
print('Число', number.get())
print('Преинкремент', preincrement(number))
print('Число', number.get())
print('Постинкремент', postincrement(number))
print('Число', number.get())
print('Предекремент', predecrement(number))
print('Число', number.get())
print('Постдекремент', postdecrement(number))
print('Число', number.get())