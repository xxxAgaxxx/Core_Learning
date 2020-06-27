students_dict = ['Коля':'1000', 'Вася':'500', 'Петя':'200']
task_sum = 0
students_dict.each{
    task_sum += it.value.toInteger()
}
println(task_sum)
