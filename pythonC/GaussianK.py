# 1d Kalman filter

from math import *

def gaussian(mu, sigma2, x):
    return (1/sqrt(2*pi*sigma2))*exp(-0.5*(x-mu)**2/sigma2)

def measureUpdate(mu1, sigma12,mu2,  sigma22): #prior and measurement
    mu = (mu1*sigma22+mu2*sigma12)/(sigma12+sigma22)
    sigma2 = (sigma12*sigma22)/(sigma12+sigma22)
    return [mu, sigma2]

def motionPredict(mean1,var1,mean_motion, var_motion):
    mean=mean1+mean_motion
    var = var1+var_motion
    return [mean, var]

mu = 0.
sig = 1000.

measurement = [5.,6.,7.,9.,10.]
measurement_sig = 4.
motion =[1.,1.,2.,1.,1.]
motion_sig = 2.

for i in range(len(measurement)):
    [mu,sig] = measureUpdate(mu, sig,measurement[i],measurement_sig)
    print 'update:',[mu, sig]
    [mu,sig] = motionPredict(mu, sig, motion[i],motion_sig)
    print 'predict:',[mu, sig]