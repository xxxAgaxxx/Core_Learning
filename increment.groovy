Integer preincrement(Integer num) {
    number += 1
    return num + 1
}

Integer postincrement(Integer num) {
    number += 1
    return num
}


Integer predecrement(Integer num) {
    number -= 1
    return num - 1
}


Integer postdecrement(Integer num) {
    number -= 1
    return num
}


number = 1
println('Число ' + number)
println('Преинкремент ' + preincrement(number))
println('Число ' + number)
println('Постинкремент ' + postincrement(number))
println('Число ' + number)
println('Предекремент ' + predecrement(number))
println('Число ' + number)
println('Постдекремент ' + postdecrement(number))
println('Число ' + number)