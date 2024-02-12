

import turtle as t
import random
# from playsound import playsound
def rect(x, y, border="#000000", fill="#ffffff"):

    t.color(border)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.color(fill)
    t.end_fill()
    t.penup()


def drawBoard():

    t.clear()

    # board background
    t.goto(-350, -350)
    t.pensize(1)
    rect(700, 600, "#464646", "#929292")

    # board holes
    for i in range(6):
        t.goto(-300, 200 - (100*i))
        for j in range(7):
            t.color("#464646")
            t.dot(82)
            t.color("#ffffff")
            t.dot(80)
            t.forward(100)

    # text lables
    t.color("#000000")
    t.goto(-311, 275)
    t.write("1", font=('Arial', 30, 'normal'))
    t.goto(-211, 275)
    t.write("2", font=('Arial', 30, 'normal'))
    t.goto(-111, 275)
    t.write("3", font=('Arial', 30, 'normal'))
    t.goto(-11, 275)
    t.write("4", font=('Arial', 30, 'normal'))
    t.goto(89, 275)
    t.write("5", font=('Arial', 30, 'normal'))
    t.goto(189, 275)
    t.write("6", font=('Arial', 30, 'normal'))
    t.goto(289, 275)
    t.write("7", font=('Arial', 30, 'normal'))


def initialize():
    global movable
    global position
    global board
    global color
    t.penup()
    t.speed(0)
    drawBoard()

    color = 'Red'
    board = [[0 for j in range(6)] for i in range(7)]
    t.speed(5)
    t.goto(0, 300)
    t.setheading(270)
    t.shape("circle")
    t.color(color)
    t.resizemode("user")
    t.turtlesize(3, 3)
    position = 3
    movable = True
    t.showturtle()
    t.goto(0, 340)
    t.write("Connect four to win! Press column number on keyboard to place where you want!", align = "center", font=('Arial', 14, 'normal'))
    t.goto(0, 300)
    t.listen()


def saveGame(winner):
    global board, games
    games += winner + " wins!\n"
    for i in range(6):
        for j in range(7):
            games += str(board[j][i])[0] + " "
        games += "\n"
    games += "\n"


def chipsInColumn(col):
    '''Outputs the number of chips in the column selected'''
    global board
    count = 6
    for i in range(6):
        if board[col][i] != 0:
            return count
        count -= 1
    return count

def placeChip(x, y):
    board[x][y] = color
    #playsound(u"Clink.mp3")
    t.dot(60, color)

def checkVertical():
    global board
    for i in range(7):
        for j in range(6):
            try:
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != 0:
                    t.pensize(30)
                    t.hideturtle()
                    t.goto(-300 + i*100, 200 - j*100)
                    t.pendown()
                    t.goto(-300 + i*100, 200 - (j+3)*100)
                    t.penup()
                    return board[i][j]
            except:
                continue
    return "none"
    
def checkHorizontal():
    global board
    for i in range(7):
        for j in range(6):
            try:
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != 0:
                    t.pensize(30)
                    t.hideturtle()
                    t.goto(-300 + i*100, 200 - j*100)
                    t.pendown()
                    t.goto(-300 + (i+3)*100, 200 - j*100)
                    t.penup()
                    return board[i][j]
            except:
                continue
    return "none"

def checkUpDiagonal():
    global board
    for i in range(7):
        for j in range(6):
            try:
                if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] != 0:
                    t.pensize(30)
                    t.hideturtle()
                    t.goto(-300 + i*100, 200 - j*100)
                    t.pendown()
                    t.goto(-300 + (i+3)*100, 200 - (j-3)*100)
                    t.penup()
                    return board[i][j]
            except:
                continue
    return "none"

def checkDownDiagonal():
    global board
    for i in range(7):
        for j in range(6):
            try:
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != 0:
                    t.pensize(30)
                    t.hideturtle()
                    t.goto(-300 + i*100, 200 - j*100)
                    t.pendown()
                    t.goto(-300 + (i+3)*100, 200 - (j+3)*100)
                    t.penup()
                    return board[i][j]
            except:
                continue
    return "none"

def checkWin():
    winner = checkVertical()
    if winner != "none":
        return winner
    winner = checkHorizontal()
    if winner != "none":
        return winner
    winner = checkUpDiagonal()
    if winner != "none":
        return winner
    winner = checkDownDiagonal()
    return winner

def win(winner):
    global playAgain, games
    t.goto(0, 330)
    t.color("black")
    t.write(winner + " wins!", align = "center", font=('Arial', 40, 'normal'))
    saveGame(winner)
    play = 0
    while play != "y" and play != "n":
        play = t.textinput(winner + " wins!", "Play Again? (y/n)").lower()
    if play == "y":
        initialize()
    else:
        t.textinput("", "Saving games to last_game.txt, click OK to continue")
        result = open("last_game.txt", "w")
        result.write(games)
        result.close()
        t.bye()
    

def tick():
    global movable, color
    
    chips = chipsInColumn(position)
    if chips >= 6:
        movable = True
    

    t.forward(100 * (6-chips))
    placeChip(position, 5-chips)
    

    winner = checkWin()
    if winner != "none":
        print(winner, "wins!")
        win(winner)
        return
    

    t.backward(100 * (6-chips))
    
    if color == 'Red':
        color = 'Yellow'
    else:
        color = 'Red'
    t.color(color)
    movable = True
    
def one():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(-300, 300)
    position = 0
    tick()

def two():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(-200, 300)
    position = 1
    tick()

def three():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(-100, 300)
    position = 2
    tick()

def four():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(0, 300)
    position = 3
    tick()

def five():
    global movable, position, color
    if not movable:
        return
    # disable movement
    movable = False
    t.goto(100, 300)
    position = 4
    tick()

def six():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(200, 300)
    position = 5
    tick()

def seven():
    global movable, position, color
    if not movable:
        return

    movable = False
    t.goto(300, 300)
    position = 6
    tick()

global games
games = ""
t.setup(800,800)
t.Screen()
t.listen()
initialize()
t.onkey(one, "1")
t.onkey(two, "2")
t.onkey(three, "3")
t.onkey(four, "4")
t.onkey(five, "5")
t.onkey(six, "6")
t.onkey(seven, "7")

t.exitonclick()