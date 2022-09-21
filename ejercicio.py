import math
X = 0
Y = 0

class Punto:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def cuadrante(self):
        if self.X > 0 and self.Y > 0:
            print( "Pertenece al primer cuadrante")
        elif self.X > 0 and self.Y < 0:
            print( "Pertenece al 4º cuadrante")
        elif self.X < 0 and self.Y > 0:
            print( "Pertenece al 2º cuadrante")
        elif self.X < 0 and self.Y > 0:
            print( "Pertenece al 4º cuadrante")
        elif self.X != 0 and self.Y == 0:
            print ("Se encuentra en el eje Y")
        elif self.X == 0 and self.Y != 0:
            print( "Se encuentra en el eje X")
        else:
            print("Se encuentra en el origen")
        