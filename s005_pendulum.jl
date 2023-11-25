import LinearAlgebra as la
include("code.jl")
import .code: newton_update

# system parameters
gravity = 9.81
length::Float64 = 1
mass = 1.0
E_matrix::la.Diagonal{Float64,Vector{Float64}} = la.Diagonal([1.0, mass * length^2])
###################
# Different ways to create a Matrix, see also
# Separators ",", ";", "\n" between arguments concatenate vertically
# Separators " ", "\tab", ";;" between arguments concatenate horizontally
# https://docs.julialang.org/en/v1/manual/arrays/#man-array-concatenation
# J_matrix = [0.0 1.0; -1.0 0.0]
J_matrix = [[0.0 1.0]; [-1.0 0.0]]
# J_matrix = [
#     0.0 1.0
#     -1.0 0.0
# ]

# integration parameters
timestepsize = 0.05  # timestep size
time_start = 0.0  # start time
time_end = 3.0  # end time
number_timestep = trunc(Int, (time_end - time_start) / timestepsize)  # number of time steps
newton_epsilon = 1e-7  # tolerance of Newton's method (norm of residual vector)
integrator = "MP"  # EE (explicit Euler), IE (implicit Euler), MP (midpoint)

# initial values
angle_initial = 0.0  # initial angle
velocity_initial = 1.0  # initial angular velocity
state_initial = [angle_initial velocity_initial]  # initial state
state = zeros(number_timestep + 2, 2)  # memory array containing all states during motion
state[1, :] = state_initial  # set initial values into memory array

println("size(state)=$(size(state))")



time = time_start
state_n = state_initial
state_n1 = state_initial
time_index = 0

while time < time_end
    global state_n = state_n1

    global state_n1 = newton_update(state_n1=state_n1, state_n=state_n)
    println("state_n1=$state_n1")
    global state[time_index+1, :] = state_n1

    global time = time + timestepsize
    global time_index = time_index + 1
    println("time=$time")
end



