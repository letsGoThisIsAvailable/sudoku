a# made by shimmy zalesch started ~2025-2-1
#returns a sudoku and it's answer

#imports
import random

#declare the current sudoku answer
sudokuAnswer = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]] #generate an empty sudokua

#make an 2d array where each index is a 3x3 box
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

# find all duplicates in an arr
def findConflictsInList(Arr, squareToFindDuplicatesOf):
 conflicts = []
 i = 0
 while i < len(Arr):
   if Arr[i] == Arr[squareToFindDuplicatesOf] and Arr[i] != 0 and Arr[squareToFindDuplicatesOf] != 0 and squareToFindDuplicatesOf != i: #squareToFindDuplicatesOf != 0 to make sure squares don't flag themselves as conflicts
     conflicts.append(i)
   i+=1
 return conflicts

#find all duplicates in rows, columns, and boxes
def conflictingSquares(Arr, squareCoordinates):

 boxX = squareCoordinates[0]//3 # squares over from left
 boxY = squareCoordinates[1]//3 # boxes vertical over from top

 conflicts = [] #array with coordinates of conflicting squares

 box = makeArrayOfBoxes([boxX, boxY])
 row = Arr[squareCoordinates[0]]
 column = []
 i=0
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
   conflicts.append([issuesInColumn[i], squareCoordinates[1]])
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

# checks if any conflicts (similar to findConflictsInList but I think faster and boolean output
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

#deletes all duplacates in an arr
def removeDuplicates(arr):
 i=0
 while i<len(arr):
   if len(arr) > 0:
     j=1
     while j<len(arr):
       if arr[i] == arr[j] and i != j:
         arr.pop(j)
       else:
         j+=1 #only go to next index if current index stayed since the new value moves into index just looked at (if that mkes sense)
   i+=1
 return arr

#checks if a square is in other places in an array
def isAConflict(arr, indexToCheck):
 i = 0 
 while i < len(arr) - 1:
   if arr[i] == arr[indexToCheck]:
     return True
   i += 1
 return False

#removes all blank indexes in a 3d array
def removeBlanks3D(arr):
 #remove blank indexes
 i = 0
 while i < len(arr):
   j = 0
   while j < len(arr[i]):
     if arr[i][j]==[]:
       arr[i].pop(j)
       j-=1
     j+=1
   i+=1
 return arr

#removes all blank indexes in a 2d array (can also delete all blank arrays in a 3d array)
def removeBlanks2D(arr):
 #remove blank indexes
 i = 0
 while i < len(arr):
   if arr[i]==[]:
     arr.pop(i)
     i-=1
   i+=1
 return arr

#adds a square and makes sure all conflicts are changed to a value that works
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
   
 conflicts = [squareToCheck]

 # loop until sudoku is possible
 issuesInlastGenTiesComplete=[[[0,1]]]
 while len(issuesInlastGenTiesComplete) != 0:
   conflicts = removeDuplicates(conflicts)
   currentValue = sudokuAnswer[conflicts[0][0]][conflicts[0][1]]
   ties = [sudokuAnswer]
   lastRepititionTies = [[[]]]
   
   noIssues = False
   i = 0
   while len(ties) > 1 or i==0:

     ties = removeDuplicates(ties)
     lastRepititionTies = ties
     ties = []

     issuesInlastGenTiesComplete = [[[]]]

     j=0
     while j < len(lastRepititionTies):
       issuesInlastGenTiesComplete.append([[]])
       m = 0
       while m < 81:
         issuesInlastGenTiesComplete[j].append(conflictingSquares(lastRepititionTies[j], [m//9, m%9]))
         m += 1
       j+=1

     issuesInlastGenTiesComplete = removeBlanks3D(issuesInlastGenTiesComplete[0])
     issuesInlastGenTiesComplete = removeBlanks2D(issuesInlastGenTiesComplete)

     j=0
     while j < len(issuesInlastGenTiesComplete):
       issuesInlastGenTiesComplete[j] = removeDuplicates(issuesInlastGenTiesComplete[j])
       j+=1

     j = 0
     while j < len(lastRepititionTies):

       l = 0
       leastSquaresConflicted = []

       k = 0
       while k < 1000:
         leastSquaresConflicted.append(0)
         k+=1

       while l < 8 and len(issuesInlastGenTiesComplete) != 0: #find the current best candidate(s)'s isues left
        
         issuesInlastGenTies = issuesInlastGenTiesComplete[j]

         tiesToImproove = lastRepititionTies[j]
                
         squaresToTry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
         squaresToTry.pop(tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]-1)

         tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]=squaresToTry[l]
         if len(conflictingSquares(tiesToImproove, issuesInlastGenTies[0])) < len(leastSquaresConflicted):
           leastSquaresConflicted = conflictingSquares(tiesToImproove, issuesInlastGenTies[0])
         l+=1
       j+=1

     k=0
     while k < len(ties): 

       if len(ties) < 2: #check if prosess should halt since no more conflicts
         noIssues = True
         sudokuAnswer = lastRepititionTies[0]
         return()
      
       else:

         tieToImproove = lastRepititionTies[j]

         squaresToTry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
         squaresToTry.pop(tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]-1) # make sure code doesn’t keep the number the same
        
         l = 0
         while l < 8: # find all the sudokus that are still deacent enough to keep seeing if best candidate

           tiesToImproove[issuesInlastGenTies[0][0]][issuesInlastGenTies[0][1]]=squaresToTry[l]

           if len(conflictingSquares(tiesToImproove, issuesInlastGenTies[0])) < len(leastSquaresConflicted):
             ties.append(tiesToImproove)
           l +=1
         i+=1
     
     ties = removeBlanks3D(ties)
     ties = removeBlanks2D(ties)
     ties = removeDuplicates(ties)
     
     conflicts = [[]]
     if len(conflicts) > 0 and len(ties)>0:
       l=0
       while l < 81:
         conflicts.append(conflictingSquares(ties[0], [l//9, l%9]))
         l += 1
       sudokuAnswer = ties[0] 

     else:
       return()

#makes a filled out sudoku
def makeOneSudoku():
 row = 0
 while row < 9:
   column = 0
   while column< 9:
     addSquare([row, column])
     column += 1
   row += 1

#makes any amount of filled out sudokus
def makeManySudokus(amount):
  sudokus=[[[]]]
  i=0
  while i<amount:
    sudokus.append(makeOneSudoku())
    i+=1
  return sudokus
