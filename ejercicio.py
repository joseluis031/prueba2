import math

a = [2,3]
b = [5,5]
c = [-3,-1]
d = [0,0]
class Punto:
    a = [2,3]
    b = [5,5]
    c = [-3,-1]
    d = [0,0]
    punto = (0,3)
    X = 0
    Y = 0
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
    
    def vector(self,punto):
        print( "El vector sera({}, {})".format(punto.X -self.X, punto.Y - self.Y))
        




        