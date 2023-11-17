using Pkg
Pkg.add("PyCall")
using PyCall
np = pyimport("numpy")

vec1 = np.array([1, 2, 3])