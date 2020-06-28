inputList = System.console().readLine().toList()
newList = inputList.findAll{element -> element.toInteger()%2 == 0}
print(newList.sort().reverse())