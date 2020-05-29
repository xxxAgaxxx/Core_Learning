def preincrement(num):
    global number
    number += 1
    return num + 1


def postincrement(num):
    global number
    number += 1
    return num


def predecrement(num):
    global number
    number -= 1
    return num - 1


def postdecrement(num):
    global number
    number -= 1
    return num


number = 1
print('Число', number)
print('Преинкремент', preincrement(number))
print('Число', number)
print('Постинкремент', postincrement(number))
print('Число', number)
print('Предекремент', predecrement(number))
print('Число', number)
print('Постдекремент', postdecrement(number))
print('Число', number)