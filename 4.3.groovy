tripReport = System.console().readLine('Расскажи где ты был через ПРОБЕЛ\n').split()
places = [:]
for (newPlace in tripReport){
    places[newPlace] = places[newPlace] ? places[newPlace] + 1 : 1
}
print(places)
