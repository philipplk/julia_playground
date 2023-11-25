#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:14:34 2023

@author: philipp
"""

import numpy as np
import matplotlib.pyplot as plt
import mechanics

#  system parameters
gravity = 9.81
length = 1
mass = 1
E_matrix = np.diag([1, mass * length**2])
J_matrix = np.array([[0, 1], [-1, 0]])

#  integration parameters
timestepsize = 0.05  # timestep size
time_start = 0.0  # start time
time_end = 3.0  # end time
number_timestep = int((time_end - time_start) / timestepsize)  # number of time steps
newton_epsilon = 1e-7  # tolerance of Newton's method (norm of residual vector)
integrator = "euler_explicit"

#  initial values
angle_initial = 0.0  # initial angle
velocity_initial = 1.0  # initial angular velocity
state_initial = np.array([angle_initial, velocity_initial])  # initial state
state = np.zeros(
    (number_timestep + 2, 2)
)  # memory array containing all states during motion
state[0, :] = state_initial  # set initial values into memory array

system = mechanics.System(
    mass=mass,
    gravity=gravity,
    length=length,
    E_matrix=E_matrix,
    J_matrix=J_matrix,
)


solver = mechanics.Solver(
    system=system,
    timestepsize=timestepsize,
    newton_epsilon=newton_epsilon,
    integrator=integrator,
)


#  time-stepping
time = time_start
state_n = state_initial
state_n1 = state_initial
time_index = 0
while time < time_end:
    state_n = state_n1

    state_n1 = solver.newton_update(state_n1, state_n)
    state[time_index + 1, :] = state_n1

    time = time + timestepsize
    time_index = time_index + 1

#  Postprocessing: plot state evolution
plt.plot(state[:, 0])
