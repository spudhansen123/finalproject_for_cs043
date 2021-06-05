# Tic Tac Toe

import random

class TicTacToe():

    def __init__(self):
        self.board = [' '] * 10
    
    def drawBoard(self):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def inputPlayerLetter(self, player):
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does the ' + player + ' want to be X or O?')
            letter = input().upper()
        return letter

    def whoGoesFirst(self):
    # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'first player'
        else:
            return 'second player'

    def playAgain(self):
    # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you guys want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal

    def isSpaceFree(self, move):
    # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove(self):
    # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self):
    # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


print('Welcome to Tic Tac Toe! This is a game for two players.')
print('What is the first player\'s name?')
nameOne = input()
print('What is the second player\'s name?')
nameTwo = input()

while True:
    # Reset the board
    cur_board = TicTacToe()
    turn = cur_board.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    c1 = cur_board.inputPlayerLetter(turn)
    if c1=='X':
        c2 = 'O'
    else:
        c2 = 'X'
    if turn=='first player':
        playerOneLetter = c1
        playerTwoLetter = c2
    else:
        playerOneLetter = c2
        playerTwoLetter = c1
    gameIsPlaying = True

    while gameIsPlaying:
        # a player's turn.
        print('It is the ' + turn + '\'s turn.')
        cur_board.drawBoard()
        move = cur_board.getPlayerMove()
        if turn=='first player':
            le = playerOneLetter
        else:
            le = playerTwoLetter
        cur_board.makeMove(le, move)

        if cur_board.isWinner(le):
            cur_board.drawBoard()
            print('Hooray! The ' + turn + ' has won the game!')
            gameIsPlaying = False
        else:
            if cur_board.isBoardFull():
                cur_board.drawBoard()
                print('The game is a tie!')
                break
            else:
                if turn=='first player':
                    turn = 'second player'
                else:
                    turn = 'first player'

    if not cur_board.playAgain():
        break
