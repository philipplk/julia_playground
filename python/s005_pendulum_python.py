"""
Created on Wed Nov 22 18:14:34 2023

@author: philipp
"""


import numpy as np
import matplotlib.pyplot as plt
import simulation

# System parameters
system = simulation.System(
    mass=1.0,
    gravity=9.81,
    length=1.0,
)

# Timestepper parameters

timeStepper = simulation.TimeStepper(
    timestepsize=0.05,  # timestep size
    time_start=0.0,  # start time
    time_end=3.0,  # end time
)

# Solver parameters
solver = simulation.Solver(
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
