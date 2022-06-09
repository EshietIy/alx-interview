#!/usr/bin/python3
"""
0.Island perimeter
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    
    perimeter = 0
    count = 0
    for x, row in enumerate(grid):
        for y, itm in enumerate(row):
            if itm == 1 :
                if grid[x - 1][y] == 0:
                    perimeter = perimeter + 1
                if grid[x + 1][y] == 0:
                    perimeter = perimeter + 1
                if grid[x][y - 1] == 0:
                    perimeter = perimeter + 1
                if grid[x][y - 1] == 0:
                    perimeter = perimeter + 1
                
    return perimeter
