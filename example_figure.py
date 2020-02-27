#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

#import seaborn as sns; sns.set()

plt.rcParams["figure.dpi"]=158 # on laptop this was incorrectly set

fig, ax = plt.subplots(1,2, figsize=(4,2))
a=np.arange(8)
ax[0].plot(a)
ax[0].set_title("First degree")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[1].plot(a**2)
ax[1].set_title("Second degree")
ax[1].set_xlabel("x")
ax[1].set_ylabel("y")
fig.suptitle("Polynomials")
fig.set_tight_layout(True)
plt.subplots_adjust(top=0.95)
if len(sys.argv) == 1:
    plt.show()
else:
    filename = sys.argv[1]
    plt.savefig(filename)
#plt.savefig("example_figure.png")
