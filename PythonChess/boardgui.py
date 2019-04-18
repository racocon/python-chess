import chessboard
from tkinter import *
import time


class BoardGUI:


    #initialize variables
    mousePressedX = 0
    mousePressedY = 0
    mouseReleasedX = 0
    mouseReleasedY = 0

    move2compare = []

    #constructor (will be called automatically when the class is called)
    def __init__(self):
        #initialize the GUI frame
        self.root = Tk()

        #set the canvas height and width
        self.canvas_height = 640
        self.canvas_width = 640

        #set the square size
        self.square_size = 80

        #create a container for the whole display
        self.myContainer1 = Frame(self.root)
        #add the container to the Frame
        self.myContainer1.pack()

        #create a canvas
        self.w = Canvas(self.myContainer1, width = self.canvas_width, height = self.canvas_height)
        #add the canvas to the frame
        self.w.pack()

        #this creates the chessboard
        #this goes from left to right, top to bottom
        for i in range(8):
            for j in range(8):
                if (j+i)%2 == 0:
                    self.w.create_rectangle(i*self.square_size, j*self.square_size, self.square_size*(i+1), self.square_size*(j+1), fill = "#778ca3") #light
                else:
                    self.w.create_rectangle(i*self.square_size, j*self.square_size, self.square_size*(i+1), self.square_size*(j+1), fill = "#4b6584") #dark


        #this command updates the GUI every 10 ms
        #calls the drawPieces() function every 10 ms
        self.root.after(10, self.drawPieces)
        self.root.mainloop()



    #this function fires during a mousepress event
    def Mousepress(self, event):
        #get the position of the mouse press and divide with the square size to get the square of which the mouse pointer is pointed
        self.mousePressedX = int(event.y/self.square_size)
        self.mousePressedY = int(event.x/self.square_size)
        #this function returns nothing, it just updates the mousePressedX and mousePressedY variables
        return

    #this function fires when the mouse is released
    def Mousereleased(self, event):
        #get the location of the mouse release event
        self.mouseReleasedX = event.y
        self.mouseReleasedY = event.x
        #initialize a list to verify the move
        self.move2compare = []
        #append the position of the mouse clicked and the mouse released location
        self.move2compare.append((self.mousePressedX, self.mousePressedY, int(self.mouseReleasedX/self.square_size), int(self.mouseReleasedY/self.square_size)))
        #calls the function determinePiece() from the chessboard.py
        chessboard.Board().determinePiece(self.move2compare)
        #this calls back the function drawPieces() after 100 ms
        self.root.after(100, self.drawPieces())
        return



    #this function is used to draw the pieces on the board
    def drawPieces(self):

        #all these lines set the variables to the right image path
        #subsample function reduces the size of the image
        self.w.whiteRook        = PhotoImage(file="BRook.png")#.subsample(4,4)
        self.w.whiteKnight      = PhotoImage(file="BKnight.png")#.subsample(4,4)
        self.w.whiteBishop      = PhotoImage(file="BBishop.png")#.subsample(4,4)
        self.w.whiteQueen       = PhotoImage(file="BQueen.png")#.subsample(4,4)
        self.w.whiteKing        = PhotoImage(file="BKing.png")#.subsample(4,4)
        self.w.whitePawn        = PhotoImage(file="BPawn.png")#.subsample(4,4)

        self.w.blackRook        = PhotoImage(file="RRook.png")#.subsample(4,4)
        self.w.blackKnight      = PhotoImage(file="RKnight.png")#.subsample(4,4)
        self.w.blackBishop      = PhotoImage(file="RBishop.png")#.subsample(4,4)
        self.w.blackQueen       = PhotoImage(file="RQueen.png")#.subsample(4,4)
        self.w.blackKing        = PhotoImage(file="RKing.png")#.subsample(4,4)
        self.w.blackPawn        = PhotoImage(file="RPawn.png")#.subsample(4,4)

        #iterates through all the tiles
        for i in range(64):
            ########## WHITE PIECES ##########
            #if the particular tile on the board has the letter "R", then a white Rook will be placed
            if chessboard.Board().chessBoard[int(i/8)][i%8] == "R":
                WRook = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whiteRook)
                self.w.tag_bind(WRook, "<ButtonPress-1>", self.Mousepress) #binding the rook image with the function Mousepress()
                self.w.tag_bind(WRook, "<ButtonRelease-1>", self.Mousereleased) #binding the rook image with the function Mousereleased()

            #if the particular tile on the board has the letter "N", then a white Knight will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "N":
                WKnight = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whiteKnight)
                self.w.tag_bind(WKnight, "<ButtonPress-1>", self.Mousepress) #binding the knight image with the function Mousepress()
                self.w.tag_bind(WKnight, "<ButtonRelease-1>", self.Mousereleased) #binding the knight image with the function Mousereleased()

            #if the particular tile on the board has the letter "B", then a white Bishop will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "B":
                WBishop = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whiteBishop)
                self.w.tag_bind(WBishop, "<ButtonPress-1>", self.Mousepress) #binding the bishop image with the function Mousepress()
                self.w.tag_bind(WBishop, "<ButtonRelease-1>", self.Mousereleased) #binding the bishop image with the function Mousereleased()

            #if the particular tile on the board has the letter "Q", then a white Queen will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "Q":
                WQueen = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whiteQueen)
                self.w.tag_bind(WQueen, "<ButtonPress-1>", self.Mousepress) #binding the queen image with the function Mousepress()
                self.w.tag_bind(WQueen, "<ButtonRelease-1>", self.Mousereleased) #binding the queen image with the function Mousereleased()

            #if the particular tile on the board has the letter "K", then a white King will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "K":
                WKing = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whiteKing)
                self.w.tag_bind(WKing, "<ButtonPress-1>", self.Mousepress) #binding the king image with the function Mousepress()
                self.w.tag_bind(WKing, "<ButtonRelease-1>", self.Mousereleased) #binding the king image with the function Mousereleased()

            #if the particular tile on the board has the letter "P", then a white Pawn will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "P":
                WPawn = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.whitePawn)
                self.w.tag_bind(WPawn, "<ButtonPress-1>", self.Mousepress) #binding the pawn image with the function Mousepress()
                self.w.tag_bind(WPawn, "<ButtonRelease-1>", self.Mousereleased) #binding the pawn image with the function Mousereleased()

            ########## BLACK PIECES ##########
            #if the particular tile on the board has the letter "r", then a black Rook will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "r":
                BRook = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackRook)
                self.w.tag_bind(BRook, "<ButtonPress-1>", self.Mousepress) #binding the rook image with the function Mousepress()
                self.w.tag_bind(BRook, "<ButtonRelease-1>", self.Mousereleased) #binding the rook image with the function Mousereleased()

            #if the particular tile on the board has the letter "n", then a white Knight will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "n":
                BKnight = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackKnight)
                self.w.tag_bind(BKnight, "<ButtonPress-1>", self.Mousepress) #binding the knight image with the function Mousepress()
                self.w.tag_bind(BKnight, "<ButtonRelease-1>", self.Mousereleased) #binding the knight image with the function Mousereleased()

            #if the particular tile on the board has the letter "b", then a white Bishop will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "b":
                BBishop = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackBishop)
                self.w.tag_bind(BBishop, "<ButtonPress-1>", self.Mousepress) #binding the bishop image with the function Mousepress()
                self.w.tag_bind(BBishop, "<ButtonRelease-1>", self.Mousereleased) #binding the bishop image with the function Mousereleased()

            #if the particular tile on the board has the letter "q", then a white Queen will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "q":
                BQueen = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackQueen)
                self.w.tag_bind(BQueen, "<ButtonPress-1>", self.Mousepress) #binding the queen image with the function Mousepress()
                self.w.tag_bind(BQueen, "<ButtonRelease-1>", self.Mousereleased) #binding the queen image with the function Mousereleased()

            #if the particular tile on the board has the letter "k", then a white King will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "k":
                BKing = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackKing)
                self.w.tag_bind(BKing, "<ButtonPress-1>", self.Mousepress) #binding the king image with the function Mousepress()
                self.w.tag_bind(BKing, "<ButtonRelease-1>", self.Mousereleased) #binding the king image with the function Mousereleased()

            #if the particular tile on the board has the letter "p", then a white Pawn will be placed
            elif chessboard.Board().chessBoard[int(i/8)][i%8] == "p":
                BPawn = self.w.create_image((i%8)*self.square_size+2, int(i/8)*self.square_size+2, anchor="nw", image=self.w.blackPawn)
                self.w.tag_bind(BPawn, "<ButtonPress-1>", self.Mousepress) #binding the pawn image with the function Mousepress()
                self.w.tag_bind(BPawn, "<ButtonRelease-1>", self.Mousereleased) #binding the pawn image with the function Mousereleased()

#calls the class
BoardGUI()
