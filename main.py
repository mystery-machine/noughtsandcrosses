score_board = [[1, 2, 1],
               [2, 3, 2],
               [1, 2, 1]]

scores = [[[0, 0], [0, 2], [2, 0], [2, 2]],
          [[0, 1], [1, 0], [1, 2], [2, 1]],
          [[1, 1]]]



player = "x"
comp = "o"



#i wrote this whilst listening to "Explosions in the Sky"
#i fully recommend listening to them whilst doing anything

def printBoard(board):
    #function for just printing the board out
    print("  ", end = "")
    for h in range(3):
        print(" " + str(h), end = "")

    print("")
    
    for i in range(3):
        print("  +-+-+-+")
        print(str(i), end = " ")
        for j in range(3):
            print("|" + board[i][j], end = "")
        print("|")

    print("  +-+-+-+")


def playerMove(x, y, board1):
    if board1[y][x] == " ":
        board1[y][x] = player
        return board1
    else:
        return False



def compMove(board, player, comp): #as in, compulsive move, not computer move (though it was that once)
    #now the difficult stuff begins
    move = [None, None]
    

    movene = 0 #move in the northwest
    movenw = 0 #move in the northeast

    countne = 0
    countnw = 0
        
    
    for i in range(3):
        movex = 0 #move in the horizontal
        movey = 0 #move in the vertical
        
        countx = 0
        county = 0

        for j in range(3):

            #- horizontal
            
            if board[i][j] == player:
                movex += j+1
                countx += 1
            elif board[i][j] == comp:
                countx -= 1
                movex += j+1

            #- vertical

            if board[j][i] == player:
                movey += j+1
                county += 1
            elif board[j][i] == comp:
                county -= 1
                movey += j+1
  

        if countx == -2:
            if movex == 4:
                movex = 2
            board[i][(movex%4) - 1] = comp
            return True

        elif county == -2:
            if movey == 4:
                movey = 2
            board[(movey%4) - 1][i] = comp
            return True
            
        elif countx == 2:
            if movex == 4:
                movex = 2
            
            move = [i, (movex%4) - 1]

        elif county == 2:
            if movey == 4:
                movey = 2
            
            move = [(movey%4) - 1, i]

        elif countx == 3 or county == 3:
            
            return "p"

        #diagonal in NE

        if board[i][2-i] == player:
            movene += i+1
            countne += 1
        elif board[i][2 - i] == comp:
            countne -= 1
            movene += i+1

        #diagonal in NW

        if board[i][i] == player:
            movenw += i+1
            countnw += 1
        elif board[i][i] == comp:
            countnw -= 1
            movenw += i+1


    if countne == -2:
        if movene == 4:
            movene = 2
        
        board[(movene%4) -1][3 - (movene%4)] = comp
        return True

    elif countnw == -2:
        if movenw == 4:
            movenw = 2
        
        board[(movenw%4) - 1][(movenw%4) - 1] = comp
        return True
    if countne == 2:
        if movene == 4:
            movene = 2
        
        move = [(movene%4) -1, 3 - (movene%4)]
        

    elif countnw == 2:
        if movenw == 4:
            movenw = 2
        
        move = [(movenw%4) - 1, (movenw%4) - 1]
        

    elif countne == 3 or countnw == 3:
        
        return "p"
    

    try:
        board[move[0]][move[1]] = comp
        return 
    except TypeError:
        return False
    
            
    #literally so many repetitions im going to cry
    #i need to make this more efficient
    #just please ignore how inefficient the above code is! it kills me
def nonCompMove(board, case, turn):

    #NON-COMPULSORY MOVES (i.e. the far more difficult bit)

    coords = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == player:
                coords.append([i, j])


    if turn == 1:
        case = score_board[coords[0][0]][coords[0][1]]
        if case == 1 or case == 2:
            
            move = scores[2][0] #middle
            
            
        elif case == 3:
            move = scores[0][0]

        
        board[move[0]][move[1]] = comp
        return case
    else:
        
        if case == 1:
            for i in range(len(scores[1])):
                if board[scores[1][i][0]][scores[1][i][1]] == " ":
                    move = scores[1][i]
                    board[move[0]][move[1]] = comp
                    return case
            for i in range(len(scores[0])):
                if board[scores[0][i][0]][scores[0][i][1]] == " ":
                    move = scores[0][i]
                    board[move[0]][move[1]] = comp
                    return case
        if case == 3:
            for i in range(len(scores[0])):
                if board[scores[0][i][0]][scores[0][i][1]] == " ":
                    move = scores[0][i]
                    board[move[0]][move[1]] = comp
                    return case
            for i in range(len(scores[1])):
                if board[scores[1][i][0]][scores[1][i][1]] == " ":
                    move = scores[1][i]
                    board[move[0]][move[1]] = comp
                    return case
        if case == 2:
            for i in range(len(scores[1])):
                if board[scores[1][i][0]][scores[1][i][1]] == " ":
                    move = scores[1][i]
                    board[move[0]][move[1]] = comp
                    return case
            for i in range(len(scores[0])):
                if board[scores[0][i][0]][scores[0][i][1]] == " ":
                    move = scores[0][i]
                    board[move[0]][move[1]] = comp
                    return case
            
            
case = 0       
            


test = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

turn = 0

print("""Welcome to NOUGHTS AND CROSSES!

This is a single player game, so you're playing against the computer.
The player automatically start (you're 'x', the computer is 'o').
First, enter the horizontal coordinate of where you want to go, hit enter
and enter the vertical coordinate and hit enter again.

Then hit enter one more time for the computer to move!

Try your best to win!
""")
printBoard(test)


while True:
    turn += 1
    print("")
    while True:
        try:
            playerMove(int(input("Horizontal coordinate: ")), int(input("Vertical coordinate: ")), test)
            break
        except Exception:
            print("ERROR: Please enter your coordinates again! (Correctly this time.)")
            print("")
            
        
    print("")
    print("Player's Move:")
    print("")
    printBoard(test)
    print("")
    input("Hit enter for the computer's move: ")
    print("")
    move = compMove(test, player, comp)
    if move == "p":
        print("Well done, you won! (Insert fancy graphics here.)")
        break
    elif move == True:
        printBoard(test)
        print("The computer won. What a shame.")
        break
        
    elif move == False:
        
        case = nonCompMove(test, case, turn)

    if turn == 5:
        print("Welp, there was no winner. It was a draw!")
        break
    print("Computer's Move:")
    print("")
    printBoard(test)
    
    

