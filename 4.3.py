where_i_was = input('Расскажи где ты был через ПРОБЕЛ\n').split()
what_a_trip = dict()
for place in where_i_was:
    if place not in what_a_trip.keys():
        what_a_trip[place] = 0
    what_a_trip[place] += 1
print(what_a_trip)
