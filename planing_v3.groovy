boolean isValid(String guess, List valid) {
    if (guess in valid || (guess.isNumber() && guess.toFloat() <= 100 && guess.toFloat() >= 0))
        return true
    return false
}

String mostSuitable(String value, List valid) {
    if (value in valid[0] || value in valid[1])
        return 'poker'
    else if (value in valid[2])
        return 'coffee'
    return nearest(value.toFloat(), valid[0])
}

Integer nearest(Float guess, List points) {
    for(i = 0; i < points.size()-1; ++i) {
        if (guess < (points[i+1].toFloat() + points[i].toFloat()) / 2) {
            return points[i].toInteger()
        }
    }
    return points[-1].toInteger()
}

List validValues = [['0', '0.5', '1', '2', '3', '5', '8', '13', '20', '40', '100'],
                    ['1/2', 'coffee', '?'], ['break', 'pause', 'zzz']]
String plan_guess = System.console().readLine()
println(isValid(plan_guess, validValues.flatten()) ?
        mostSuitable(plan_guess, validValues) : '?')
