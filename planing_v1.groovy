Set validValues = ['0', '0.5', '1/2', '1', '2', '3', '5',
                   '8', '13', '20', '40', '100', '?', 'coffee']
String poker = System.console().readLine()
if (poker in validValues) {
    println('poker')
}
else {
    println('error')
}
