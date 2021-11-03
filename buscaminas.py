from random import randint
class Exception(Exception):
    pass

class Buscaminas:
    def __init__(self,rows,cols,bombs):
        self.esta_jugando = True
        self.hay_bomba = False
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = self.crear_tablero()
        self.initial_board = [['-' for x in range(self.rows)] for y in range(self.cols)]
        
    
    def show_board(self):
        for fila in self.initial_board:
            print(fila, "\n")
        for fila in self.board:
            print(fila, "\n")
        #aca lo que se hace es mostrar lo que el jugador va marcando
    
    def question(self,movs):
        #que movimiento desea elegir el usuario [][[]]
        self.movs = input("Ingrese el movimiento, flag o uncover: ")
        self.row = input("Elija una fila para su movimiento: ")
        self.col = input("Elija una columna: ")
        if movs == "flag":
            self.board[self.row][self.col] = "F"
        if movs == "uncover":
            self.board[self.row][self.col] = self.board[self.row][self.col]
        
        if movs != "flag" and movs != "uncover":
            raise Exception()

    def crear_tablero(self):
        board = [[randint(1, 4) for x in range(self.rows)] for y in range(self.cols)]
        for i in range(self.bombs):
            board[randint(0,self.rows-1)][randint(0,self.cols-1)] = 'B'
        return board
    
    def show(self):
        return self.initial_board

    def play(self,mov,row,col):
        if mov == 'flag':
            self.initial_board[row][col] = 'F'
        if mov == 'uncover':
            if self.hay_bomba(row, col):
                self.lose()
            else:
                self.initial_board[row][col] = self.board[row][col]
       
        
    
    def win(self):
        a = 0
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == "B" and self.initial_board[row][col] == "F":
                    a += 1
        if a == self.bombs:
            return True
        else:
            return False
                
        #se gana cuando se completa el tablero poniendo las banderas donde van las bombas
    def lose(self):
        #se pierde cuando se elige un lugar que haya una bomba
        return True

if __name__ == '__main__':
    movs = ['flag', 'uncover']
    buscaminas = Buscaminas(rows=8, cols=8, bombs=10)
    print('Juego')
    buscaminas.show_board()
    # jugar
    while not buscaminas.win() and not buscaminas.lose():
        try:
            mov, row, col = buscaminas.question(movs)
            buscaminas.play(mov, row, col)
            print('Juego')
            buscaminas.show_board()
        except:
            print('Movimiento ilegal')
    if buscaminas.win():
        print('Ganaste')
    else:
        print('Perdiste')

    



