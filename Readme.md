# Conway's Game of Life

This project is an implementation of **Conway's Game of Life** in Python using **Pygame** and **SciPy's convolution** for efficient calculations. It provides a visualization of the evolution of life on a grid based on simple rules, showcasing how initial configurations evolve over time.

![Demo](/assets/demo.gif)


## What is Conway's Game of Life?

Conway's Game of Life is a **cellular automaton** devised by the British mathematician **John Horton Conway** in 1970. The game consists of a grid of cells, each of which can be **alive** or **dead**. The state of each cell changes over time based on a set of rules that are applied simultaneously to every cell in the grid, with the next generation being a result of the current state. These rules are:

1. **Any live cell with fewer than two live neighbors dies** (underpopulation).
2. **Any live cell with two or three live neighbors lives on to the next generation** (survival).
3. **Any live cell with more than three live neighbors dies** (overpopulation).
4. **Any dead cell with exactly three live neighbors becomes a live cell** (reproduction).

The grid evolves in discrete time steps, with each step called a "generation".

## Features

- **6 Preset Patterns**: 
  - **Spacefiller**
  - **Hammerhead Spaceship**
  - **Gosper Glider Gun**
  - **Pulsar**
  - **Pentadecathlon**
  - **Replicator**
  
- **Zoom Functionality**: Adjust the zoom level for better control over the grid's appearance.
- **Adjustable Grid Size**: Modify the grid size to control performance and accommodate different visualizations.
- **Real-time Evolution**: Watch the grid evolve live as the algorithm runs in real-time.

## Prerequisites

- **Python 3.x**

### Required Libraries

- `pygame`
- `scipy`

To install the required libraries, you can use the following command:

```bash
pip install -r requirements.txt
```

## Documentation

For more information, check out the [Conway's Game of Life Info markdown file](/assets/Conways%20Game%20of%20Life.md)

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.