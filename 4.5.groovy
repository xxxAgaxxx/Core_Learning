public class MutableString
{
    public MutableString(String text) {
        this.text = text;
    }
    public MutableString(MutableString string) {
        this.text = string.text;
    }
    public lenght() {
        return this.text.length()
    }
    public String get() {
        return text;
    }
    // вставляет new_text вместо символа position
    public modify (Integer position, String new_text) {
        if (position == 0) this.text = new_text + this.text.substring(1)
        else if (position >= this.text.length() || position == -1) this.text = this.text + new_text
        else this.text = this.text.substring(0, position-1) + new_text + this.text.substring(position)
    }
    // вставляет new_text вместо символа по срезу
    public modify (IntRange position, String new_text) {
        if (position == 0) this.text = new_text + this.text.substring(position[-1])
        else if (position[0] >= this.text.length()) this.text = this.text + new_text
        else this.text = this.text.substring(0, position[0]) + new_text + this.text.substring(position[-1])
    }
    private String text;
}

mut_string = new MutableString('some text')
println(mut_string.lenght())    // 9
println(mut_string.get())   // some text
mut_string.modify(0..4, 'no')
println(mut_string.get())   // no text
mut_string.modify(-1, ' added')
println(mut_string.get())   // no text added
