import matplotlib.pyplot as plt
import numpy as np

#Insetting metoden for A,B og C
print("Skriv inn A, B og C verdiene i annengradslikningen:")
svar = input("a = ")
a = float(svar)
svar = input("b = ")
b = float(svar)
svar = input("c = ")
c = float(svar)


x = np.linspace(-5,5,100)

#Formelen
y = a*x**2+b*x+c

f = np.array([4])
#Grafisk setting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'b', label='ax**2+bx+c', linestyle = 'dotted')
plt.plot(f)
#Ekstra stash på grafen
plt.title('Annengradslikning')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')

#Gridden
plt.grid()

#Visning av grafen
plt.show()