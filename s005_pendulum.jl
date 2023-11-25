import LinearAlgebra as la


# system parameters
gravity = 9.81
length::Float64 = 1
mass = 1.0

E_matrix::la.Diagonal{Float64,Vector{Float64}} = la.Diagonal([1.0, mass * length^2])
# J_matrix = [0.0 1.0; -1.0 0.0]
J_matrix = [[0.0 1.0]; [-1.0 0.0]]
# J_matrix = [
#     0.0 1.0
#     -1.0 0.0
# ]


