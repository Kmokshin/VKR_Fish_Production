import matplotlib.pyplot as plt
import math

ax1 = plt.subplot(1,2,1)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("pollution (загрязнение)")
plt.axis([0, 90, 0, 90])

ax2 = plt.subplot(1,2,2)
plt.grid()
plt.xlabel("time (время в сутках)")
plt.ylabel("quantity (количество рыб)")
plt.axis([0, 90, 0, 50])

pollution = 1
fish = 35
fish_initial = 35
time = 1
d_time = 0.1
_time = []
_fish = []
_pollution = []

while time < 100:
    deathtime = math.exp((-7 * pollution / 30) + 7)
    velocity = -((fish) / (deathtime))
    velocity_pol = 1
    fish += velocity * d_time
    fish_1 = (fish_initial * math.exp(-time / deathtime))
    pollution += velocity_pol * d_time
    time += d_time
    print("time " + str(time) + " | fish " + str(fish) + " | fish_1 " + str(fish_1) + " | pol " + str(pollution) + " | death " + str(deathtime))
    _time.append(time)
    _fish.append(fish)
    _pollution.append(pollution)
    _time.append(time)
    plt.sca(ax2)
    plt.plot(time, fish,".b")
    plt.sca(ax1)
    plt.plot(time, pollution, ".g")
    plt.pause(0.001)

plt.plot(_time,_fish)
plt.plot(_time,_pollution)
plt.show()