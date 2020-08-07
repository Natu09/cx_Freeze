import pkg_resources
pkg_resources.require("numpy==1.16.2")  # modified to use specific numpy
import numpy as np 

version = np.__version__
print("Numpy version: ", version)
