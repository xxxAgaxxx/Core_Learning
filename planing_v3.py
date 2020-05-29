def is_valid(value):
    if value in {'break', 'pause', 'zzz', '1/2', 'coffee', '?'}:
        return True
    try:
         if 0 <= float(value) <= 100:
             return True
    except ValueError:
        return False


def most_suitable(value, cards):
    if value in cards[0] or value in cards[1]:
        return 'poker'
    elif value in {'break', 'pause', 'zzz'}:
        return 'coffee'
    else:
        return nearest(float(value), cards[0])


def nearest(value, cards):
    for i in range(len(cards)-1):
        if value < (float(cards[i+1]) + float(cards[i])) / 2:
            return cards[i]
    else:
        return cards[i+1]


plan_guess = input()
deck = [['0', '0.5', '1', '2', '3', '5', '8', '13', '20', '40', '100'], {'1/2', 'coffee', '?'}]
print(most_suitable(plan_guess, deck) if is_valid(plan_guess) else '?')
