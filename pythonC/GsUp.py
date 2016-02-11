from matrix import matrix

def GaussianUp(mean1, sigma21, mean2, sigma22):
    NewM = 1.*(sigma21*mean2+sigma22*mean1)/(sigma21+sigma22)
    NewS = 1.*sigma21*sigma22/(sigma21+sigma22)
    return NewM, NewS

def MotionUp(mean1, sigma21, mean2, sigma22):
    NM = mean1+mean2
    NS = sigma21+sigma22
    return NM, NS

x = matrix([ [1 ,1, 1],
             [2, 2, 2]])
y = matrix([[1,1],[2,2],[3,3]])




z = x * y
z.show()
z=z.transpose()
z.show()








#initial state of location and velocity
#x =