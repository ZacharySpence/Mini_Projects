import collections
from collections import Counter
#Test case
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]


#Sub-routines
#Creating flipped puzzle (rows become columns, columns rows)
def swapIt(nlisty):
    swapped_listy=[[],[],[],[],[],[],[],[],[]]
    for i in nlisty:
        for j in range(len(i)):
            swapped_listy[j].append(i[j])
    return swapped_listy


#Create the squares:
def createSquares(alpha_puzzle):
    broken1 = [i[0:3] for i in alpha_puzzle] #broken into 3's
    broken2 = [i[3:6] for i in alpha_puzzle]
    broken3 = [i[6:9] for i in alpha_puzzle]
    all_squares=[]
    broken1.extend(broken2)
    broken1.extend(broken3)
    for i in range(0,27,3):
        square=[]
        for j in range(0,3):
            square.extend(broken1[j+i])
        all_squares.append(square)
    return all_squares

#get square
def getSquare(j,i,allSquare):
    match j:
        case _ if j<3:
            match i:
                case _ if i<3:check=all_squares[0]
                case _ if i<6:check=all_squares[1]
                case _ if i<9:check=all_squares[2]
        case _ if j<6:
            match i:
                case _ if i<3:check=all_squares[3]
                case _ if i<6:check=all_squares[4]
                case _ if i<9:check=all_squares[5]
        case _ if i<9:
            match i:
                case _ if i<3:check=all_squares[6]
                case _ if i<6:check=all_squares[7]
                case _ if i<9:check=all_squares[8]
    return check

#Convert to string values (using counters as solution self-challenge)
alphabet="0123456789"
alpha_puzzle =[list(map(lambda x:alphabet[x],pz))for pz in puzzle]
y_alpha_puzzle = swapIt(alpha_puzzle)
#Create a 2nd puzzle with y-axis lists

                

#find the correct axis

#make 18 counters
    #full counter
full = ['1','2','3','4','5','6','7','8','9']
full = Counter(full)

while sum(x.count("0") for x in alpha_puzzle):
    for i in range(9):
        x = Counter(alpha_puzzle[i])
        #generating possible choices to put in an 'empty' spot
        for j in range(9): 
            if alpha_puzzle[i][j] == "0":
                y = Counter(y_alpha_puzzle[j])
                all_squares = createSquares(alpha_puzzle)
                check = Counter(getSquare(j,i,all_squares))
                insct =full-x-y-check #gives counter of all numbers not in the Row, Column or in its Square.
    #putting in correct number
                if len(insct)==1: #determinative choice (only 1)
                #i and j are just the correct column/row)
                    alpha_puzzle[i][j] = str(list(insct.keys())[0])
                    y_alpha_puzzle[j][i] = str(list(insct.keys())[0])



#print alpha_puzzle out nicely
for i in range(9):
    stringy=""
    for j in range(9):
        stringy+=alpha_puzzle[i][j]
    print(stringy)

#Turn back into list of numbers
puzzle =[list(map(lambda x:int(x),pz))for pz in alpha_puzzle]

        


