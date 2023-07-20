"""This is server (player2)."""
import tkinter as tk
from gameboard import BoardClass
import socket


class GUI:
    """A class for a user to player Tic tac toe through a graphic user interface for the server side."""
    def __init__(self):
        self.gameBoard = BoardClass()
        self.root = tk.Tk()
        self.root.title('Player 2 (server): Tic-Tac-Toe')
        self.root.geometry('600x600')
        self.tkinterVariables()
        self.getHostInfo()
        self.root.mainloop()
        self.boardSetUp()
        self.root.mainloop()


    def tkinterVariables(self):
        """Sets tkinter variables to reference."""
        self.host = tk.StringVar()
        self.port = tk.IntVar()
        self.username = tk.StringVar()


    def connectP1(self):
        """Connects the two players through sockets."""
        try:
            HOST = self.host.get()
            PORT = self.port.get()
            self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.newSocket.bind((HOST, PORT))
            self.newSocket.listen(5)
            self.p1socket, self.p1address = self.newSocket.accept()
            self.root.after(200, self.getp1user)
        except:
            pass


    def getp1user(self):
        """Receives player 1 username."""
        self.player1Name = self.p1socket.recv(1024).decode()
        self.gameBoard.setPlayer1name(self.player1Name)
        self.gameBoard.setLastPlayer(self.player1Name)
        self.sendP2user()


    def sendP2user(self):
        """Sends player 2's username to player 1."""
        self.clearWidgets()
        self.userLabel = tk.Label(self.root, text = "Enter username: ")
        self.userLabel.grid(row=2,column=0, sticky ='E')
        self.userEntry = tk.Entry(self.root, textvariable = self.username)
        self.userEntry.grid(row=2, column=1, sticky='N')
        player2name = self.username.get()
        self.gameBoard.setPlayer2name(player2name)
        print(self.gameBoard.player2name)
        self.confirmUsername = tk.Button(self.root, text='Confirm.', command=lambda: self.p2socketUser())
        self.confirmUsername.grid(row=3)


    def getHostInfo(self):
        """Creates widgets for the user to enter host, port, and username."""

        self.hostLabel = tk.Label(self.root, text = "Input host name: ")
        self.hostLabel.grid(row=0, column=0, sticky='E')
        self.hostEntry = tk.Entry(self.root, textvariable = self.host)
        self.hostEntry.grid(row=0, column=1, sticky='N')
        self.portLabel = tk.Label(self.root, text = "Input port number: ")
        self.portLabel.grid(row=1, column=0, sticky='E')
        self.portEntry = tk.Entry(self.root, textvariable = self.port)
        self.portEntry.grid(row=1, column=1, sticky='N')
        self.confirmButt = tk.Button(self.root, text='Confirm.', command=lambda: self.connectP1())
        self.confirmButt.grid(row=3)


    def p2socketUser(self):
        """Sends player 2 username to player 1."""
        self.p1socket.send(self.username.get().encode())
        self.boardSetUp()
        self.disableButton()


    def recieveMove(self):
        """Recieves player 1 move, updating the board, and checks if game is over."""
        self.disableButton()
        self.player1move = self.p1socket.recv(1024).decode()
        self.changeButtons()
        self.gameBoard.setLastPlayer(self.gameBoard.playerName)
        self.gameBoard.updateGameBoard(int(self.player1move), 'X')
        self.turnLabel.config(text="Your Turn")
        if not self.gameBoard.isWinner() and not self.gameBoard.boardIsFull():
            self.enableButton()
        else:
            self.changeButtons()
            self.turnLabel.config(text="Game Over")
            self.root.after(200,self.gameOver)


    def changeButtons(self):
        """Converts player 1's move to an X on the board."""
        if int(self.player1move) == 0:
            self.b0.config(text='X')
        if int(self.player1move) == 1:
            self.b1.config(text='X')
        if int(self.player1move) == 2:
            self.b2.config(text='X')
        if int(self.player1move) == 3:
            self.b3.config(text='X')
        if int(self.player1move) == 4:
            self.b4.config(text='X')
        if int(self.player1move) == 5:
            self.b5.config(text='X')
        if int(self.player1move) == 6:
            self.b6.config(text='X')
        if int(self.player1move) == 7:
            self.b7.config(text='X')
        if int(self.player1move) == 8:
            self.b8.config(text='X')


    def sendMove(self, position):
        """Sends player 2 move to player 1."""
        self.p1socket.send(str(position).encode())
        self.disableButton()
        self.root.after(200, self.recieveMove)


    def buttonClick(self, button):
        """Updates GUI to show a symbol where the user clicked.

        Args:
            button: Button that was pressed."""
        if button['text'] == ' ':
            button.config(text='O')
            self.disableButton()
            self.turnLabel.config(text="Their Turn")
            self.gameBoard.updateGameBoard(self.convertPostion(button), 'O')
            if self.gameBoard.isWinner() or self.gameBoard.boardIsFull():
                button = self.convertPostion(button)
                self.turnLabel.config(text="Game Over")
                self.p1socket.send(str(button).encode())
                self.root.after(200,self.gameOver)
            else:
                self.sendMove(self.convertPostion(button))
                self.turnLabel.config(text="Their Turn")

    def boardSetUp(self):
        """Sets up the board at the beginning of game."""
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
        self.disableButton()

        self.turnLabel = tk.Label(self.root, text="Their Turn", height=3, width=8)
        self.turnLabel.grid(row=1, column=3)
        self.root.after(200, self.recieveMove)


    def resetButton(self):
        """Resets the GUI board."""
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
        self.turnLabel = tk.Label(self.root, text='Their Turn', height=3, width=8)
        self.turnLabel.grid(row=1,column=3)
        self.root.after(200,self.recieveMove)



    def clearWidgets(self):
        """Clears all widgets."""
        lists = self.root.winfo_children()
        for wid in lists:
            wid.destroy()


    def convertPostion(self, button):
        """Converts the button clicked into a postion integer.
        args:
        button: The button that was pressed.

        returns:
        int"""
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

    def gameOver(self):
        """Clears widgets and prompts the user to play again."""
        self.clearWidgets()
        self.playAgain()


    def playAgain(self):
        """Resets the game or prints stats after player 1 choice.
        """
        verdict = self.p1socket.recv(1024).decode()
        if verdict == 'again':
            self.resetButton()
        if verdict == 'stat':
            self.displayStats()


    def displayStats(self):
        """Prints the overall stats for the player.
        """
        self.clearWidgets()

        self.title = tk.Label(self.root, text='GAME STATS')
        self.title.grid(row=0, column=1)
        print(self.gameBoard.player2name)
        self.nameLabel = tk.Label(self.root, text=f'Player : {self.username.get()}')
        self.nameLabel.grid(row=2, column=1)

        self.oppLabel = tk.Label(self.root, text=f'Opponent : {self.gameBoard.playerName}')
        self.oppLabel.grid(row=4, column=1)

        self.winLabel = tk.Label(self.root, text=f'Number of Wins : {self.gameBoard.p2wins}')
        self.winLabel.grid(row=6, column=1)

        self.lossLabel = tk.Label(self.root, text=f'Number of Losses : {self.gameBoard.p2loss}')
        self.lossLabel.grid(row=8, column=1)

        self.tieLabel = tk.Label(self.root, text=f'Number of Ties : {self.gameBoard.ties}')
        self.tieLabel.grid(row=10, column=1)

        self.totalLabel = tk.Label(self.root, text=f'Total Games Played : {self.gameBoard.updateGamesPlayed()}')
        self.totalLabel.grid(row=12, column=1)


    def disableButton(self):
        """Disables tic tac toe buttons."""

        listofButtons = [self.b0, self.b1,self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8]
        for button in listofButtons:
            button['state'] = tk.DISABLED


    def enableButton(self):
        """Enables available tic tac toe buttons."""
        listofButtons = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8]
        for button in listofButtons:
            if button['state'] == tk.DISABLED and button['text'] == ' ':
                button.update()
                button['state'] = tk.NORMAL


if __name__ == '__main__':
    p2 = GUI()