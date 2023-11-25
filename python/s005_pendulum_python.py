#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:14:34 2023

@author: philipp
"""

import numpy as np
import matplotlib.pyplot as plt

# %% system parameters
gravity = 9.81
length = 1
mass = 1
E_matrix = np.diag([1, mass * length**2])
J_matrix = np.array([[0, 1], [-1, 0]])

# %% integration parameters
timestepsize = 0.05  # timestep size
time_start = 0.0  # start time
time_end = 3.0  # end time
number_timestep = int((time_end - time_start) / timestepsize)  # number of time steps
newton_epsilon = 1e-7  # tolerance of Newton's method (norm of residual vector)
integrator = "MP"  # EE (explicit Euler), IE (implicit Euler), MP (midpoint)

# %% initial values
angle_initial = 0.0  # initial angle
velocity_initial = 1.0  # initial angular velocity
state_initial = np.array([angle_initial, velocity_initial])  # initial state
state = np.zeros(
    (number_timestep + 2, 2)
)  # memory array containing all states during motion
state[0, :] = state_initial  # set initial values into memory array


# %% functions
def compute(state_n1, state_n, integrator):
    """
    Parameters
    ----------
    state_n1 : 2x1 array of float64
        state at next timestep t_n+1 (i.e. an unknown).
    state_n : 2x1 array of float64
        state at last timestep t_n (i.e. known).
    integrator : str
        Name of the desired integration scheme.

    Returns
    -------
    residual : 2x1 array of float64
        residual vector of Newtons method.
    tangent : 2x2 array of float64
        tangent matrix of Newtons method.

    """
    if integrator == "EE":
        # explicit Euler, evaluates z at t_n
        z_n = get_z_vector(state_n)
        residual = E_matrix @ (state_n1 - state_n) - timestepsize * J_matrix @ z_n
        tangent = E_matrix

    elif integrator == "IE":
        # implicit Euler, evaluates z at t_n1
        z_n1 = get_z_vector(state_n1)
        dzn1_dxn1 = get_Jacobian(state_n1)
        residual = E_matrix @ (state_n1 - state_n) - timestepsize * J_matrix @ z_n1
        tangent = E_matrix - timestepsize * J_matrix @ dzn1_dxn1

    elif integrator == "MP":
        # Midpoint rule, evaluates z at t_n05
        state_n05 = 0.5 * (state_n + state_n1)
        z_n05 = get_z_vector(state_n05)
        dzn05_dxn1 = 0.5 * get_Jacobian(state_n1)
        residual = E_matrix @ (state_n1 - state_n) - timestepsize * J_matrix @ z_n05
        tangent = E_matrix - timestepsize * J_matrix @ dzn05_dxn1

    return residual, tangent


def newton_update(state_n1, state_n):
    """
    Parameters
    ----------
    state_n1 : 2x1 array of float64
        state at next timestep t_n+1 (i.e. an unknown).
    state_n : 2x1 array of float64
        state at last timestep t_n (i.e. known).

    Returns
    -------
    state_n1 : 2x1 array of float64
        iterated state at next timestep.

    """
    residual_norm = 1e5
    while residual_norm >= newton_epsilon:
        residual, tangent_matrix = compute(state_n1, state_n, integrator)
        state_delta = -np.linalg.inv(tangent_matrix) @ residual
        state_n1 = state_n1 + state_delta
        residual_norm = np.linalg.norm(residual)
    return state_n1


def get_z_vector(state):
    """

    Parameters
    ----------
    state : 2x1 array of float64
        state vector x=(q,v).

    Returns
    -------
    2x1 array of float64
        Vector z=z(x).

    """
    q = state[0]
    v = state[1]
    return np.array([mass * gravity * length * np.sin(q), v])


def get_Jacobian(state):
    """

    Parameters
    ----------
    state : 2x1 array of float64
        state vector x=(q,v).

    Returns
    -------
    2x2 array of float64
        Jacobian of z=z(x), i.e. dz/dx.

    """
    q = state[0]
    v = state[1]
    return np.diag([mass * gravity * length * np.cos(q), 1])


# %% time-stepping
time = time_start
state_n = state_initial
state_n1 = state_initial
time_index = 0
while time < time_end:
    state_n = state_n1

    state_n1 = newton_update(state_n1, state_n)
    state[time_index + 1, :] = state_n1

    time = time + timestepsize
    time_index = time_index + 1

# %% Postprocessing: plot state evolution
plt.plot(state[:, 0])
