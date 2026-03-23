# Simple Otto Cycle Simulation

import numpy as np
import matplotlib.pyplot as plt

# basic values
gamma = 1.4
r = 6
r = 10
r = 12

P1 = 101325
V1 = 1

# compression
V2 = V1 / r
P2 = P1 * (V1 / V2) ** gamma

# heat addition (assume pressure increase)
P3 = P2 * 2
V3 = V2

# expansion
V4 = V1
P4 = P3 * (V3 / V4) ** gamma

# efficiency
efficiency = 1 - (1 / (r ** (gamma - 1)))
print("Efficiency:", efficiency)

# plotting

# compression curve
V_comp = np.linspace(V1, V2, 50)
P_comp = P1 * (V1 / V_comp) ** gamma

# expansion curve
V_exp = np.linspace(V3, V4, 50)
P_exp = P3 * (V3 / V_exp) ** gamma

# plot graph
plt.plot(V_comp, P_comp)
plt.plot([V2, V3], [P2, P3])  # heat addition
plt.plot(V_exp, P_exp)
plt.plot([V4, V1], [P4, P1])  # heat rejection

plt.xlabel("Volume")
plt.ylabel("Pressure")
plt.title("Otto Cycle")
plt.savefig("otto_cycle.png")
plt.show()