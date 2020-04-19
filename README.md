# Nonogram solver
In this project I'm trying to write an automated nonogram solution system


upd:With this program you can solve any nonogram (if it has only one solution).
This program will output the solution and save it.
upd2: Also u can open your matrix with values for solution, and save your work on mid solution for in order to return to him at another time.


I am using an existing algorithm to solve:
1. Start with a create zero-matrix. 0 = unknown, 1 = off, 2 = on
2. For each row, generate all possible permutations
3. If a value is equal to "off 'for every permutation then set the row's cell to off. And vice versa. Otherwise it is still unknown.
4. Do the same for every column.
5. Repeat 2-4 until no more changes are possible.

In future i will try create: 
- user friendly graphical interface (completed)
- functions for creating your own nanograms which using your images.
