from math import *

class matrix:

    def __init__(self, value):
        self.value = value
        self.dimx = len(value)
        self.dimy = len(value[0])
        if value==[[]]:
            self.dimx=0

    def  zero(self,dimx,dimy):
        #check if the matrix is valide
        if dimx<1 or dimy<1:
            raise ValueError, 'Invalide matrix'
        else:
            self.dimx = dimx
            self.dimy = dimy
            self.value = [[0 for i in range(dimy)] for j in range(dimx)]

    def identy(self,dim):
        if dim < 1:
            raise ValueError, 'Invalide dimension'
        else:
            self.dim = dim
            self.value = [[0 for i in range(dim)] for j in range(dim)]
            for i in range(dim):
                self.value[i][i]=1

    def show(self):
        for i in range(self.dimx):
            print self.value[i]

    def __add__(self, other):
        # check if same dim
        if self.dimx != other.dimx or self.dimy != other.dimy:
            raise ValueError, 'Dimension not match'
        else:
            res = matrix([[]])
            res.zero(self.dimx,self.dimy)
            for i in range(self.dimx):
                for j in range(self.dimy):
                    res[i][j] = self.value[i][j]+other.value[i][j]
        return res

    def __sub__(self, other):
        if self.dimx != other.dimx or self.dimy != other.dimy :
            raise ValueError, 'Dimension not match'
        else:
            res = matrix([[]])
            res.zero(self.dimx,self.dimy)
            for i in range(self.dimx):
                for j in range(self.dimy):
                    res[i][j] = self.value[i][j]-other.value[i][j]
        return res

    def __mul__(self, other):
        if self.dimy != other.dimx:
            raise ValueError, 'Dimension not match'
        else:
            res =  matrix([[]])
            res.zero(self.dimx, other.dimy)
            for i in range(self.dimx):
                for j in range(other.dimy):
                    for k in range(self.dimy):
                        res[i][j] += self.value[i][k]*other.value[k][j]
        return res

    def transpose(self):
        res = matrix([[]])
        res.zero(self.dimy, self.dimx)
        for i in range(self.dimx):
            for j in range(self.dimy):
                res[j][i] = self.value[i][j]

        return res

    def Cholesky(self, ztol=1.0e-5):
        # computes the upper triangular Cholexcy factorization of a positive definite matrix
        res = matrix([[]])
        res.zero(self.dimx,self.dimy)
        for i in range(self.dimx):
            S = sum([res[k][i]**2 for k in range(i)])
            d = self.value[i][i]-S
            if abs(d)<ztol:
                res.value[i][i]=0.0
            else:
                if d<0.0:
                    raise ValueError, "Matrix not positive definite"
                res.value[i][i] = sqrt(d)
            for j in range(i+1, self.dimx):
                S = sum([res.value[k][i] * res.value[k][j] for k in range(i)])
                if abs(S) < ztol:
                    S = 0.0
                try:
                    res.value[i][j] = (self.value[i][j] - S)/res.value[i][i]
                except:
                    raise ValueError, "Zero diagonal"
        return(res)

    def CholeskyInverse(self):
        """
        Computes inverse of matrix given its Cholesky upper Triangular
        decomposition t.
        """
        res = matrix([[]])
        res.zero(self.dimx,self.dimy)

        # Backward step for inverse.
        for j in reversed(range(self.dimx)):
            tjj = self.value[j][j]
            S = sum([self.value[j][k]*res.value[j][k] for k in range(j+1, self.dimx)])
            res.value[j][j] = 1.0/ tjj**2 - S/ tjj
            for i in reversed(range(j)):
                res.value[j][i] = res.value[i][j] = -sum([self.value[i][k]*res.value[k][j] for k in range(i+1,self.dimx)])/self.value[i][i]
        return res

    def inverse(self):
        aux = self.Cholesky()
        res = aux.CholeskyInverse()
        return res

    def __getitem__(self, item):
        return self.value[item]

def filter(x,P):
    for n in range(len(measurements)):
        Z = matrix([[measurements[n]]])
        y = Z -(H*x)
        S = H * P *H.transpose()+R
        K = P *H.transpose()*S.inverse()
        x = x + (K*y)

        P = (I -(K*H))*P

        #prediction
        x = (F*x)+u
        P = F*P*F.transpose()

        print 'x='
        x.show()
        print 'P='
        P.show()









measurements = [1,2,3]
H = matrix([[1.,0.]])#measurement function
P = matrix([[1000., 0.],[0.,1000.]])#initial uncertainty
x = matrix([[0.],[0.]])#initial state location and velocity
R = matrix([[1.]])#measurement uncerktainty
I = matrix([[1.,0.],[0.,1.]])#indentity matrix
u =matrix([[0.],[0.]])#external motion
F = matrix([[1.,1.],[0.,1.]])#next state function

filter(x,P)