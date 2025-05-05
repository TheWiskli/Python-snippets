from pylab import *

antall_timer = int(input("Hvor mange timer? :"))
r = 1

timer = linspace(0, antall_timer, antall_timer+1)

bakterier = zeros(antall_timer+1)

bakterier[0] = 1

for i in range(1, antall_timer+1):
 bakterier[i] = bakterier[i-1] + r*bakterier[i-1]

plot(timer, bakterier)
xlabel("Tid (timer)")
ylabel("Antall bakterier")
grid()
show()