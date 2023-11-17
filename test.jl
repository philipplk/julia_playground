println("I'm excited to learn Julia!")

function advanced_print(; arg1, default1="Huhu")
    println("$default1 $arg1")
end

advanced_print(arg1="Phil")