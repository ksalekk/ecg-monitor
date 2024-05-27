from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='ecg_monitor script')
parser.add_argument('fname', type=str, help='File path')
parser.add_argument('-fs', type=int, help='Sampling frequency; default 1000Hz', default=1000)
parser.add_argument('--delimiter', type=str, help='Columns delimiter; default \',\'', default=';')
parser.add_argument('-tstart', type=int, help='Signal recording start time in seconds; default 0', default=0)
parser.add_argument('-tstop', type=int, help='Signal recording stop time in seconds; default signal duration', default=0)
parser.add_argument('--lowcut', type=float, help='Butterworth filter lowcut frequency [Hz]; default 0.5Hz', default=0.5)
parser.add_argument('--highcut', type=float, help='Butterworth filter highcut frequency [Hz]; default 150Hz', default=150)
parser.add_argument('-dt', type=int, help='Window displaying time in seconds; default 5s', default=5)
args = parser.parse_args()

sensor_data = np.loadtxt(args.fname, delimiter=args.delimiter)
args.tstop = int(len(sensor_data)/args.fs) if args.tstop == 0 else args.tstop
t = sensor_data[args.tstart * args.fs : args.tstop*args.fs, 0]
ecg_raw = sensor_data[args.tstart * args.fs : args.tstop*args.fs, 1]

nyq = args.fs/2
sos = butter(5, [args.lowcut/nyq, args.highcut/nyq], 'band', output='sos')
ecg_filtered = sosfiltfilt(sos, ecg_raw)

# ax: plt.AxLine | plt.Axes
fig, ax = plt.subplots()
line, = ax.plot(t, ecg_filtered)

ax.set(title="Filtered ECG Signal",
       xlabel="Time [s]",
       ylabel="Voltage [mV]")
ax.set_ylim(-0.1, 0.3)
plt.grid()

def update_dynamic(frame):
    line.set_data(t[:frame*100], ecg_filtered[:frame*100])
    if frame % 50 == 0:
        ax.set_xlim(args.tstart + frame/10, args.tstart + frame/10 + args.dt)

ax.set_xlim(args.tstart, args.tstart + 5)
my_animation = FuncAnimation(fig, update_dynamic, frames=3000, interval=100)
plt.show()
