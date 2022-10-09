#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import bdg_loader 



# cropped_scaled_R1_NA_control_lambda.bdg
# R1_control = load_data("cropped_scaled_R1_NA_control_lambda.bdg")
# #cropped_scaled_R1_NA_treat_lambda.bdg
# R1_treat = load_data("cropped_scaled_R1_NA_treat_lambda.bdg")
# # cropped_scaled__R2_NA_control_lambda.bdg
# R2_control = load_data("cropped_scaled__R2_NA_control_lambda.bdg")


# R2_x =
# for each position in the x part of the dictionary, we will split by period, assign the left part as X, the right part as a Y, and plot those values individually

# for x in R2_treat:
#
#     split by "."
#Turn back into integers from the float, then can separate by .
# cropped_scaled__R2_NA_treat_pileup.bdgx
R2_treat = bdg_loader.load_data("cropped_scaled__R2_NA_treat_pileup.bdg")
# print(R2_treat)
# R2_treat = exec(open("bdg_loader.py").read("cropped_scaled__R2_NA_treat_pileup.bdg"))
# This is a dictionary:
R2_x = R2_treat['X']
R2_y = R2_treat['Y']


# cropped_scaled_D0_H3K27ac_treat.bdg
Day0_H3K27ac = bdg_loader.load_data("cropped_scaled_D0_H3K27ac_treat.bdg")
D0_K3K_x = Day0_H3K27ac['X']
D0_K3K_y = Day0_H3K27ac['Y']

# cropped_scaled_D2_H3K27ac_treat.bdg
Day2_H3K27ac = bdg_loader.load_data("cropped_scaled_D2_H3K27ac_treat.bdg")
D2_K3K_x = Day2_H3K27ac['X']
D2_K3K_y = Day2_H3K27ac['Y']

# cropped_scaled_D2_Klf4_treat.bdg
Klf4 = bdg_loader.load_data("cropped_scaled_D2_Klf4_treat.bdg")
Klf4_x = Klf4['X']
Klf4_y = Klf4['Y']



fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, ncols=1)


ax0.bar(R2_x, R2_y, width = 100, color = 'red')
ax0.set_xlabel("Position")
ax0.set_ylabel("Reads")
ax0.set_title("Sox2 R2 treat pileup")

ax1.bar(Klf4_x, Klf4_y, width = 100, color = 'orange')
ax1.set_xlabel("Position")
ax1.set_ylabel("Reads")
ax1.set_title("Klf4")
#
ax2.bar(D0_K3K_x, D0_K3K_y, width = 100, color = 'green')
ax2.set_xlabel("Position")
ax2.set_ylabel("Reads")
ax2.set_title("Day 0 H2K27ax")
#
ax3.bar(D2_K3K_x, D2_K3K_y, width = 100, color = 'blue')
ax3.set_xlabel("Position")
ax3.set_ylabel("Reads")
ax3.set_title("Day 2 H2K27ax")

# plt.tight_layout()
# plt.show()

# plt.savefig("track_figure.png")
# plt.close(fig)

