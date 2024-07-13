import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ux_prof.dat', delimiter=',')

fig = plt.figure()
plt.plot(df[' ux_exact'])
plt.savefig('velocityProfile.png')

