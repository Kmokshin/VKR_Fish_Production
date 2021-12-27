import matplotlib.pyplot as plt
import math

ax1 = plt.subplot(1,2,1)
plt.grid()
plt.axis([0, 500, 0, 3])
plt.xlabel("x (время)")
plt.ylabel("y (масса)")

ax2 = plt.subplot(1,2,2)
plt.grid()
plt.axis([0, 500, 25, 35])
plt.xlabel("x (время)")
plt.ylabel("t (температура)")

#начальная масса, с которой начинается рост
y = 0.1
t = 30
d_t = 5
t1 = t + d_t
tg = 30
d_tg = 5
#начальное время в сутках
x = 0.0
x_t = 0.0
x1 = 300
x1_t = 1
#шаг по времени на единицу массы
dx = 1
dx_t = 1
_x = []
_x_t = []
_y = []
_t = []
_y1 = []
_t1 = []
test_z = 0
print("----------------------------------------------------------")
print("Время: | Масса рыбы: | Температура воды: |")
print("----------------------------------------------------------")

while x < 500:
    #скорость - производная
    #v = (1/x1)*(math.exp(-x/x1))
    v = math.exp((t-tg)/d_tg)*((1/x1)*(math.exp(-x/x1)))
    v1 = (2*3.14/x1_t)*(d_t*math.cos((2*3.14*x_t)/x1_t))
    #v1 = 0
    #v = (3.14/x1)*(math.sin(3.14*(x/x1)))
    #новая масса, которая равна сумме предыдущее и произведения скорости роста на шаг по времени
    y += v * dx
    t += v1 * dx_t
    if x == 2*x1:
        break
    #новое время как сумма старого и шага по времени
    x += dx
    x_t += dx_t
    print(str(x) + " | ",str(y) + " | ",str(t) + " | ")
    print("----------------------------------------------------------")
    _x.append(x)
    _y.append(y)
    _x_t.append(x_t)
    _t.append(t)
    test_z = (3.14*(x/x1))
    _y1.append(1.1 - (math.exp(-x/x1)))
    _t1.append(math.exp(x_t))
    plt.sca(ax1)
    plt.plot(x, y,"*b")
    #задержка, с которой рисуется график
    #plt.pause(0.001)
    plt.sca(ax2)
    plt.plot(x_t, t,"*r")
    #задержка, с которой рисуется график
    #plt.pause(0.001)
plt.sca(ax1)
#эталонный график
plt.plot(_x,_y1)
#получившийся график
plt.plot(_x,_y)
plt.sca(ax2)
#эталонный график
plt.plot(_x_t,_t1)
#получившийся график
plt.plot(_x_t,_t)
plt.show()