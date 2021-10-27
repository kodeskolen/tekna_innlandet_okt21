temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]

# Manuell løsning
maks = -100
for temp in temperaturer:
    if temp > maks:
        maks = temp       
print(f"Den høyeste temperaturen var {maks} grader")

# Innebygget løsning
print(f"Den høyeste temperaturen var {max(temperaturer)}")




