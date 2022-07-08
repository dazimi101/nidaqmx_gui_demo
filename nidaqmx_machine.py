import nidaqmx as mx
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def read_daq():
    task = mx.Task()
    task.ai_channels.add_ai_voltage_chan("TestDev/ai0")
    task.start()
    value = task.read()
    task.stop()
    task.close()
    return value

sampling_time = 1
n = 10
x_len = n
t_min = 0; t_max =.1
y_range = [t_min, t_max]

fig = plt.figure()
ax = fig.add_subplot(111)
xs = list(range(0, n))
ys = [0]*x_len
ax.set_ylim(y_range)
line, = ax.plot(xs, ys)
plt.grid()

def logging(i, ys):
    value = read_daq()
    time.sleep(sampling_time)
    ys.append(value)
    ys = ys[-x_len:]
    line.set_ydata(ys)
    return line

ani = animation.FuncAnimation(fig, logging, fargs=(ys,), interval=100)

plt.show()
