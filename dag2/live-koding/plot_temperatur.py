temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]

# Importer "alle" funksjoner i biblioteket matplotlib.pyplot
from matplotlib.pyplot import *

# Plot en liste med verdier mot sin egen indeks
plot(temperaturer, 'o-')

# Sett navn på plott og aksene
xlabel('Klokkeslett')
ylabel('Temperatur')
title('Et døgn i Oslo')

# Sett grenser på x- og y-aksen
xlim(0, 23)
ylim(-25, 0)

# Legg på et rutenett
grid()

# Vis frem endelig plott
show()