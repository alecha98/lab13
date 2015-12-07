class Matrix:


    def __init__(self, m, n=None):
        self.m=m
        self.n=n
        if n==None:
            self.Mat=int([0])*m
        else:
            self.Mat=int([0])*m
            for a in range(m):
                self.Mat[a]=[0]*n

    def __add__(self, other):
        for a in range (self.m):
            for b in range (self.n):
                self.Mat[a,b]=self.Mat[a,b]+other.Mat[a,b]
        return self.Mat

    def determinant (self):
        pass

    def __eq__(self, other):
        flag=0
        for a in range (self.m):
            for b in range (self.n):
                if self.Mat[a,b]:
                    pass

    def get(self, i, j):
        return self.Mat(i,j)

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def get_size(self):
        pass

    def invert (self):
        pass

    def __mul__(self, other):
        pass

    def set(self, i, j, value):
        Mat[i,j]=value

    def __sub__(self, other):
        pass

    def transpose (self):
        pass

    def __truediv__(self, other):
        pass
