import numpy as np
import matplotlib.pyplot as plt

def iaf_step(V, Vrest, tau, I, R, dt):
  Vnew = V + ((-V + Vrest + (R * I)) / (tau)) * dt
  return(Vnew)

vReset = -80
dt = 0.1

refractoryPeriod = [5,10,20,50]

t = np.arange(0,1000,dt)
newI = np.arange(0,6,.02)
spike  = np.zeros((len(newI),len(refractoryPeriod)))




for k in range(len(refractoryPeriod)):
  Vout = -70*np.ones(len(t))
  refractoryPauseCount = 0
  inRefractory = False
  for i in range(len(newI)):
    for j in range(len(t)-1):
        if Vout[j] >= -50:
            Vout[j] = 20
            Vout[j+1] = vReset
            spike[i,k] += 1
            inRefractory = True
        elif inRefractory:
            refractoryPauseCount += 1
            Vout[j+1] = vReset
            if refractoryPauseCount*dt >= refractoryPeriod[k]:
                inRefractory = False
                refractoryPauseCount = 0
        else:
            Vout[j+1] = iaf_step(Vout[j], -70, 10, newI[i], 10, dt)

    #plt.plot(t,Vout)
    #plt.pause(.02)
    
plt.show()

sim = 1/(1000/spike*.001)
sim[np.isnan(sim)] = 0


plt.plot(newI,sim)
plt.xlabel("Current (mA)")
plt.ylabel("# of spikes")
plt.title("# of Spikes vs Current for " + str(refractoryPeriod) + " ms Refractory Period")
plt.legend(["5","10","20","50"])
plt.show()