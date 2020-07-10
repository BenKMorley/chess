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


def border_color(color):
  if color == "white":
    return "black"

  if color == "black":
    return "grey"


class piece(object):
  def __init__(self, color, locations, name):
    self.color = color
    self.locations = locations
    self.name = name


class pawn(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " pawn"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    axes[1].add_artist(plt.Circle([self.location[0], self.location[1]], radius=0.3, linewidth=0.3, color=self.color))
    axes[1].add_artist(plt.Circle([self.location[0], self.location[1]], radius=0.3, linewidth=0.3, color=border_color(self.color), fill=False, lw=1))


class rook(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " rook"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    axes[1].add_artist(plt.Rectangle((self.location[0] - 0.3, self.location[1] - 0.3), 0.6, 0.6, linewidth=0.3, color=self.color))
    axes[1].add_artist(plt.Rectangle((self.location[0] - 0.3, self.location[1] - 0.3), 0.6, 0.6, linewidth=0.3, color=border_color(self.color), fill=False, lw=1))


class knight(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " knight"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    shape = [[-0.25, 0.35], [0.25, 0.15], [0.25, -0.35], [-0.25, -0.35]]
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=self.color, linewidth=0.3))
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=border_color(self.color), fill=False, lw=1))


class bishop(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " knight"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    shape = [[0, -0.35], [-0.35, 0], [0, 0.35], [0.35, 0]]
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=self.color, linewidth=0.3))
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=border_color(self.color), fill=False, lw=1))


class queen(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " knight"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    shape = [[-0.25, -0.35], [-0.4, 0.05], [0, 0.35], [0.4, 0.05], [0.25, -0.35]]
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=self.color, linewidth=0.3))
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=border_color(self.color), fill=False, lw=1))


class king(piece):
  def __init__(self, color, location):
    self.color = color
    self.name = self.color + " knight"
    self.location = location

  def move(board_config):
    return None

  def plot(self, fig, axes):
    shape = [[-0.15, -0.4], [-0.15, -0.15], [-0.4, -0.15], [-0.4, 0.15], [-0.15, 0.15], [-0.15, 0.4],
                  [0.15, 0.4], [0.15, 0.15], [0.4, 0.15], [0.4, -0.15], [0.15, -0.15], [0.15, -0.4]]
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=self.color, linewidth=0.3))
    axes[1].add_artist(plt.Polygon(numpy.array([[self.location[0] + k[0], self.location[1] + k[1]] for k in shape]), color=border_color(self.color), fill=False, lw=1))


class pieces(object):
  def __init__(self, color, piece_list=False):
    self.color = color
    if piece_list is not False:
      self.piece_list = piece_list
    
    else:
      # Set pieces to default location
      self.piece_list = []
      
      # Add the pawns
      if self.color == 'white':
        for i in range(8):
          self.piece_list.append(pawn('white', [i, 1]))

      else:
        for i in range(8):
          self.piece_list.append(pawn('black', [i, 6]))

      # Add the rooks
      if self.color == 'white':
        self.piece_list.append(rook('white', [0, 0]))
        self.piece_list.append(rook('white', [7, 0]))

      else:
        self.piece_list.append(rook('black', [0, 7]))
        self.piece_list.append(rook('black', [7, 7]))

      # Add the knights
      if self.color == 'white':
        self.piece_list.append(knight('white', [1, 0]))
        self.piece_list.append(knight('white', [6, 0]))

      else:
        self.piece_list.append(knight('black', [1, 7]))
        self.piece_list.append(knight('black', [6, 7]))

      # Add the bishops
      if self.color == 'white':
        self.piece_list.append(bishop('white', [2, 0]))
        self.piece_list.append(bishop('white', [5, 0]))

      else:
        self.piece_list.append(bishop('black', [2, 7]))
        self.piece_list.append(bishop('black', [5, 7]))

      # Add the Queen
      if self.color == 'white':
        self.piece_list.append(queen('white', [3, 0]))

      if self.color == 'black':
        self.piece_list.append(queen('black', [3, 7]))

      # Add the King
      if self.color == 'white':
        self.piece_list.append(king('white', [4, 0]))

      if self.color == 'black':
        self.piece_list.append(king('black', [4, 7]))


  def plot(self, fig, axes):
    for piece in self.piece_list:
      piece.plot(fig, axes)

fig, axes = make_board()

white_pieces = pieces('white')
black_pieces = pieces('black')


white_pieces.plot(fig, axes)
black_pieces.plot(fig, axes)


plt.show()
