import sys # provides functions for interacting with the interpreter, e.g. sys.exit()
import os

class Node():
  def _init_(self,state,parent,action):
    self.state = state
    self.parent = parent 
    self.action = action

class StackFrontier():
  def _inti_(self):
    self.frontier = []
  
  def add(self,node):
    self.frontier.append(node)

  def contains_state (self,state):
    return any(node.state == state for node in self.frontier)

  def empty(self):
    return len(self.frontier) == 0

# LIFO
  def remove(self):
    if self.empty():
      raise Exception("Empty Frontier")
    else:
      node = self.frontier[-1]
      self.frontier = self.frontier[:-1]
      return node #removed element

class QueueFrontier(StackFrontier):
  # FIFO
  def remove(self):
    if self.empty():
      raise Exception("Empty Frontier")
    else:
      node = self.frontier[0]
      self.frontier = self.frontier[1:0]
      return node

class Maze():
  def __init__(self, filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as f:
      contents = f.read()

    if contents.count("A") != 1:
      raise Exception("Maze must have exactly one start point ")
    if contents.count("B") != 1:
      raise Exception("Maze must have exactly one goal")

    # determine height and width of maze
    contents = contents.splitlines() # splitlines() returns a list of lines in the string
    self.height = len(contents)
    self.width = max(len(line) for line in contents)

    # keep track of walls
    self.walls = []
    # i is column, j is row
    for i in range(self.height):
      row = []
      for j in range(self.width):
        try:
          if contents[i][j] == "A":
            self.start = (i,j)
            row.append(False)
          elif contents[i][j] == "B":
            self.goal = (i,j)
            row.append(False)
          elif contents[i][j] == " ":
            row.append(False)
          else:
            row.append(True)
        except IndexError:
          row.append(False)
      self.walls.append(row)
      # print(self.walls)
    self.solution = None 

  def display(self):
      solution = self.solution[1] if self.solution is not None else None
      print()
      for i, row in enumerate(self.walls):
          for j, col in enumerate(row):
              if col:
                  print("█", end="")
              elif (i, j) == self.start:
                  print("A", end="")
              elif (i, j) == self.goal:
                  print("B", end="")
              elif solution is not None and (i, j) in solution:
                  print("*", end="")
              else:
                  print(" ", end="")
          print()
      print()
  def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result




maze = Maze("maze1.txt")
