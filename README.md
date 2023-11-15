# N - QUEENS AI
Genetic algorithm implemented in python.




The classic 8 queens puzzle, the problem of placing eight chess queens on an 8×8 chessboard so that none of them threatens another.

In this implementation the program finds a solution for placing n queens on a board n x n with the use of Genetic algorithm. The default mutation is set to 50% (which is high), but you have the ability to change it.

Each board is represented as a list, each position represents a column and each item (integer) represents a queens.

For example, [1,3,4,7,4,2,6,5] respesents the following board:

```
x x x x x x x x 
x x x q x x x x 
x x x x x x q x
x x x x x x x q
x x q x q x x x 
x q x x x x x x 
x x x x x q x x 
q x x x x x x x 
```




## In order to run the script :
```bash 
python3 main.py
```

The program will then ask for the number of queens that you like to place (for example if you enter 12, the script will create 12 * 12 boards) and the mutation probability that you would prefer (instead of 50%, someone may enter 0.01 for 1% a mutation to occur).
