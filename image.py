import matplotlib.pyplot as plt 
import numpy as np 

a=np.array([0.3121212121,0.42121212121,0.512121212121,0.531313212313131
,0.231311212,0.52312312121,0.121212121,0.61231231,0.123123112]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shrink=0.9)
plt.xticks(())
plt.yticks(())
plt.show()