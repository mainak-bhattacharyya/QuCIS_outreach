import numpy as np

# Almost Equal
from numpy.testing import assert_almost_equal as aae





### Linear Algebra Tools

# Matrices
H = 1/np.sqrt(2)*np.array([[1, 1], [1, -1]])

# Unitary Matrix
Unitary_matrix = lambda theta, phi, lam: np.array([[np.cos(theta/2), -np.exp(1j*lam)*np.sin(theta/2)],
                                       [np.exp(1j*phi)*np.sin(theta/2), np.exp(1j*lam + 1j*phi)*np.cos(theta/2)]])

