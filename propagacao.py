# Import necessary modules
import numpy
from matplotlib import pyplot

# Wavegu# Waveguide lengths (cm)
x_exp = [0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0]

# Single-mode waveguide insertion loss (dB)
y_sm = [13.312, 13.178, 14.017,
        16.238, 16.315, 16.068,
        19.928, 20.015, 21.610]

# Multimode waveguide insertion loss (dB)
y_mm = [23.649, 22.815, 23.989,
        27.252, 26.765, 26.546,
        33.332, 32.786, 34.023]

c_sm, v_sm = numpy.polyfit(x_exp, y_sm, 1, cov=True)
c_mm, v_mm = numpy.polyfit(x_exp, y_mm, 1, cov=True)

print('''Single-mode:
  Propagation loss: ({:.1f} +/- {:.1f}) dB/cm
  Coupling loss: ({:.1f} +/- {:.1f}) dB

Multimode:
  Propagation loss: ({:.1f} +/- {:.1f}) dB/cm
  Coupling loss: ({:.1f} +/- {:.1f}) dB
'''.format(c_sm[0], v_sm[0, 0]**0.5,
           c_sm[1], v_sm[1, 1]**0.5,
           c_mm[0], v_mm[0, 0]**0.5,
           c_mm[1], v_mm[1, 1]**0.5))

x_fit = numpy.array([0, 2.0])
y_sm_fit = c_sm[0] * x_fit + c_sm[1]
y_mm_fit = c_mm[0] * x_fit + c_mm[1]

fig, ax = pyplot.subplots(1, 1, figsize=(5.5, 4)) # rows × cols, size in inches

ax.plot(x_exp, y_sm, 'o', label='Single-mode data')
ax.plot(x_fit, y_sm_fit, label='y = {0[0]:.1f}x + {0[1]:.1f}'.format(c_sm))

ax.plot(x_exp, y_mm, 's', label='Multimode data')
ax.plot(x_fit, y_mm_fit, '--', label='y = {0[0]:.1f}x + {0[1]:.1f}'.format(c_mm))

ax.legend()

ax.set_xlabel('Length (cm)')
ax.set_ylabel('Insertion Loss (dB)')

ax.grid()

# Other useful formats: svg, eps, png
fig.savefig('figure.pdf')

pyplot.show()
