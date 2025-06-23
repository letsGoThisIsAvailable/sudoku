# made by shimmy zalesch started ~2025-2-1
#returns a sudoku and it's answer

#imports
import random

#declare the current sudoku and it’s answer
sudoku       = [ 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0]]

sudokuAnswer =[
  [0, 1, 2, 3,4, 5, 6, 7, 8], 
  [9, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0], 
  [0, 0, 0, 0,0, 0, 0, 0, 0]]

#declare the current sudoku and it’s answer  

#make a list of the known squares. used for looping through remaining squares
def makeListOfKnownSquares(arr):
  i=0
  coordinatesOfFilledSquares = [[]]
  while i < 9:
    j = 0
    while j < 9:
      if arr[i][j] != 0:
        coordinatesOfFilledSquares.append([i, j])
      j+=1
    i +=1
  return coordinatesOfFilledSquares

#make an 2d array where each index is a box
def makeArrayOfBoxes(BoxCoordsWanted):
  sudokuBoxes = [0,0, 0, 0, 0, 0, 0, 0, 0] 

  boxindex = BoxCoordsWanted[0]*3+BoxCoordsWanted[1]

  # loop through rows and columns within boxes
  k = 0
  while k<3:
    l=0
    while l<3:
      sudokuBoxes[k*3+l] = sudokuAnswer[BoxCoordsWanted[0]*3+k][BoxCoordsWanted[1]*3+l]
      l+=1
    k+=1
  return sudokuBoxes

def findConflictsInList(Arr, squareToFindDuplicatesOf):
  conflicts = []
  i = 0
  while i < len(Arr):
    if Arr[i] == Arr[squareToFindDuplicatesOf] and Arr[i] != 0 and Arr[squareToFindDuplicatesOf] != 0 and squareToFindDuplicatesOf != i: #squareToFindDuplicatesOf != 0 to make sure squares don't flag themselves as conflicts
      conflicts.append(i)
    i+=1
  return conflicts

def conflictingSquares(Arr, squareCoordinates):

  boxX = squareCoordinates[0]//3 # squares over from left
  boxY = squareCoordinates[1]//3 # boxes vertical over from top

  conflicts = [] #array with coordinates of conflicting squares

  box = makeArrayOfBoxes([boxX, boxY])
  row = Arr[squareCoordinates[0]]
  column = []
  i=0
  print(len(Arr), squareCoordinates[1])
  while i<9:
    column.append(Arr[i][squareCoordinates[1]])
    i += 1

  issuesInRow = findConflictsInList(row, squareCoordinates[1])

  i=0
  while i<len(issuesInRow):
    conflicts.append([squareCoordinates[1], issuesInRow[i]])
    i+=1

  issuesInColumn = findConflictsInList(column, squareCoordinates[0])
  i=0
  while i<len(issuesInColumn):
    conflicts.append([[issuesInColumn[i]], squareCoordinates[1]])
    i+=1

  # find where in the box the square is in
  indexSquareIsIn = squareCoordinates[0]%3 *3 + squareCoordinates[1]%3
  issuesInBox = findConflictsInList(box, indexSquareIsIn)

  i=0  
  while i<len(issuesInBox):
    coordsOfSquare = [boxX*3+issuesInBox[i]//3, boxY*3+issuesInBox[i]%3]                                          
    conflicts.append(coordsOfSquare)  
    i+=1

  return conflicts

def isDuplicate(Arr):
  i=0
  while i<len(Arr):
    j=1
    while j<len(Arr)-i: #'-i' is to avoid checking if same as digits before it since those are already checked
      if not(Arr[i] == 0 or Arr[i+j] == 0):
        if Arr[i] == Arr[i+j]:
          return True
      j+=1
    i+=1
  return False

#check if the square is valid 
def checkSquare(attemptedSudoku, squareToCheck):
  if conflictingSquares(attemptedSudoku, squareToCheck) != 0:
    return True
  else:
    return False

def removeDuplicates(arr):
  i=0
  while i<len(arr):
    j=1
    while j<len(arr):
      if arr[i] == arr[j] and i != j:
        arr.pop(j)
      else:
        j+=1
    i+=1
  return arr

def isAConflict(arr, indexToCheck):
  i = 0  
  while i < len(arr) - 1:
    if arr[i] == arr[indexToCheck]:
      return True
    i += 1
  return False

def addSquare(squareToCheck):
  global  sudokuAnswer
  # while True:
  availableNumbersToTry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  random.shuffle(availableNumbersToTry)
  i=0
  numWorks = False
  attemptedSudoku = sudokuAnswer
  while i < 9:
    attemptedSudoku[squareToCheck[0]][squareToCheck[1]] = availableNumbersToTry[i] #add the number to the attempted sudoku
    if len(conflictingSquares(attemptedSudoku, squareToCheck)) == 0: #if there are no conflicts, the number works
      sudokuAnswer = attemptedSudoku
      break
    i+=1

  conflicts = [[squareToCheck[0], squareToCheck[1]]]

  # loop until sudoku is possible
  while len(conflicts) != 0:
    conflicts = removeDuplicates(conflicts)
    currentValue = sudokuAnswer[conflicts[0][0]][conflicts[0][1]]
    ties = [sudokuAnswer]
    lastRepititionTies = [[[]]]

    noIssues = False
    i = 0
    while len(ties) > 1 or i==0:
      ties = removeDuplicates(ties)
      lastRepititionTies = ties
      ties = [[[]]]

      k=0
      while k < len(ties):

        l = 0
        while l < 8: #find the current best candidate(s)'s isues left
          tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]=squaresToTry[l]

          if len(conflictingSquares(tiesToImproove, issuesInlastGenTies[0])) < leastSquaresConflicted:
            leastSquaresConflicted = conflictingSquares(tiesToImproove, issuesInlastGenTies[0])
          l+=1
        
        k+=1

      j=0 
      while j<len(ties):
        k=0
        issuesInlastGenTies = [[]]
        k = 0
        while k < 81:
          issuesInlastGenTies.append(conflictingSquares(lastRepititionTies[j], [k//9, k%9]))
          k+=1
        if len(issuesInlastGenTies) < 2: #check if prosess should halt since no more conflicts
          noIssues = True
          sudokuAnswer = lastRepititionTies[j]
          break
            
        leastSquaresConflicted = 10
        leastConflictingSquare = []

        tieToImproove = lastRepititionTies[j]

        squaresToTry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        squaresToTry.pop(tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]-1) # make sure code doesn’t keep the number the same
        
        l = 0
        while l < 8: # find all the sudokus that are still deacent enough to keep seeing if best candidate

          tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]=squaresToTry[l]

          if len(conflictingSquares(tiesToImproove, issuesInlastGenTies[0])) < leastSquaresConflicted:
            ties.append(tiesToImproove)
          l +=1
        print(ties[0])
        j+=1
      i+=1

    conflicts = [[]]

    k=0
    while k < 81:
      print(k%9, " | ", ties[0])
      conflicts.append(conflictingSquares(ties[0], [k//9, k%9]))
      k+=1
    sudokuAnswer = ties[0]	

def makeSudoku():
  row = 0
  while row < 9:
    column = 0
    while column< 9:
      addSquare([row, column])
      print(sudokuAnswer)
      column += 1
    row += 1

x = addSquare([0,0])
# print(x)
# makeSudoku()
print(sudokuAnswer)