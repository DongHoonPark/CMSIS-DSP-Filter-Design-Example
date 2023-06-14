import numpy as np
import cmsisdsp_filtering as cf;
from scipy.signal import iirfilter
from scipy import signal
import matplotlib.pyplot as plt

fs = 1000 # sampling frequency
fc = 100  # cut-off frequency

wp = fc/fs

b, a = iirfilter(N=2, Wn=[wp], btype='lowpass', ftype='butter', analog=False) #design digital iir filter

coeff = list(b)+list(-a[1:])

filt = cf.arm_biquad_casd_df1_inst_f32()
cf.arm_biquad_cascade_df1_init_f32(filt, 1, coeff, np.zeros(4))

t_step = 0.2
n_step = int(fs * t_step +1)
x = np.linspace(0, t_step, n_step)
y_in = np.ones_like(x) 
y_out = np.zeros_like(y_in)

for i, _ in enumerate(y_in):
    y_out[i] = cf.arm_biquad_cascade_df1_f32(filt, [y_in[i]])

plt.plot(x, y_in)
plt.plot(x, y_out)

x, y_scipy = signal.dstep((b,a,1/fs), n=n_step)
plt.plot(x, np.reshape(y_scipy, x.shape))
plt.show()
pass