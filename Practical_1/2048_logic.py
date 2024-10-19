import numpy as np
import random

def start_game():
    mat = np.zeros((4, 4), dtype=int)
    print("Commands are as follows:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")
    add_new_2(mat)
    return mat

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        mat[r][c] = 2

def get_current_state(mat):
    if 2048 in mat:
        return 'WON'
    if 0 in mat:
        return 'GAME NOT OVER'
    if any(mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j] for i in range(3) for j in range(3)):
        return 'GAME NOT OVER'
    if any(mat[3][j] == mat[3][j+1] for j in range(3)):
        return 'GAME NOT OVER'
    if any(mat[i][3] == mat[i+1][3] for i in range(3)):
        return 'GAME NOT OVER'
    return 'LOST'

def compress(mat):
    new_mat = np.zeros_like(mat)
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    return np.flip(mat, axis=1)

def transpose(mat):
    return np.transpose(mat)

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    return reverse(new_grid), changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    return transpose(new_grid), changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    return transpose(new_grid), changed

if __name__ == '__main__':
    mat = start_game()
    while True:
        x = input("Press the command: ")
        if x.lower() == 'w':
            mat, flag = move_up(mat)
        elif x.lower() == 's':
            mat, flag = move_down(mat)
        elif x.lower() == 'a':
            mat, flag = move_left(mat)
        elif x.lower() == 'd':
            mat, flag = move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue
        
        status = get_current_state(mat)
        print(status)
        
        if status == 'GAME NOT OVER':
            add_new_2(mat)
        else:
            break
        
        print(mat)
