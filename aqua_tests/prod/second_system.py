import matplotlib.pyplot as plt
import math

plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("weight (вес)")
plt.axis([0, 500, 0, 3.1])

#начальный вес
weight = 0.1
#начальное время
time = 0.0
time1 = 300
#шаг по времени на единицу веса
d_time = 1
_time = []
_weight = []
_weight1 = []
#рисуем график, пока не прошло 500 суток
while time < 500:
    #скорость набора веса - производная; увеличивается
    velocity = (1/time1)*(math.exp(-time/time1))
    #новый вес, который равен сумме предыдущего веса и произведения скорости набора веса на шаг по времени
    weight += velocity * d_time
    #новое время как сумма старого и шага по времени
    time += d_time
    print(time,weight)
    _time.append(time)
    _weight.append(weight)
    #_weight1.append(math.exp(time))
    plt.plot(time,weight,".b")
    #задержка, с которой рисуется график
    plt.pause(0.01)

#эталонный график со сглаживанием по расстоянию
#plt.plot(_time,_weight1)
#получившийся график без сглаживания по расстоянию
plt.plot(_time,_weight)
plt.show()