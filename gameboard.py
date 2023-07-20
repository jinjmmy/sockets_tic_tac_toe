class BoardClass:
    """A class to keep track of the board game and player statistics.

    Attributes:
        playerName (str): Player's username.
        lastPlayer (str): The username of the last player who moved a piece.
        p1wins (int): The number of times player 1 has won.
        p2wins(int): The number of times player 2 has won.
        p1loss (int): The number of times player 1 has lost.
        p2loss (int): The number of times player 2 has lost.
        ties (int): The number of times the player has tied.
        gameBoard (list of lists): The tic-tac-toe board.
        gamesPlayed (int): The number of games played.
        """

    def __init__(self):
        self.gameBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.playerName = ''
        self.p1wins = 0
        self.p2wins = 0
        self.p1loss = 0
        self.p2loss = 0
        self.ties = 0
        self.lastPlayer = ''
        self.player2name = ''



    def setPlayer2name(self, player2):
        """Sets player 2 name."""
        self.player2name = player2
        print(self.player2name)

    def getPlayer2name(self):
        """Retrieves player 2 name.

        Returns:
            player2name: (str)."""

        return self.player2name


    def setPlayer1name(self, player1):
        """Sets player 1 name."""
        self.playerName = player1


    def getPlayer1name(self):
        """Retrieves player 1 name.

        Returns:
            playerName: (str)."""

        return self.playerName

    def setLastPlayer(self, player):
        self.lastPlayer = player


    def updateGamesPlayed(self)-> int:
        """Adds number of wins, losses, and ties.

        Returns:
            gamesPlayed: (int).
            """
        self.gamesPlayed = self.p1wins + self.p1loss + self.ties
        return self.gamesPlayed


    def resetGameBoard(self):
        """Replaces old game board with new, empty game board."""
        self.gameBoard = [
                        [' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']
                        ]
        return self.gameBoard

    def updateGameBoard(self, position: int, symbol):
        """Takes an integer from 0-8 and places player marker in that position.
        [[0,1,2]
        [3,4,5]
        [6,7,8]]
        """

        row = int(position) // 3
        col = int(position) % 3
        if self.gameBoard[row][col] == ' ':
            self.gameBoard[row][col] = symbol


    def isWinner(self):
        """Checks if the most recent move resulted in a win and updates the win count.

        Returns:
            True if game is won and False if not."""
        #check horizontal wins
        for row in self.gameBoard:
            if row[0] == row[1] == row[2] == 'X':
                self.p1wins += 1
                self.p2loss += 1
                print()
                self.printBoard()
                self.resetGameBoard()
                return True
            if row[0] == row[1] == row[2] == 'O':
                self.p2wins += 1
                self.p1loss += 1
                print()
                self.printBoard()
                self.resetGameBoard()
                print(self.lastPlayer)
                return True
        #check vertical wins
        for col in range(3):
            if 'X' == self.gameBoard[0][col] == self.gameBoard[1][col] == self.gameBoard[2][col]:
                self.p1wins += 1
                self.p2loss += 1
                print()
                self.printBoard()
                self.resetGameBoard()
                return True
            if 'O' == self.gameBoard[0][col] == self.gameBoard[1][col] == self.gameBoard[2][col]:
                self.p2wins += 1
                self.p1loss += 1
                print()
                self.printBoard()
                self.resetGameBoard()
                return True
        #check diagonals
        if (self.gameBoard[0][0] == self.gameBoard[1][1] == self.gameBoard[2][2] == 'X') or (self.gameBoard[0][2] == self.gameBoard[1][1] == self.gameBoard[2][0] == 'X'):
            self.p1wins += 1
            self.p2loss += 1
            print()
            self.printBoard()
            self.resetGameBoard()
            return True
        if (self.gameBoard[0][0] == self.gameBoard[1][1] == self.gameBoard[2][2] == 'O') or (self.gameBoard[0][2] == self.gameBoard[1][1] == self.gameBoard[2][0] == 'O'):
            self.p2wins += 1
            self.p1loss += 1
            print()
            self.printBoard()
            self.resetGameBoard()
            return True
        else:
            return False



    def boardIsFull(self) -> bool:
        """Checks if board is full.

        Returns:
            True or False."""

        count = 0
        if self.isWinner() is False:
            for row in range(len(self.gameBoard)):
                for col in range(len(self.gameBoard[row])):
                    if self.gameBoard[row][col] != ' ':
                        count += 1
                        if count == 9:
                            self.ties += 1
                            self.printBoard()
                            self.resetGameBoard()
                            print('Game over: Tie')
                            return True
                    else:
                        return False


    def printBoard(self):
        """Prints the nested lists that make up the game board in new lines for readability."""

        for row in self.gameBoard:
            print(row)


    def computStats(self):
        """Computes the losses, wins, player names, and ties."""
        return self.playerName, self.player2name, self.p1loss,self.p2loss, self.p1wins, self.p2wins, self.ties, self.gamesPlayed
