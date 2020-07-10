import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy


def make_board():
  # I wish also to show en-passant status, this will be done by an extra row at the
  # top and bottom of the board. This is for the sake of the board state being a
  # complete description, without the need to reference previous board states.

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

           'blue': ((0, 0.2, 0.2),
                   (1, 0.6, 0.6))}

  board_color_map = LinearSegmentedColormap('board_color_map', cdict)
  plt.register_cmap(cmap=board_color_map)

  fig, axes = plt.subplots(3, 1, gridspec_kw={'height_ratios': [1, 8, 1]})

  axes[0].imshow([[1, ] * 8], vmin=0, vmax=1, cmap=board_color_map)
  axes[0].set_xticklabels(['', ] * 8)
  axes[0].set_yticklabels([''])
  axes[0].tick_params(axis=u'both', which=u'both',length=0)


  axes[2].imshow([[0, ] * 8], cmap=board_color_map)
  axes[2].set_xticklabels(['', ] * 8)
  axes[2].set_yticklabels([''])
  axes[2].tick_params(axis=u'both', which=u'both',length=0)


  axes[1].imshow(filled, cmap=board_color_map, extent=[-0.5, 7.5, -0.5, 7.5])
  axes[1].set_xticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
  axes[1].set_yticklabels([f'{i}' for i in range(1, 9)])
  axes[1].set_xticks(numpy.linspace(0, 7, 8))
  axes[1].set_yticks(numpy.linspace(0, 7, 8))
  axes[1].tick_params(axis=u'both', which=u'both',length=0)

  board = fig, axes
  return board


def swap_color(color):
  if color == "white":
    return "black"

  if color == "black":
    return "white"


class piece(object):
  def __init__(self, color, locations, name):
    self.color = color
    self.locations = locations
    self.name = name


class pawns(piece):
  def __init__(self, color, locations=False):
    self.color = color
    self.name = self.color + " pawns"
    if locations is not False:
      self.locations = locations
    
    # Set pieces to default location
    else:
      if color == 'white':
        self.locations = numpy.zeros((8, 8))
        self.locations[:, 1] = 1


  def moves(board_config):
    return None

  def plot(self, fig, axes):
    for i in range(8):
      for j in range(8):
        if self.locations[i, j] == 1:
          axes[1].add_artist(plt.Circle([i, j], radius=0.3, zorder=1, color=self.color))
          axes[1].add_artist(plt.Circle([i, j], radius=0.3, zorder=1, color=swap_color(self.color), fill=False, lw=1))


fig, axes = make_board()

white_pawns = pawns('white')

white_pawns.plot(fig, axes)
plt.show()
