import matplotlib.pyplot as plt
import math

ax1 = plt.subplot(1,2,1)
plt.title("Загрязнение от времени")
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("pollution (загрязнение)")
plt.axis([0, 90, 0, 90])

ax2 = plt.subplot(1,2,2)
plt.title("Количество особей от времени")
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("fish (ед. особей)")
plt.axis([0, 90, 0, 50])

#начальное количество особей
fish = 35
pollution = 1
delta_pollution = 5
fish_pollution = 1
delta_fish_pollution = 5
#начальное время
time = 1
time1 = 100
pol_time = 1
pol_time1 = 100
deathtime = 1000
#шаг по времени
d_time = 0.1
d_pol_time = 1
_pol_time = []
_time = []
_fish = []
_fish1 = []
_pollution = []
_pollution1 = []
_fish_pollution = []
_fish_pollution1 = []
counter = 0
#рисуем график, пока не прошло 100 суток
while time < 100:
    #скорость сокращения особей - производная; увеличивается
    #velocity = -((fish*math.exp(-time/deathtime))/(deathtime*pollution))
    #velocity = -((fish) / (deathtime * pollution))
    velocity = -((fish) / (deathtime))
    velocity_pol = 0
    deathtime = math.exp((-7*pollution/30)+7)
    fish += velocity * d_time
    pollution += velocity_pol * d_time
    fish_1 = (fish*math.exp(-time/deathtime))
    #новое время как сумма старого и шага по времени
    time += d_time
    pol_time += d_pol_time
    counter += 1
    print(str(counter) + " | " + "time " + str(time) + " | fish " + str(fish) + " | fish_1 " + str(fish_1) + " | pol " + str(pollution) + " | death " + str(deathtime))
    _time.append(time)
    _fish.append(fish)
    _pol_time.append(pol_time)
    _pollution.append(pollution)
    #_weight1.append(math.exp(time))
    plt.sca(ax2)
    plt.plot(time, fish,".b")
    plt.sca(ax1)
    plt.plot(pol_time, pollution, ".g")
    #задержка, с которой рисуется график
    plt.pause(0.5)

plt.plot(_time,_fish)
plt.plot(_pol_time,_pollution)
plt.show()