# RaceUP
Solution to exercise 1 among those proposed


Description of the program:

The following are the steps I took, in chronological order, to solve the task:
 - The program checks that there are .txt files corresponding to the exercises to be solved within the 'mazes/' folder. If no files are found, an error is raised.
 - The names of the text files are collected into a list.
 - The names in the list are used to generate matrices that represent the contents of each file.
 - For each matrix, a recursive algorithm is executed to determine if it is possible to reach a cell containing the character 'E'. The algorithm follows this checking pattern: Up, Down, Left, Right. In addition, the algorithm checks whether the adjacent cells are free (i.e., do not contain the character '#') and ensures that the next cell to be explored is not the previous cell. If 'E' is found, the moves are passed back through the recursion. If 'E' is unreachable, the function returns a string indicating that the position was not found.


ASSUMPTIONS:

    - There are no cycles in the paths leading to 'E'. Otherwise, the algorithm may enter an infinite loop.
    - Characters '.' along with any other character that is not ('S', 'E', or '#') are considered equivalent (thus representing free passages).


Execute code guide:

To execute the code, navigate to the base directory in the terminal, where the file pathFinder.py is located, and run the command: ```python .\pathFinder.py```
