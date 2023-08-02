"""This is client (player 1)."""
import tkinter as tk
from gameboard import BoardClass
from tkinter import font
import socket


class GUI:
    """A class for a user to player Tic tac toe through a graphic user interface for the client side."""
    def __init__(self):
        self.gameBoard = BoardClass()
        self.root = tk.Tk()
        self.root.title('Player 1 (client):Tic-Tac-Toe')
        self.root.geometry('600x600')
        self.tkinterVariables()
        self.getHostInfo()
        self.root.mainloop()
        self.boardSetUp()
        self.root.mainloop()


    def buttonClick(self, button):
        """Updates GUI to show a symbol where the user clicked."""
        if button['text'] == ' ':
            button.config(text='X')
            self.disableButton()
            self.gameBoard.updateGameBoard(self.convertPostion(button), 'X')
            if self.gameBoard.isWinner() or self.gameBoard.boardIsFull():
                button = self.convertPostion(button)
                self.turnLabel.config(text="Game Over")
                self.newSocket.send(str(button).encode())
                self.gameOver()
            else:
                self.sendMove(self.convertPostion(button))
                self.turnLabel.config(text="Their Turn")



    def recieveMove(self):
        """Recieves player 2 moves and updates Tic Tac Toe board."""
        self.player2move = self.newSocket.recv(1024).decode()
        self.gameBoard.updateGameBoard(int(self.player2move), 'O')
        self.gameBoard.setLastPlayer(self.gameBoard.player2name)
        self.turnLabel.config(text='Your Turn')
        self.changeButtons()
        if not self.gameBoard.isWinner() and not self.gameBoard.boardIsFull():
            self.enableButton()
        else:
            self.turnLabel.config(text="Game Over")
            self.root.after(200,self.gameOver)


    def changeButtons(self):
        """Converts player 2 move to the corresponding button on the board."""
        if int(self.player2move) == 0:
            self.b0.config(text='O')
        if int(self.player2move) == 1:
            self.b1.config(text='O')
        if int(self.player2move) == 2:
            self.b2.config(text='O')
        if int(self.player2move) == 3:
            self.b3.config(text='O')
        if int(self.player2move) == 4:
            self.b4.config(text='O')
        if int(self.player2move) == 5:
            self.b5.config(text='O')
        if int(self.player2move) == 6:
            self.b6.config(text='O')
        if int(self.player2move) == 7:
            self.b7.config(text='O')
        if int(self.player2move) == 8:
            self.b8.config(text='O')


    def sendMove(self, position):
        """Sends move to player 2.

        args:
        position (int): numerical position of the button"""
        self.newSocket.send(str(position).encode())
        self.gameBoard.setLastPlayer(self.username.get())
        self.root.after(200, self.recieveMove)



    def tkinterVariables(self):
        """Sets tkinter variables to reference."""
        self.host = tk.StringVar()
        self.port = tk.StringVar()
        self.username = tk.StringVar()
        self.userInp = tk.StringVar()


    def getHostInfo(self):
        """Creates widgets for the user to enter host, port, and username."""
        self.clearWidgets()
        self.hostLabel = tk.Label(self.root, text = "Input host name: ")
        self.hostLabel.grid(row=0, column=0, sticky='E')
        self.hostEntry = tk.Entry(self.root, textvariable = self.host)
        self.hostEntry.grid(row=0, column=1, sticky='N')
        self.portLabel = tk.Label(self.root, text = "Input port number: ")
        self.portLabel.grid(row=1, column=0, sticky='E')
        self.portEntry = tk.Entry(self.root, textvariable = self.port)
        self.portEntry.grid(row=1, column=1, sticky='N')
        self.confirmHostAndPort = tk.Button(self.root, text='Confirm host and port.', command=lambda: self.connectServer())
        self.confirmHostAndPort.grid(row=3)



    def connectServer(self):
        """Tries to connect to the server."""
        self.clearWidgets()
        try:
            self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.HOST = self.host.get()
            self.PORT = int(self.port.get())
            self.newSocket.connect((self.HOST, self.PORT))
            self.userLabel = tk.Label(self.root, text="Enter username: ")
            self.userLabel.grid(row=2, column=0, sticky='E')
            self.userEntry = tk.Entry(self.root, textvariable = self.username)
            self.userEntry.grid(row=2, column=1, sticky='N')
            self.confirmButt = tk.Button(self.root, text='Confirm.', command=lambda: self.sendp1user())
            self.confirmButt.grid(row=3)
        except:
            self.clearWidgets()
            self.userInpLabel = tk.Label(self.root, text="Connection unsuccessful: Try connecting to player 2 again? ")
            self.userInpLabel.grid(row=0,column=0,sticky='E')
            self.tryAgainButton = tk.Button(self.root, text='Yes', command=lambda : self.getHostInfo())
            self.tryAgainButton.grid(row=3,column=0)
            self.exitButton = tk.Button(self.root, text='No', command=lambda : quit())
            self.exitButton.grid(row=3,column=1)
            self.userInpLabel.grid(row=2, column=0, sticky='E')


    def sendp1user(self):
        """Sends player 1 username to player 2."""
        self.newSocket.send(self.username.get().encode())
        player1name = self.username.get()
        self.gameBoard.setPlayer1name(player1name)
        self.root.after(200, self.recievePlayer2user)


    def boardSetUp(self):
        """Sets up a new board."""
        self.clearWidgets()
        self.b0 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b0))
        self.b1 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b1))
        self.b2 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b2))

        self.b3 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b3))
        self.b4 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b4))
        self.b5 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b5))

        self.b6 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b6))
        self.b7 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b7))
        self.b8 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace',command=lambda: self.buttonClick(self.b8))

        self.b0.grid(row=0, column=0)
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)

        self.b3.grid(row=1, column=0)
        self.b4.grid(row=1, column=1)
        self.b5.grid(row=1, column=2)

        self.b6.grid(row=2, column=0)
        self.b7.grid(row=2, column=1)
        self.b8.grid(row=2, column=2)

        self.turnLabel = tk.Label(self.root, text='Your Turn', height=3, width=8)
        self.turnLabel.grid(row=1, column=3)


    def recievePlayer2user(self):
        player2name = self.newSocket.recv(1024).decode()
        self.gameBoard.setPlayer2name(player2name)
        self.gameBoard.setLastPlayer(player2name)
        self.boardSetUp()


    def resetButton(self):
        """Clears the board for a new game.
        """
        self.newSocket.send('again'.encode())
        self.gameBoard.resetGameBoard()
        self.clearWidgets()
        self.b0 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b0))
        self.b1 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b1))
        self.b2 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b2))
        self.b3 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b3))
        self.b4 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b4))
        self.b5 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b5))
        self.b6 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b6))
        self.b7 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b7))
        self.b8 = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=7, width=10, bg='SystemButtonFace', command=lambda: self.buttonClick(self.b8))
        self.b0.grid(row=0, column=0)
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)
        self.b3.grid(row=1, column=0)
        self.b4.grid(row=1, column=1)
        self.b5.grid(row=1, column=2)
        self.b6.grid(row=2, column=0)
        self.b7.grid(row=2, column=1)
        self.b8.grid(row=2, column=2)
        self.turnLabel = tk.Label(self.root, text='Your Turn', height=3, width=8)
        self.turnLabel.grid(row=1,column=3)


    def gameOver(self):
        """Toggles when the game is over."""
        self.playAgain()


    def playAgain(self):
        """Asks the player to end or start a new game.
        """

        self.playAgainLabel = tk.Label(self.root, text="Play again?")
        self.playAgainLabel.grid(row=2, column=4)

        self.yesButton = tk.Button(self.root, text="Yes", command=self.resetButton)
        self.yesButton.grid(row=5, column=3, sticky='E')

        self.noButton = tk.Button(self.root, text="No", command=self.displayStats)
        self.noButton.grid(row=5, column=5, sticky='W')



    def clearWidgets(self):
        """Clears all widgets from the window."""
        lists = self.root.winfo_children()
        for wid in lists:
            wid.destroy()

    def displayStats(self):
        """Prints the overall stats for the player."""
        self.newSocket.send('stat'.encode())

        self.clearWidgets()

        # Set up font
        title_font = font.Font(family='Helvetica', size=18, weight='bold')
        label_font = font.Font(family='Helvetica', size=12)

        # Set up title label
        self.title = tk.Label(self.root, text='GAME STATS', font=title_font)
        self.title.grid(row=0, column=1, padx=10, pady=10, sticky='n')

        # Set up other labels
        self.nameLabel = tk.Label(self.root, text=f'Player: {self.gameBoard.playerName}', font=label_font)
        self.nameLabel.grid(row=2, column=1, padx=10, pady=5, sticky='n')

        self.oppLabel = tk.Label(self.root, text=f'Opponent: {self.gameBoard.player2name}', font=label_font)
        self.oppLabel.grid(row=4, column=1, padx=10, pady=5, sticky='n')

        self.winLabel = tk.Label(self.root, text=f'Number of Wins: {self.gameBoard.p1wins}', font=label_font)
        self.winLabel.grid(row=6, column=1, padx=10, pady=5, sticky='n')

        self.lossLabel = tk.Label(self.root, text=f'Number of Losses: {self.gameBoard.p1loss}', font=label_font)
        self.lossLabel.grid(row=8, column=1, padx=10, pady=5, sticky='n')

        self.tieLabel = tk.Label(self.root, text=f'Number of Ties: {self.gameBoard.ties}', font=label_font)
        self.tieLabel.grid(row=10, column=1, padx=10, pady=5, sticky='n')

        self.totalLabel = tk.Label(self.root, text=f'Total Games Played: {self.gameBoard.updateGamesPlayed()}',
                                   font=label_font)
        self.totalLabel.grid(row=12, column=1, padx=10, pady=5, sticky='n')

    def convertPostion(self, button):
        if button == self.b0:
            return 0
        if button == self.b1:
            return 1
        if button == self.b2:
            return 2
        if button == self.b3:
            return 3
        if button == self.b4:
            return 4
        if button == self.b5:
            return 5
        if button == self.b6:
            return 6
        if button == self.b7:
            return 7
        if button == self.b8:
            return 8


    def disableButton(self):
        """Disables all buttons."""
        listofButtons = [self.b0, self.b1,self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8]
        for button in listofButtons:
            button['state'] = tk.DISABLED


    def enableButton(self):
        """Enables available buttons."""
        listofButtons = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8]
        for button in listofButtons:
            if button['state'] == tk.DISABLED and button['text'] == ' ':
                button.update()
                button['state'] = tk.NORMAL


if __name__ == '__main__':
    p1 = GUI()
