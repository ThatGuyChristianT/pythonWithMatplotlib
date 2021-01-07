##Matplotlib

import matplotlib.pyplot as plt
import numpy as np

#Instantiating two numpy Arrays
x = np.linspace(0,5,11)
y = x ** 2

#Functional method
plt.plot(x,y)
#plt.show() #Prints the plot

#Adding x and y label
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('Functional Title')

#Creates multi-plot on the same canvas
plt.subplot(1,2,1)#number of rows, column, and plot number being referenced
plt.plot(x,y, 'r')

plt.subplot(1,2,2)
plt.plot(y,x, 'b')

#plt.show()

#Re-creating the first plot created using Object Oriented function
figure = plt.figure() #Note: Axes can be added
axes = figure.add_axes([0.1,0.1,0.8,0.8 ]) #Needs to pass a list,  #Left, bottom, width, and height
axes.plot(x,y)
#Adding label of x and y axis
axes.set_xlabel('X-Label')
axes.set_ylabel('Y-Label')
#plt.show()

#Creation of another figure object
fig = plt.figure() #Empty canvas
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #Left, bottom, width, and height
axes1.plot(x,y)
#Second axes will be nested inside the first axes
axes2 = fig.add_axes([0.2,0.50,0.4,0.3])
axes2.plot(y,x)
#plt.show()

#Creating sub-plots using OOP
fig, axes = plt.subplots(nrows  =3, ncols =3) #Rows and columns kargs
#Note, axes is a list of matplotlib axes


#Adding padding between the plots so that the texts won't overlap
plt.tight_layout() #Always recommended to put on the end of each plotting statements
#plt.show()

##Figure Aspect Ratio and DPI

fig,axes = plt.subplots(nrows = 2, ncols = 1, figsize=(8,2))#figsize = Width and height | dpi = pixel per inch
axes[0].plot(x,y)
axes[1].plot(x,y)
plt.tight_layout()
#plt.show()

#Saving a figure to a file
#fig.savefig('my_picture.jpg', dpi = 200) #Automatically saves figure. Can also increase DPI for more detail.

##Legends

#Recreation of object
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = 'X Squared') #Label is an idenfier going to be used for the legend
ax.plot(x,x**3, label = 'X Cubed')
ax.legend(loc = 0)#loc can be passed a parameter to move the legend around the plot.
plt.show()
