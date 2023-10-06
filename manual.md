# Conway's Game of Life Simulator User Manual

## Introduction

Welcome to the user manual for the Conway's Game of Life Simulator! This software allows you to simulate and visualize the famous cellular automaton known as Conway's Game of Life. With a fully functional GUI, you can easily set up the initial layout of the blocks, scale the GUI, save and load different layouts, and end the simulation at any time.

## Installation

To use the Conway's Game of Life Simulator, you need to have Python installed on your machine. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install tkinter
```

## Usage

To start the Conway's Game of Life Simulator, open a terminal or command prompt and navigate to the directory where you have saved the source code files (`main.py`, `game_of_life.py`, `menu.py`).

Run the following command to start the simulator:

```
python main.py
```

## Main Menu

Upon starting the simulator, you will see the main menu. From here, you can access various functions and settings:

- **Setup Layout**: Click this button to set up the initial layout of the blocks in the simulation. Click on the cells in the grid to toggle their state (alive or dead).

- **Save Layout**: Click this button to save the current layout to a file. You will be prompted to choose a file location and name.

- **Load Layout**: Click this button to load a previously saved layout from a file. You will be prompted to choose a file to load.

- **End Simulation**: Click this button to quickly end the simulation and return to the starting menu. This will reset the grid to its initial state.

## Simulation

After setting up the initial layout or loading a layout from a file, the simulation will start automatically. The cells in the grid will evolve according to the rules of Conway's Game of Life:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

You can observe the evolution of the cells in the GUI. The grid will be updated automatically based on the rules of the game.

## Scaling the GUI

You can scale all aspects of the GUI by dragging the corner of the window. This allows you to adjust the size of the grid and the cells according to your preference.

## Saving and Loading Layouts

You can save and load different layouts through the menu in the GUI. Use the **Save Layout** button to save the current layout to a file. Use the **Load Layout** button to load a previously saved layout from a file. Saved layouts are stored as text files.

## Ending the Simulation

You can quickly end the simulation at any time by clicking the **End Simulation** button. This will return you to the starting menu and reset the grid to its initial state.

## Conclusion

Congratulations! You are now ready to use the Conway's Game of Life Simulator. Have fun exploring the fascinating world of cellular automata and enjoy experimenting with different layouts and settings. If you have any questions or encounter any issues, please refer to the documentation or contact our support team for assistance. Happy simulating!