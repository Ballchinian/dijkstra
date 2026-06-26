# Dijkstra
 
A little pathfinder. Hand it a grid of digits and it works out the cheapest way to walk from the top-left corner to the bottom-right, where the cost of each step is how much the number changes as you move onto the next cell.
 
## How it works
 
It's Dijkstra's algorithm on a grid. Every cell is a node, its neighbours are the cells directly north, east, south, and west, and the weight of moving between two of them is the absolute difference of their values. From the start it keeps the cheapest-known cost to reach each cell, always expands whichever cell is currently cheapest, and stops the moment it reaches the bottom-right — the cost it's holding at that point is the answer. No diagonals, and a step onto an equal number is free.
 
## Input
 
The grid comes in as a string: one row per line, one digit per cell, and the same number of rows as columns.
 
```
010
010
010
```
 
For that grid the answer is **2**. The outer columns are all zeros, so you can run straight down one of them for free; the only cost is crossing the wall of `1`s in the middle, which is `0 → 1 → 0`, and there's no way around paying that once.
 
## Running it
 
It's a single function with no dependencies, so any Python 3 will do.
 
```python
path_finder("010\n010\n010")   # -> 2
```
 
Or run the file directly to see the example print:
 
```
python path_finder.py
```
 
