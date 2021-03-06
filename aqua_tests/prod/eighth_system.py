import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker

#ax1 = plt.subplot(1,2,1)
#plt.grid()
#plt.xlabel("time (время в сутках)")
#plt.ylabel("temperature (температура)")
#plt.axis([0, 10, 20, 40])

ax2 = plt.subplot(1,1,1)
plt.grid()
plt.title("Изменение веса рыбы при изменяющейся температуре от 22°C до 32°C")
plt.xlabel("time (время в сутках)")
plt.ylabel("weight (вес)")
plt.axis([0, 270, 0.1, 2])
ax2.xaxis.set_major_locator(ticker.MultipleLocator(7))

#начальный вес
weight = 0.1
temperature = 27
delta_temperature = 5
weight_temperature = 27
delta_weight_temperature = 5
#начальное время
time = 0.0
time1 = 300
temp_time = 0.0
temp_time1 = 1
#шаг по времени на единицу веса
d_time = 0.01
d_temp_time = 0.01
_temp_time = []
_time = []
_weight = []
_weight1 = []
_temperature = []
_temperature1 = []
_weight_temperature = []
_weight_temperature1 = []
#рисуем график, пока не прошло 500 суток
while time < 270:
    #скорость набора веса - производная; увеличивается
    velocity = math.exp((temperature-weight_temperature)/delta_weight_temperature)*((1/time1)*(math.exp(-time/time1)))
    velocity_temp = (2*3.14/temp_time1)*(delta_temperature*math.cos((2*3.14*temp_time)/temp_time1))
    #новый вес, который равен сумме предыдущего веса и произведения скорости набора веса на шаг по времени
    weight += velocity * d_time
    temperature += velocity_temp * d_temp_time
    #новое время как сумма старого и шага по времени
    time += d_time
    temp_time += d_temp_time
    print(time,weight,temperature)
    _time.append(time)
    _weight.append(weight)
    _temp_time.append(temp_time)
    _temperature.append(temperature)
    #_weight1.append(math.exp(time))
    plt.sca(ax2)
    plt.plot(time, weight,".b")
    #plt.sca(ax1)
    plt.plot(temp_time, temperature, ".r")
    #задержка, с которой рисуется график
    #plt.pause(0.01)

#эталонный график со сглаживанием по расстоянию
#plt.plot(_time,_weight1)
#получившийся график без сглаживания по расстоянию
plt.plot(_time,_weight)
#plt.plot(_temp_time,_temperature)
plt.show()