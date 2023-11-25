#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:14:34 2023

@author: philipp
"""

import numpy as np
import matplotlib.pyplot as plt

# %% system parameters
g = 9.81
l = 1
m = 1
E = np.diag([1, m * l * l])
J = np.array([[0, 1], [-1, 0]])

# %% integration parameters
h = 0.05  # timestep size
t_0 = 0.0  # start time
t_1 = 3.0  # end time
NT = int((t_1 - t_0) / h)  # number of time steps
epsilon = 1e-7  # tolerance of Newton's method (norm of residual vector)
name_int = "MP"  # EE (explicit Euler), IE (implicit Euler), MP (midpoint)

# %% initial values
phi_0 = 0.0  # initial angle
omega_0 = 1.0  # initial angular velocity
x_0 = np.array([phi_0, omega_0])  # initial state
x = np.zeros((NT + 2, 2))  # memory array containing all states during motion
x[0, :] = x_0  # set initial values into memory array


# %% functions
def compute(x_n1, x_n, name_int):
    """
    Parameters
    ----------
    x_n1 : 2x1 array of float64
        state at next timestep t_n+1 (i.e. an unknown).
    x_n : 2x1 array of float64
        state at last timestep t_n (i.e. known).
    name_int : str
        Name of the desired integration scheme.

    Returns
    -------
    residual : 2x1 array of float64
        residual vector of Newtons method.
    tangent : 2x2 array of float64
        tangent matrix of Newtons method.

    """
    if name_int == "EE":
        # explicit Euler, evaluates z at t_n
        z_n = get_z_vector(x_n)
        residual = E @ (x_n1 - x_n) - h * J @ z_n
        tangent = E

    elif name_int == "IE":
        # implicit Euler, evaluates z at t_n1
        z_n1 = get_z_vector(x_n1)
        dzn1_dxn1 = get_Jacobian(x_n1)
        residual = E @ (x_n1 - x_n) - h * J @ z_n1
        tangent = E - h * J @ dzn1_dxn1

    elif name_int == "MP":
        # Midpoint rule, evaluates z at t_n05
        x_n05 = 0.5 * (x_n + x_n1)
        z_n05 = get_z_vector(x_n05)
        dzn05_dxn1 = 0.5 * get_Jacobian(x_n1)
        residual = E @ (x_n1 - x_n) - h * J @ z_n05
        tangent = E - h * J @ dzn05_dxn1

    return residual, tangent


def newton_update(x_n1, x_n):
    """
    Parameters
    ----------
    x_n1 : 2x1 array of float64
        state at next timestep t_n+1 (i.e. an unknown).
    x_n : 2x1 array of float64
        state at last timestep t_n (i.e. known).

    Returns
    -------
    x_n1 : 2x1 array of float64
        iterated state at next timestep.

    """
    resi = 1e5
    while resi >= epsilon:
        R, K = compute(x_n1, x_n, name_int)
        x_delta = -np.linalg.inv(K) @ R
        x_n1 = x_n1 + x_delta
        resi = np.linalg.norm(R)
    return x_n1


def get_z_vector(x):
    """

    Parameters
    ----------
    x : 2x1 array of float64
        state vector x=(q,v).

    Returns
    -------
    2x1 array of float64
        Vector z=z(x).

    """
    q = x[0]
    v = x[1]
    return np.array([m * g * l * np.sin(q), v])


def get_Jacobian(x):
    """

    Parameters
    ----------
    x : 2x1 array of float64
        state vector x=(q,v).

    Returns
    -------
    2x2 array of float64
        Jacobian of z=z(x), i.e. dz/dx.

    """
    q = x[0]
    v = x[1]
    return np.diag([m * g * l * np.cos(q), 1])


# %% time-stepping
t = t_0
x_n = x_0
x_n1 = x_0
k = 0
while t < t_1:
    x_n = x_n1

    x_n1 = newton_update(x_n1, x_n)
    x[k + 1, :] = x_n1

    t = t + h
    k = k + 1

# %% Postprocessing: plot state evolution
plt.plot(x[:, 0])