public class MutableInteger
{
    public MutableInteger(int value) {
        this.value = value;
    }
    public MutableInteger(MutableInteger value) {
        this.value = value.value;
    }
    public void add(int value) {
        this.value += value;
    }
    public void sub(int value) {
        this.value -= value;
    }
    public int get() {
        return value;
    }

    private int value;
}

MutableInteger preincrement(num) {
    num.add(1)
    return num
}

MutableInteger postincrement(num) {
    tmp = new MutableInteger(num)
    num.add(1)
    return tmp
}


MutableInteger predecrement(num) {
    num.sub(1)
    return num
}


MutableInteger postdecrement(num) {
    tmp = new MutableInteger(num)
    num.sub(1)
    return tmp
}


def number = new MutableInteger(5)
println('Число ' + number.get())
println('Постинкремент ' + postincrement(number).get())
println('Число ' + number.get())
println('Преинкремент ' + preincrement(number).get())
println('Число ' + number.get())
println('Предекремент ' + predecrement(number).get())
println('Число ' + number.get())
println('Постдекремент ' + postdecrement(number).get())
println('Число ' + number.get())
