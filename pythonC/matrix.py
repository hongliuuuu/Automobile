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
        res.zero(self.dimx, self.dimy)
        for i in range(self.dimx):
            for j in range(self.dimy):
                res[i][j] = self.value[j][i]

        return res


    def __getitem__(self, item):
        return self.value[item]