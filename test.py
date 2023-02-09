import numpy as np
import matplotlib.pyplot as plt

"""
plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()
"""
def iaf_step(V, Vrest, tau, I, R, dt):
  Vnew = V + ((-V + Vrest + (R * I)) / (tau)) * dt
  return(Vnew)

dt = 0.1

t = np.arange(0,1000,dt)
Vout = -70*np.ones(len(t))
newI = np.arange(0,6,.05)
spike  = 0

vReset = -80


refractoryPeriod = 10
refractoryPauseCount = 0
inRefractory = False

I = 5

for j in range(len(t)-1):
    if Vout[j] >= -50:
      Vout[j] = 20
      Vout[j+1] = vReset
      spike += 1
      inRefractory = True
    elif inRefractory:
      refractoryPauseCount += 1
      Vout[j+1] = vReset
      if refractoryPauseCount*dt >= refractoryPeriod:
        inRefractory = False
        refractoryPauseCount = 0
    else:
      Vout[j+1] = iaf_step(Vout[j], -70, 10, I, 10, dt)

plt.plot(t,Vout)
plt.show()

print(spike)