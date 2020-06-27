def newList = []
inputList = System.console().readLine().toList()
for (number in inputList){
    if (number.toInteger()%2 == 0) newList << number
}
print(newList.sort().reverse())
