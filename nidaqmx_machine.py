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

def logging(i, ys, sampling_time, line, x_len):
    value = read_daq()
    time.sleep(sampling_time)
    ys.append(value)
    ys = ys[-x_len:]
    line.set_ydata(ys)
    return line