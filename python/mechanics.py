import numpy as np


class System:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # mass, gravity, length, E_matrix, J_matrix

    def get_z_vector(self, state):
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
        return np.array([self.mass * self.gravity * self.length * np.sin(q), v])

    def get_Jacobian(self, state):
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
        return np.diag([self.mass * self.gravity * self.length * np.cos(q), 1])


class Solver:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # system, timestepsize, newton_epsilon, integrator

    def compute(self, state_n1, state_n, integrator):
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
            z_n = self.system.get_z_vector(state_n)
            residual = (
                self.system.E_matrix @ (state_n1 - state_n)
                - self.timestepsize * self.system.J_matrix @ z_n
            )
            tangent = self.system.E_matrix

        elif integrator == "IE":
            # implicit Euler, evaluates z at t_n1
            z_n1 = self.system.get_z_vector(state_n1)
            dzn1_dxn1 = self.system.get_Jacobian(state_n1)
            residual = (
                self.system.E_matrix @ (state_n1 - state_n)
                - self.timestepsize * self.system.J_matrix @ z_n1
            )
            tangent = (
                self.system.E_matrix
                - self.timestepsize * self.system.J_matrix @ dzn1_dxn1
            )

        elif integrator == "MP":
            # Midpoint rule, evaluates z at t_n05
            state_n05 = 0.5 * (state_n + state_n1)
            z_n05 = self.system.get_z_vector(state_n05)
            dzn05_dxn1 = 0.5 * self.system.get_Jacobian(state_n1)
            residual = (
                self.system.E_matrix @ (state_n1 - state_n)
                - self.timestepsize * self.system.J_matrix @ z_n05
            )
            tangent = (
                self.system.E_matrix
                - self.timestepsize * self.system.J_matrix @ dzn05_dxn1
            )

        return residual, tangent

    def newton_update(self, state_n1, state_n):
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
        while residual_norm >= self.newton_epsilon:
            residual, tangent_matrix = self.compute(state_n1, state_n, self.integrator)
            state_delta = -np.linalg.inv(tangent_matrix) @ residual
            state_n1 = state_n1 + state_delta
            residual_norm = np.linalg.norm(residual)
        return state_n1