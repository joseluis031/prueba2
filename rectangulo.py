class Rectangulo:
    x1 = 2
    y1 = 3
    x2 = 5
    y2 = 5



    a = [x1,y1]
    b = [x2,y2]
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def base(self):
        print("la base es {} ".format(self.x2 - self.x1))
        
    def altura(self):
        print("la altura es {}".format(self.y2 - self.y1))
        
    def area(self):
        print("El area es {}".format((self.x2-self.x1)*(self.y2-self.y1)))
              
