def MinimoComunMultiplo(denom1, denom2, denom3):
    numeroMaximo = max(denom1, denom2, denom3)
    while True:
        if numeroMaximo % denom1 == 0 and numeroMaximo % denom2 == 0 and numeroMaximo % denom3 == 0:
            return numeroMaximo
        numeroMaximo += 1

def operacion(numerador1, numerador2, numerador3, denom1, denom2, denom3):
    numeradores = []
    mcm = MinimoComunMultiplo(denom1, denom2, denom3)

    numerador1 = (mcm // denom1) * numerador1
    numerador2 = (mcm // denom2) * numerador2
    numerador3 = (mcm // denom3) * numerador3

    numeradores =  [numerador1, numerador2, numerador3 ]
    suma = numeradores[0] + numeradores[1] + numeradores[2]

    return suma

numerador1 = 1
numerador2 = 2
numerador3 = 3
denom1 = 3
denom2 = 5
denom3 = 2

Total_Numeradores = operacion(numerador1, numerador2, numerador3, denom1, denom2, denom3)
totalMCM = MinimoComunMultiplo(denom1, denom2, denom3)

print("La respuesta es:", Total_Numeradores, "/", totalMCM)