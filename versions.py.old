#!/usr/bin/env python3

try:
    import numpy as np
except ModuleNotFoundError:
    np = None
    
try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None
    
try:
    import matplotlib as mpl
except ModuleNotFoundError:
    mpl = None
    
try:
    import sklearn
except ModuleNotFoundError:
    sklearn = None

try:
    import scipy
except ModuleNotFoundError:
    scipy = None

try:
    import seaborn
except ModuleNotFoundError:
    seaborn = None

import sys

def helper(name, imp):
    if imp:
        print("%s version: %s from file %s" % (name, imp.__version__, imp.__file__))
    else:
        print("%s not installed" % name)
        

print("Python version:", sys.version.split('\n')[0])
helper("numpy", np)
helper("pandas", pd)
helper("matplotlib", mpl)
helper("scikit-learn", sklearn)
helper("scipy", scipy)
helper("seaborn", seaborn)

