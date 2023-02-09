import numpy as np
import matplotlib.pyplot as plt

def iaf_step(V, Vrest, tau, I, R, dt):
  Vnew = V + ((-V + Vrest + (R * I)) / (tau)) * dt

  return(Vnew)
  

refractoryPeriod = 16
inRefrac = False
refracCount = 0
dt = .1
numfires = 0
t = np.arange(0,500,dt)
V = -70
vReset = -80
vTh = -54
timeBetweenSpikes = 0.0
out = np.zeros(len(t), dtype = float)
out[0] = -70
for i in range(len(t)-1):
  if inRefrac:
    out[i+1] = vReset
    refracCount += 1
    if refracCount*dt >= refractoryPeriod:
      inRefrac = False
  elif (400 > t[i]) and (t[i] > 100):
    I = 6
  else:
    I = 0
  if not inRefrac:
    out[i+1] = iaf_step(out[i],-70, 10, I, 10, .1)
  if out[i] > vTh:
    plt.vlines(t[i], vTh, 20, 'c')
    out[i+1] = vReset
    numfires += 1
    inRefrac = True
    refracCount = 0 




plt.plot(t,out, 'c')
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Voltage vs Time for a Refractory Period of " + str(refractoryPeriod) + " ms")
plt.show()
print(300/numfires)