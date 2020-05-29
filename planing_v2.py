import random

# plan_guess = random.uniform(-20,120)
# print(plan_guess)
plan_guess = input()
valid_values = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100]
if plan_guess in {'break', 'pause', 'zzz'}:
    print('coffee')
elif plan_guess in ('1/2', 'coffee', '?') or (plan_guess.isnumeric() and int(plan_guess) in valid_values):
    print('poker')
else:
    try:
        plan_guess = float(plan_guess)
    except ValueError:
        print('?')
    else:
        if not(0 <= plan_guess <= 100):
            print('?')
        else:
            plan_guess = float(plan_guess)
            difference = 100
            for i in valid_values:
                dif = abs(i - plan_guess)
                if difference >= dif:
                    difference = dif
                    nearest = i
                if difference == 0:
                    print(int(plan_guess))
                    break
            else:
                print(nearest)
