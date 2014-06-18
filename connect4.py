# -*- coding: utf-8 -*-
"""

@author: g_singhal
"""

import random
import copy

def printboard(board):
    print "   1   2   3   4    5   6   7"
    print "1: "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" | "+board[0][3]+" | "+board[0][4]+" | "+board[0][5]+" | "+board[0][6]
    print "  ---+---+---+---+---+---+---"
    print "2: "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" | "+board[1][3]+" | "+board[1][4]+" | "+board[1][5]+" | "+board [1][6]  
    print "  ---+---+---+---+---+---+---+"
    print "3: "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" | "+board[2][3]+" | "+board [2][4]+" | "+board [2][5]+" | "+board [2][6]
    print "  ---+---+---+---+---+---+---+"
    print "4: "+board[3][0]+" | "+board[3][1]+" | "+board[3][2]+" | "+board[3][3]+" | "+board [3][4]+" | "+board [3][5]+" | "+board [3][6]
    print "  ---+---+---+---+---+---+---+"
    print "5: "+board[4][0]+" | "+board[4][1]+" | "+board[4][2]+" | "+board[4][3]+" | "+board [4][4]+" | "+board [4][5]+" | "+board [4][6]
    print "  ---+---+---+---+---+---+---+"
    print "6: "+board[5][0]+" | "+board[5][1]+" | "+board[5][2]+" | "+board[5][3]+" | "+board [5][4]+" | "+board [5][5]+" | "+board [5][6]
    print "  ---+---+---+---+---+---+---+"
    print "7: "+board[6][0]+" | "+board[6][1]+" | "+board[6][2]+" | "+board[6][3]+" | "+board [6][4]+" | "+board [6][5]+" | "+board [6][6]+"\n"
    
def check4win(board):
    #check rows
    for row in range(7):
        for col in range(4):
            if board[row][col]!="":
                if board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]:
                    return board[row][col]
    
    #check columns
    for col in range(7):
        for row in range(4):
            if board[row][col]!="":
                if board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]:
                    return board[row][col]
    
    #check diagonals from top left
    for row in range(4):
        for col in range(4):
            if board[row][col]!="":
                if board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]:
                    return board[row][col]
    
    #check diagonals from top right
    for row in range(4):
        for col in range(3,7):
            if board[row][col]!="":
                if board[row][col]==board[row+1][col-1]==board[row+2][col-2]==board[row+3][col-3]:
                    return board[row][col]
    
    # if no winner
    return ""

def findvalidrow(board,col):
    validrow = -1    
    for row in range(6,-1,-1):
        if board[row][col]=="":
            validrow = row
            break
    return validrow

def playhuman(board):
    inputflag = True    
    while inputflag:
        col = raw_input("Desired column (1-7) for next move: ")
        
        if col.isdigit():
            col = int(col)
            if 1<=col<=7:
                validrow = findvalidrow(board,col-1)
                if validrow>-1:
                    board[validrow][col-1] = "X"                
                    inputflag = False                    
                    break
                else:
                    print "Column filled. Try Again!\n"
            else:
                print "Invalid column #. Try Again!\n"
        else: 
            print "Integer input only. Try Again!\n"

def findvalidmoves(board):
    rows = []
    cols = range(7)    
    for col in cols:
        row = findvalidrow(board,col)
        rows.append(row) 
    
    validmoves = [(i,j) for (i,j) in zip(rows,cols) if i>-1]
    return validmoves
    
def minimax(board,player,depth,maxDepth):
    bestMove = []
    dupboard = copy.deepcopy(board)
    validmoves = findvalidmoves(dupboard)        
    
    if player=="computer":
        bestScore = -999999999
        tile = "O"
        enemy = "human"
    else:
        bestScore =  999999999
        tile = "X"
        enemy = "computer"
    
    if depth==maxDepth:
        score = getScore(dupboard,player)
        return score, None
    
    for move in validmoves:
        row = move[0]
        col = move[1]
        dupboard[row][col] = tile    
        
        score = minimax(dupboard,enemy,depth+1,maxDepth)
        
        if player=="computer":
            if score>bestScore:
                bestScore = score
                bestMove = move
        else: 
            if score<bestScore:
                bestScore = score
                bestMove = move 
    
    return bestScore, bestMove

def getScore(board,player):
    return random.randint(1,100)
        
def playcomputer(board):
    #get valid moves
    validmoves = findvalidmoves(board)
    
    #check/score moves
    bestMove = []
    for move in validmoves:
        row = move[0]
        col = move[1]
        
        board[row][col] = "O"
        if check4win(board)=="O":
            bestMove = move
            break
        else:
            board[row][col] = ""
    
    if bestMove==[]:
        for move in validmoves:
            row = move[0]
            col = move[1]
            board[row][col] = "X"
            if check4win(board)=="X":
                bestMove = move
                board[row][col] = "O"
                break
            else:
                board[row][col] = ""
    
    if bestMove==[]:
        bestScore, bestMove = minimax(board,"computer",0,2)
        row = bestMove[0]
        col = bestMove[1]
        board[row][col] = "O"
        
    print "The computer has chosen row=",str(bestMove[0])," and col=",str(bestMove[1])," \n"

def main():
    #create board
    board = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
    maxmoves = 7*7    
    nummoves = 0    
    
    #choose who plays first
    inputFlag = True
    while inputFlag:
        choice = raw_input("Do you want to play first? (y or n): ")
        choice = choice[0]
        if choice=="y" or choice=="Y":
            playfirst = True
            inputFlag = False
            break
        elif choice=="n" or choice=="N":
            playfirst = False
            inputFlag = False
            break
        else:
            print "Invalid Input. Try Again!\n"
    
    #start gameplay
    nowinordraw = True
    while nowinordraw:
        nummoves+=1
        if nummoves<=maxmoves:
            printboard(board)            
            if nummoves%2==0:
                if playfirst:
                    playcomputer(board)
                else:
                    playhuman(board)
            else:
                if playfirst:
                    playhuman(board)
                else:
                    playcomputer(board)
        else:
            print "All squares filled. Game is a draw! \n"
            nowinordraw = False
            break
        
        #check for winner
        winner = check4win(board)
        if winner=="X":
            print "Congrats You have won! \n"
            nowinordraw = False
            break
        elif winner=="O": 
            print "Sorry, the computer has won :( \n"
            nowinordraw = False
            break
            
if __name__ == '__main__':
    main()                    

