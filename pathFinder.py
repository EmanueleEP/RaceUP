import os

# global vars:

# Folder containing the exercises
folder_path = "mazes/"

# Define the possible moves with their directions
moves = [
    (-1, 0, "UP"),     # Move UP
    (1, 0, "DOWN"),    # Move DOWN
    (0, -1, "LEFT"),   # Move LEFT
    (0, 1, "RIGHT")    # Move RIGHT
]

# Check if .txt files exists in maze folder
def has_txt_files(folder_path):
    # Check if the directory exists
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path '{folder_path}' is not a valid directory.")

    # Check for .txt files in the folder and append them in a list
    txt = False
    txt_list = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            txt_list.append(file_name)
            if not txt:
                txt = True
    return txt, txt_list


# Print matrices in list
def printMatrices(exampleMatrices):
    for matrix in exampleMatrices:
        print("Matrix:")
        for row in matrix:
            print(row)
        print()  # Blank line


# Create matrices having the list of file names
def listExamples(file_list):
    exampleMatrices = []
    for file_ in file_list:
        temp = []
        with open(file_, 'r') as file:
            # Read each line from the file and strip newline characters
            temp = [list(line.strip()) for line in file]
            # If temp exists remove the first row (the one that indicates the maze number )
            if temp:
                temp = temp[1:]
            exampleMatrices.append(temp)
    # Uncomment next line to print examples in mazes folder
    printMatrices(exampleMatrices)
    return exampleMatrices


# Search starting position
def startPosMaze(mazeMatrix):
    # Search for the 'S' character in the maze
    for row in range(len(mazeMatrix)):
        for col in range(len(mazeMatrix[row])):
            if mazeMatrix[row][col] == 'S':
                return row, col  # Return the position immediately upon finding 'S'
    
    raise ValueError("Start position 'S' not found in the maze.")  # Return Error if 'S' is not found


# Return last move done
def lastMoveDirection(row, col, prevRow, prevCol):
    # Calculate the difference in positions
    diffRow = row - prevRow
    diffCol = col - prevCol

    # Iterate through the moves to find the direction
    for rowOffset, colOffset, moveName in moves: # moves is a global var.
        if diffRow == rowOffset and diffCol == colOffset:
            return moveName

    return "UNKNOWN MOVE"  # In case of an unexpected case


# Search recursively for the solution
def recursiveSearch(rowPos, colPos, mazeMatrix, prevRowPos=None, prevColPos=None):
    symbol = mazeMatrix[rowPos][colPos]

    # Base case: Exit found
    if symbol == 'E':
        return True, ""

    # Iterate over each possible move
    for rowOffset, colOffset, moveName in moves:
        newRow, newCol = rowPos + rowOffset, colPos + colOffset

        # Check that the new position is within bounds and not the previous cell
        if (0 <= newRow < len(mazeMatrix) and 0 <= newCol < len(mazeMatrix[0])
                and (newRow != prevRowPos or newCol != prevColPos)
                and mazeMatrix[newRow][newCol] != '#'):
            
            # Recursive call to search in the new position
            found, direction = recursiveSearch(newRow, newCol, mazeMatrix, rowPos, colPos)
            if found:
                tempList = lastMoveDirection(newRow, newCol, rowPos, colPos)
                tempList += " " + direction
                return found, tempList

    # No moves available, exit not found
    return False, "No exit found :("



def main():
    
    file_list = []
    
    # Check if exists at least one .txt file in 'maze/' folder
    try:
        result, file_list = has_txt_files(folder_path)
        if result:
            print(file_list)
        else:
            raise ValueError(f"No .txt file found in '{folder_path}' directory.")
    except ValueError as e:
        print(e)

    # Add the folder path to each string in file_list
    file_list = [folder_path + string for string in file_list]

    # Create a list of matrices containing all the exercises
    matrices = listExamples(file_list)

    # Solution for all mazes in list
    for i in range(len(matrices)):

        print(f"Exercise {i+1}: ")
        
        # Handle no starting pos error
        try:
            # Find cell containing char 'S'
            r, c = startPosMaze(matrices[i])
            print(f"Starting position: row={r}, col={c}")
            # Recursively search for solution
            print(recursiveSearch(r,c, matrices[i])[1])
        except ValueError as e:
            print(e)  
        
        print()



if __name__ == "__main__":
    main()