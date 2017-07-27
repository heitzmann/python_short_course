# Import necessary modules
import numpy
from matplotlib import pyplot

# Waveguide lengths (cm)
x = [0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0]

# Single-mode waveguide insertion loss (dB)
y1 = [13.31181, 13.1782, 14.01734,
      16.2383, 16.3154, 16.068,
      19.9276, 20.0151, 21.6095]

# Single-mode waveguide insertion loss (dB)
y2 = [23.64875, 22.815, 23.9887,
      27.25228, 26.7654, 26.5463,
      33.33211, 32.786, 34.0234]

c1, v1 = numpy.polyfit(x, y1, 1, cov=True)
c2, v2 = numpy.polyfit(x, y2, 1, cov=True)

print('''Single-mode:
  Propagation loss: ({:.1f} +/- {:.1f}) dB/cm
  Coupling loss: ({:.1f} +/- {:.1f}) dB

Multimode:
  Propagation loss: ({:.1f} +/- {:.1f}) dB/cm
  Coupling loss: ({:.1f} +/- {:.1f}) dB
'''.format(c1[0], v1[0, 0]**0.5,
           c1[1], v1[1, 1]**0.5,
           c2[0], v2[0, 0]**0.5,
           c2[1], v2[1, 1]**0.5))

fit_x = numpy.array([0, 2.0])
fit_y1 = c1[0] * fit_x + c1[1]
fit_y2 = c2[0] * fit_x + c2[1]

fig, ax = pyplot.subplots(1, 1, figsize=(5.5, 4)) # rows × cols, size in inches

ax.plot(x, y1, 'o', label='Single-mode data')
ax.plot(fit_x, fit_y1, label='y = {0[0]:.1f}x + {0[1]:.1f}'.format(c1))

ax.plot(x, y2, 's', label='Multimode data')
ax.plot(fit_x, fit_y2, '--', label='y = {0[0]:.1f}x + {0[1]:.1f}'.format(c2))

ax.legend()

ax.set_xlabel('Length (cm)')
ax.set_ylabel('Insertion Loss (dB)')

ax.grid()

# Other useful formats: svg, eps, png
fig.savefig('figure.pdf')

pyplot.show()
