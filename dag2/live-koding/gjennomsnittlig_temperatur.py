temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]

# Manuell løsning
total = 0
for temp in temperaturer:
    total += temp
    
gjennomsnitt = total/len(temperaturer)
print(f"Gjennomsnittstemperaturen er {gjennomsnitt:.1f} grader")


# Innebygget
gjennomsnitt = sum(temperaturer)/len(temperaturer)
print(round(gjennomsnitt, 1))

# Kan importeres
from statistics import mean, stdev, variance

print(mean(temperaturer))
print(f"Standardavviket er {stdev(temperaturer)}")
print(f"Variansen er {variance(temperaturer)}")