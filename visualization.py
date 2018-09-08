import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def ysBuilder(file):
	out = []
	with open(file) as f:
		for line in f:
			num = float(line)
			out.append(num)
	return out
ys = ysBuilder('./FEP-thin-plasma-2-chirp/FEP-thin-plasma-2-chirp-50cm.csv')
time = list(enumerate(ys,0))
time = [t[0] for t in time]

ax1.clear()
ax1.plot(time,ys)

class animateWrapper:
	def __init__(self):
		print('preparing animation')
	def animate(self,i,offset = 1000): #offset control the speed of animation
		i = i * offset
		if i >= len(time) - 2:
			return
		plt.bar([i,i,i+offset,i+offset], [0.6,-0.6,0.6,-0.6],1000,color = ('white','white', 'red', 'red'))


a = animateWrapper()
ani = animation.FuncAnimation(fig, a.animate,interval = 1)
plt.show()
