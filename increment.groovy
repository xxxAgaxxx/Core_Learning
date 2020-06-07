import Mutable
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

Integer preincrement(num) {
    num.add(1)
    return num.get()
}

Integer postincrement(num) {
    tmp = num.get()
    num.add(1)
    return tmp
}


Integer predecrement(num) {
    num.sub(1)
    return num.get()
}


Integer postdecrement(num) {
    tmp = num.get()
    num.sub(1)
    return tmp
}


def number = new MutableInteger(1)
println('Число ' + number.get())
println('Преинкремент ' + preincrement(number))
println('Число ' + number.get())
println('Постинкремент ' + postincrement(number))
println('Число ' + number.get())
println('Предекремент ' + predecrement(number))
println('Число ' + number.get())
println('Постдекремент ' + postdecrement(number))
println('Число ' + number.get())
