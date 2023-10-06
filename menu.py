import tkinter as tk
from tkinter import filedialog
class Menu:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.setup_button = tk.Button(self.frame, text="Setup Layout", command=self.setup_layout)
        self.setup_button.pack()
        self.save_button = tk.Button(self.frame, text="Save Layout", command=self.save_layout)
        self.save_button.pack()
        self.load_button = tk.Button(self.frame, text="Load Layout", command=self.load_layout)
        self.load_button.pack()
        self.end_button = tk.Button(self.frame, text="End Simulation", command=self.end_simulation)
        self.end_button.pack()
    def setup_layout(self):
        # Open a dialog to allow the user to set up the initial layout of the blocks
        self.game.canvas.bind("<Button-1>", self.handle_click)
    def save_layout(self):
        # Save the current layout to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                for row in self.game.grid:
                    file.write("".join(str(cell) for cell in row))
                    file.write("\n")
    def load_layout(self):
        # Load a layout from a file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                lines = file.readlines()
                grid = [[int(cell) for cell in line.strip()] for line in lines]
                self.game.grid = grid
                self.game.draw_grid()
    def end_simulation(self):
        # End the simulation and return to the starting menu
        self.game.canvas.unbind("<Button-1>")
        self.game.grid = [[0] * len(self.game.grid[0]) for _ in range(len(self.game.grid))]
        self.game.draw_grid()
    def handle_click(self, event):
        cell_width = self.game.canvas.winfo_width() / len(self.game.grid[0])
        cell_height = self.game.canvas.winfo_height() / len(self.game.grid)
        col = int(event.x // cell_width)
        row = int(event.y // cell_height)
        self.game.grid[row][col] = 1 - self.game.grid[row][col]
        self.game.draw_grid()