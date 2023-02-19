# calculate power of solar power plant in clear sky depends on Sun position
# Sel: Sun elevation
# Saz: Sun azimuth
# Pel: Panel elevation: 90 degree - panel declination: orthogonal on sun panel
# Paz: Panel azimuth
# max_power= maximal power of sun panel: installed PV(kWp or Wp)
# estimate_power= estimate power depends on Sun position in clear sky; theoretical
# explanation look at SP.pdf
from math import *

Sel = 0
Saz = 0
Pel = 0
Paz = 0
max_power = 0
cos_alpha = cos(Sel)*cos(Pel)*cos(Saz-Paz)+sin(Sel)*sin(Pel)
estimate_power = cos_alpha*max_power
