import matplotlib.pyplot as plt
import math

ax1 = plt.subplot(2,2,1)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("pollution (загрязнение)")
plt.axis([0, 10, 1, 2])

ax2 = plt.subplot(2,2,2)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("weight (вес)")
plt.axis([0, 10, 0.1, 0.2])

ax3 = plt.subplot(2,2,3)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("temperature (температура)")
plt.axis([0, 10, 20, 40])

ax4 = plt.subplot(2,2,4)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("weight (вес)")
plt.axis([0, 10, 0.1, 0.2])

#начальный вес
pweight = 0.1
pollution = 1.3
delta_pollution = 0.1
pweight_pollution = 1.3
delta_pweight_pollution = 0.1
#начальное время
ptime = 0.0
ptime1 = 300
pol_ptime = 0.0
pol_ptime1 = 1
#шаг по времени на единицу веса
d_ptime = 0.01
d_pol_ptime = 0.01
_pol_ptime = []
_ptime = []
_pweight = []
_pweight1 = []
_pollution = []
_pollution1 = []
_pweight_pollution = []
_pweight_pollution1 = []

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
while ptime < 500:
    #скорость набора веса - производная; увеличивается
    pvelocity = math.exp((pollution-pweight_pollution)/delta_pweight_pollution)*((1/ptime1)*(math.exp(-ptime/ptime1)))
    pvelocity_pol = 0
    #velocity_pol = (2*3.14/pol_time1)*(delta_pollution*math.cos((2*3.14*pol_time)/pol_time1))
    #скорость набора веса - производная; увеличивается
    velocity = math.exp((temperature-weight_temperature)/delta_weight_temperature)*((1/time1)*(math.exp(-time/time1)))
    velocity_temp = 0
    #velocity_temp = (2*3.14/temp_time1)*(delta_temperature*math.cos((2*3.14*temp_time)/temp_time1))
    #новый вес, который равен сумме предыдущего веса и произведения скорости набора веса на шаг по времени
    pweight += pvelocity * d_ptime
    pollution += pvelocity_pol * d_pol_ptime
    #новый вес, который равен сумме предыдущего веса и произведения скорости набора веса на шаг по времени
    weight += velocity * d_time
    temperature += velocity_temp * d_temp_time
    #новое время как сумма старого и шага по времени
    ptime += d_ptime
    pol_ptime += d_pol_ptime
    print(ptime,pweight,pollution)
    _ptime.append(ptime)
    _pweight.append(pweight)
    _pol_ptime.append(pol_ptime)
    _pollution.append(pollution)
    #_weight1.append(math.exp(time))
    #новое время как сумма старого и шага по времени
    time += d_time
    temp_time += d_temp_time
    print(time,weight,temperature)
    _time.append(time)
    _weight.append(weight)
    _temp_time.append(temp_time)
    _temperature.append(temperature)
    #_weight1.append(math.exp(time))
    plt.sca(ax4)
    plt.plot(time, weight,".b")
    plt.sca(ax3)
    plt.plot(temp_time, temperature, ".r")
    plt.sca(ax2)
    plt.plot(ptime, pweight,".c")
    plt.sca(ax1)
    plt.plot(pol_ptime, pollution, ".g")
    #задержка, с которой рисуется график
    plt.pause(0.01)

#эталонный график со сглаживанием по расстоянию
#plt.plot(_time,_weight1)
#получившийся график без сглаживания по расстоянию
plt.plot(_time,_weight)
plt.plot(_temp_time,_temperature)
plt.plot(_ptime,_pweight)
plt.plot(_pol_ptime,_pollution)
plt.show()