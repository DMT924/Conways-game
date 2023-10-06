import tkinter as tk
class GameOfLife:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.grid = [[0] * 40 for _ in range(30)]  # Example grid, replace with actual grid initialization
    def update_grid(self):
        new_grid = [[0] * len(self.grid[0]) for _ in range(len(self.grid))]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 1
        self.grid = new_grid
        self.draw_grid()
    def count_live_neighbors(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0]):
                    if i != row or j != col:
                        count += self.grid[i][j]
        return count
    def draw_grid(self):
        self.canvas.delete("all")
        cell_width = self.canvas.winfo_width() / len(self.grid[0])
        cell_height = self.canvas.winfo_height() / len(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    x1 = j * cell_width
                    y1 = i * cell_height
                    x2 = (j + 1) * cell_width
                    y2 = (i + 1) * cell_height
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    def handle_click(self, event):
        cell_width = self.canvas.winfo_width() / len(self.grid[0])
        cell_height = self.canvas.winfo_height() / len(self.grid)
        col = int(event.x // cell_width)
        row = int(event.y // cell_height)
        self.grid[row][col] = 1 - self.grid[row][col]
        self.draw_grid()