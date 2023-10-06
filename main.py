import tkinter as tk
from game_of_life import GameOfLife
from menu import Menu
def main():
    root = tk.Tk()
    game = GameOfLife(root)
    menu = Menu(root, game)
    root.mainloop()
if __name__ == "__main__":
    main()