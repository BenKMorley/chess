import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy

# Make the empty board
color1 = [220, 220, 220]  # white squares
color2 = [143, 152, 120]  # black squares

filled = numpy.zeros((8, 8))
for i in range(8):
  for j in range(8):
    filled[i, j] = not ((i + j) % 2)

# Define a color dictionary for brown on filled = 0, white on filled = 1
cdict = {'red': ((0, 0.5, 0.5),
                 (1, 0.9, 0.9)),

        'green': ((0, 0.3, 0.3),
                  (1, 0.8, 0.8)),

        'blue' : ((0, 0.2, 0.2),
                 (1, 0.6, 0.6))}

board_color_map = LinearSegmentedColormap('board_color_map', cdict)
plt.register_cmap(cmap=board_color_map)

fig, ax = plt.subplots()

ax.set_xticklabels(['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
ax.set_yticklabels([f'{i}' for i in range(1, 10)][::-1])


ax.imshow(filled, cmap=board_color_map)