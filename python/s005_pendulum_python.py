"""
Created on Wed Nov 22 18:14:34 2023

@author: philipp
"""

# Notes:
# The time stepping scheme is currently rather naive:
# The systems behavior usually depends on teh time aswell.
# The solver should adapt the timestepping based on quality measures
# The length of the solution (state) currently depends on setting of the timestepping
# Ususally the number of iterations required to archive a satisfactory precision is not known a priori
# From an engineering point of view, we request the solution at specific points in time and the time stepping
# combined with the solver should do what it needs to do to get the solution at the specified points in time.


import numpy as np
import matplotlib.pyplot as plt
import mechanics

# System parameters
mass = 1.0
length = 1.0
system = mechanics.System(
    mass=mass,
    gravity=9.81,
    length=length,
    E_matrix=np.diag([1, mass * length**2]),
    J_matrix=np.array([[0, 1], [-1, 0]]),
)
del mass, length

# Timestepper parameters

timeStepper = mechanics.TimeStepper(
    timestepsize=0.05,  # timestep size
    time_start=0.0,  # start time
    time_end=3.0,  # end time
)

# Solver parameters
solver = mechanics.Solver(
    system=system,
    timeStepper=timeStepper,
    newton_epsilon=1e-7,  # tolerance of Newton's method (norm of residual vector),
    integrator="midpoint",
)

# Initial values
angle_initial = 0.0  # initial angle
velocity_initial = 1.0  # initial angular velocity
state_initial = np.array([angle_initial, velocity_initial])  # initial state


# Do something

solution = solver.solve(state_initial=state_initial)


#  Postprocessing: plot state evolution
plt.plot(solution[:, 0])
