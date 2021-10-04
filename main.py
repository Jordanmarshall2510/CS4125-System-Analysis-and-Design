import threading
from Distribution.battery import *
from World.environment import *

env=environment()

th = threading.Thread(target=env.start)
th.start()

print('before')
time.sleep(2)
print('after')
env.stop()
time.sleep(0.1)

env.setTime('1.4.2100, 00:00:00')
print(env.getTime())
print(env.getSeason())
print(env.getWeather())
env.setTime('1.7.2100, 00:00:00')
print(env.getTime())
print(env.getSeason())
print(env.getWeather())
env.setTime('1.10.2100, 00:00:00')
print(env.getTime())
print(env.getSeason())
print(env.getWeather())