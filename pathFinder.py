import os

# global vars
folder_path = "mazes/"



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



def printMatrices(exampleMatrices):
    for matrix in exampleMatrices:
        print("Matrix:")
        for row in matrix:
            print(row)
        print()  # Blank line to separate matrices



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



def startPosMaze(mazeMatrix):
    # Letter S is not necessarily in first row first column
    r = 0
    c = 0
    # Search until S char is found
    continueSearch = True
    for row in range(len(mazeMatrix)):
        for col in range(len(mazeMatrix[r])):
            if mazeMatrix[r][c] == 'S':
                r = row
                c = col
                continueSearch = False
                break
        
        if not continueSearch:
            break
    return r, c



# Return last move done
def lastMoveDirection(row, col, prevRow, prevCol):
    diffRow = row - prevRow
    diffCol = col - prevCol

    if diffRow == -1 and diffCol == 0:
        # current pos is below previous
        return "UP"
    elif diffRow == 1 and diffCol == 0:
        return "DOWN"
    elif diffRow == 0 and diffCol == -1:
        return "LEFT"
    else: 
        return "RIGHT" # (0, 1)



def recursiveSearch(rowPos, colPos, mazeMatrix, prevRowPos = None, prevColPos = None):
    symbol = mazeMatrix[rowPos][colPos]

    if symbol == 'E':
        return True, ""
    
    found = False

    if not (rowPos-1 == prevRowPos and colPos == prevColPos): 
        # check if UP move is available, otherwise same position as previous iteration
        up = mazeMatrix[rowPos - 1][colPos] if ((rowPos - 1) in range(len(mazeMatrix))) else '#'
        if not (up == "#"):
            found, direction = recursiveSearch(rowPos - 1, colPos, mazeMatrix, rowPos, colPos)
            if found:
                tempList = lastMoveDirection(rowPos - 1, colPos, rowPos, colPos)
                tempList += " " + direction
                return found, tempList
    

    if not (rowPos+1 == prevRowPos and colPos == prevColPos) and not found: 
        down = mazeMatrix[rowPos + 1][colPos] if ((rowPos + 1) in range(len(mazeMatrix))) else '#'
        if not (down == "#"):
            found, direction = recursiveSearch(rowPos + 1, colPos, mazeMatrix, rowPos, colPos)
            if found:
                tempList = lastMoveDirection(rowPos + 1, colPos, rowPos, colPos)
                tempList += " " + direction
                return found, tempList


    if not (rowPos == prevRowPos and colPos-1 == prevColPos) and not found: 
        left = mazeMatrix[rowPos][colPos - 1] if ((colPos - 1) in range(len(mazeMatrix[rowPos]))) else '#'
        if not (left == "#"):
            found, direction = recursiveSearch(rowPos, colPos - 1, mazeMatrix, rowPos, colPos)
            if found:
                tempList = lastMoveDirection(rowPos, colPos - 1, rowPos, colPos)
                tempList += " " + direction
                return found, tempList


    if not (rowPos == prevRowPos and colPos+1 == prevColPos) and not found: 
        right = mazeMatrix[rowPos][colPos + 1] if ((colPos + 1) in range(len(mazeMatrix[rowPos]))) else '#'
        if not (right == "#"):
            found, direction = recursiveSearch(rowPos , colPos + 1, mazeMatrix, rowPos, colPos)
            if found:
                tempList = lastMoveDirection(rowPos, colPos + 1, rowPos, colPos)
                tempList += " " + direction
                return found, tempList

    # no moves allowed
    return False, "No exit found :("



def main():
    file_list = []
    
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

    # make for loop for all the exercises
    r, c = startPosMaze(matrices[0])
    print(recursiveSearch(r,c, matrices[0])[1])


if __name__ == "__main__":
    main()