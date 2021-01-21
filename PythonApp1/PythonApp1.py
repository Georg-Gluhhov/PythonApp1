
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np



# Нахождение коардинат 
x = np.arange(0, 10, 1)
y1 = (2/27)*x**2-3

x1= np.arange(-10,1,1)
y2 = (0.04) * x1**2 - 3

x2= np.arange(-9,-2,1)
y3 = (2/9) * ((x2+6)**2)+ 1

x3= np.arange(-3,10,1)
y4 =-1*(1/12)*((x3-3)**2)+6

x4= np.arange(5,9,1)
y5= (1/9)*((x4-5)**2)+2

x5= np.arange(5,9,1)
y6= (1/8)*((x5-7)**2)+1.5

x6= np.arange(-13,-8,1)
y7= -1*(0.75)*((x6+11)**2)+6

x7= np.arange(-15,-12,1)
y8= -1*(0.5)*((x7+13)**2)+3

x8= np.arange(-15,-9,1)
y9= [1] * len(x8)

x9= np.arange(3,4,1)
y10= [3] * len(x9)
# Построение графика
plt.subplots()
plt.tick_params(axis="x",direction="in",length=2,width=3,color="red", labelsize=6)
plt.title("кит") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y1, y2")    # ось ординат
plt.grid(axis="y",alpha=0.5, linewidth=3)  
plt.grid(axis="x",alpha=0.5, linewidth=3)
plt.grid(True)# включение отображение сетки
plt.plot(x,y1,x1,y2,x2,y3,x3,y4,x4,y5,x5,y6,x6,y7,x7,y8,x8,y9,x9,y10)  # построение графика
plt.savefig("my_image.png")
plt.show()


x1= np.arange(-12,13,1)
y2 = (-1/18)*x1**2+12

x2= np.arange(-4,5,1)
y3 = (-1/8)*x2**2+6

x3= np.arange(-12,-3,1)
y4 = (-1/8)*(x3+8)**2+6

x4= np.arange(4,13,1)
y5= (-1/8)*(x4-8)**2+6

x5= np.arange(-4,1,1)
y6= 2*(x5+3)**2-9

x6= np.arange(-4,1,1)
y7= (x6+3)**2-10

plt.subplots()
plt.tick_params(axis="x",direction="in",length=2,width=3,color="red", labelsize=6)
plt.title("зонт") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y1, y2")    # ось ординат
plt.grid(axis="y",alpha=0.5, linewidth=3)  
plt.grid(axis="x",alpha=0.5, linewidth=3)
plt.grid(True)# включение отображение сетки
plt.plot(x1,y2,x2,y3,x3,y4,x4,y5,x5,y6,x6,y7)  # построение графика
plt.savefig("my_image.png")
plt.show()

fail=open(r"graphic.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
title = "Данные о коронавирусе в эстонии на 19.01.2021"
plt.grid(True)
color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)
plt.show()