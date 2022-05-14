import numpy as np 
import matplotlib.pyplot as plt
with open(src_plot_pos.dat) as text:
    data = text.read().replace('\n', ',').replace('        ',',').split(',')
    print(data)
    text.close()
length = int((len(data)-1)/2)
x_data = [0]*length
y_data = [0]*length
j=0
for i in range(1,len(data),2):
    x_data[j] = data[i]
    j=j+1
j=0
for i in range(2,len(data),2):
    y_data[j] = data[i]
    j=j+1

delta = 0 - int(data[0])

time = [0]*length
for i in range(len(time)):
     delta = delta + int(data[0])
     time[i] = delta

delta = 0 - int(data[0])
vtime = [0]*(length-2)
for i in range(len(vtime)):
     delta = delta + int(data[0])
     vtime[i] = delta

xvelocity = [0]*(length-2)
yvelocity = [0]*(length-2)
for i in range(len(xvelocity)):
    xvelocity[i] = (float(x_data[i+1])-float(x_data[i]))/delta
for i in range(len(yvelocity)):
    yvelocity[i] = (float(y_data[i+1])-float(y_data[i]))/delta
print(xvelocity)
print(yvelocity)
plt.plot(vtime,xvelocity)
plt.title("x velocity over time")
plt.xlabel("time")
plt.ylabel("x_velocity")
plt.show()

plt.plot(vtime,yvelocity)
plt.title("y velocity over time")
plt.xlabel("time")
plt.ylabel("y_velocity")
plt.show()

plt.plot(time,x_data)
plt.title("x position graph")
plt.xlabel("time")
plt.ylabel("x_position")
plt.show()

plt.plot(time,y_data)
plt.title("y position graph")
plt.xlabel("time")
plt.ylabel("y_position")
plt.show()