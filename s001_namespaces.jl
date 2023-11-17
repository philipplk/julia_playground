using Pkg
Pkg.add("Plots") # Equivalent to Python:`pip install Plots`
using Plots # Eqivalent to Python`import Plots`

# Julia / Python
# using package / from package import *
# import package / import package
# using .NiceStuff: nice, DOG / from .Niccestuff import nice, DOG

println("I'm excited to learn Julia!")

function advanced_print(; arg1, default1="Huhu")
    println("$default1 $arg1")
end

advanced_print(arg1="Phil")

include("module1.jl")
import .Ourfancymodule
b = Ourfancymodule.a
println("b=$b")
