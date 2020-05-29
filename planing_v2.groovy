Set validValues = ['0', '0.5', '1/2', '1', '2', '3', '5', '8', '13', '20', '40', '100', 'coffee', '?']
String plan_guess = System.console().readLine()
if (plan_guess in validValues)
    println('poker')
else if (plan_guess in ['break', 'pause', 'zzz'])
    println('coffee')
else if (!(plan_guess.isNumber()) ||
        (plan_guess.toFloat() > 100) ||
        (plan_guess.toFloat() < 0))
    println('?')
else
    switch (plan_guess.toDouble()) {
        case { it < 0.25 }:
            println(0); break
        case { it < 0.75 }:
            println(0.5); break
        case { it < 1.5 }:
            println(1); break
        case { it < 2.5 }:
            println(2); break
        case { it < 4.0 }:
            println(3); break
        case { it < 6.5 }:
            println(5); break
        case { it < 10.5 }:
            println(8); break
        case { it < 16.5 }:
            println(13); break
        case { it < 30.0 }:
            println(20); break
        case { it < 70.0 }:
            println(40); break
        default: println 100
    }
