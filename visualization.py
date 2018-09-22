import matplotlib.pyplot as plt
from ctypes import string_at
import matplotlib.animation as animation
from matplotlib import style
import random
import numpy as np
from pyaudio import PyAudio
import time
class audioSignal:
	def __init__(self):
		self.buffer = []
		self.tracker= 0
		self.base = 0
		BITRATE = 16000
		p = PyAudio()
		self.stream = p.open(
		    format=p.get_format_from_width(1),
		    channels=1,
		    rate=BITRATE,
		    output=True,
		    )
		self.time = []
		self.timeUnit = 0.001
		self.fig = plt.figure()
		self.ax1 = self.fig.add_subplot(111)
		plt.ion()
	def load(self, data):
		#print("input" + str(data))
		if self.chanceFilter(data) == data:
			print("acpt" + str(data))
			self.buffer.append(data)
			self.time.append(self.timeUnit)
			self.tracker +=1
			self.timeUnit += 0.01
			if  self.tracker%100 == 0:
				#freq = np.fft.fft(self.buffer[self.base : self.tracker+self.base])
				freq = np.fft.fftfreq(np.array(self.buffer[self.base : self.tracker]).shape[-1])
				print('play sound' + str(self.base))
				# TODO -> properly plays the sound 
				self.stream.write(freq)
				print('finish' + str(self.base))
				# TODO -> fix plotting 
				self.ax1.plot(self.time,self.buffer)
				self.fig.canvas.draw()
				#time.sleep(10) 
				self.base = self.tracker
				
				#plt.show(block= )

				
	# TODO -> correct way of desampling data
	def chanceFilter(self, input, chance = 200):
		x = random.randint(1,chance)
		if x == 2:
			return input
		else:
			return False

	def ysBuilder(self,file):
		out = []
		with open(file) as f:
			for line in f:
				num = float(line)
				out.append(num)
		return out
	
	def initBlank(self):
		self.ax1.plot([],[])
		#plt.show()
	class animateWrapper:
		def __init__(self):
			print('preparing animation')
		def animate(self,i,offset = 1000): #offset control the speed of animation
			i = i * offset
			if i >= len(time) - 2:
				return
			plt.bar([i,i,i+offset,i+offset], [0.6,-0.6,0.6,-0.6],1000,color = ('white','white', 'red', 'red'))
	def testrun(self):
		ys = self.ysBuilder('./FEP-thin-plasma-2-chirp/FEP-thin-plasma-2-chirp-50cm.csv')
		time = list(enumerate(ys,0))
		time = [t[0] for t in time]

		self.ax1.clear()
		self.ax1.plot(time,ys)
		#a = animateWrapper()
		#ani = animation.FuncAnimation(self.fig, a.animate,interval = 1)
		
		print('done')



m = audioSignal()

def simulation(input, obj):
	obj.initBlank()
	for i in input:
		obj.load(i)
simulation(m.ysBuilder('./FEP-thin-plasma-2-chirp/FEP-thin-plasma-2-chirp-50cm.csv'), m)

