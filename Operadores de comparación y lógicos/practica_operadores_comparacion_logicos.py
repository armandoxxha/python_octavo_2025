# Operadores de asignación

numero = 20
# Primer operador +=

numero += 30
print(numero)

# Segundo operador -=

numero -= 23
print(numero)

# Tercer operador *=

numero *= 3
print(numero)

# Cuarto operador /=

numero /= 5
print(numero)

# Operadores de comparación 

# Primero comparación > Mayor que
print(300 > 450)
print(300 > 300)
print(69 > 36)

numA = 35
numB = 59
print(numA > numB)

# Segundo comparación < Menor que
print(45 < 89)
print(100 < 78)
print(numA < numB)

# Tercer comparacion  == igual que

print("casa" == "Casa")
print(89 == 79)
print(30 == 30)
print(numA == numB)

# Cuarto comparación != diferente que

print(79 != 79)
print(300 != 78)
print(numA != numB)

# Quinto comparación >= Mayor o igual que
print(200 >= 200)
print(350 >= 499)
print(numA >= numB)

# Sexta comparación <= Menor o igual que
print(35 <= 45)
print(45 <= 45)
print(numA <= numB)

# Operadores logicos
# AND 

print(34 == 56 and 67 <= 89)
print(56 != 78 and 69 == 69)
print("hola" != "Hola" and 100 >= 78)
print(89 < 89 and 67 != 67)

# OR Solo ocupa una comparación verdadera

print(34 == 56 or 67 <= 89)
print(56 != 78 or 69 == 69)
print("hola" != "Hola" or 100 >= 78)
print(89 < 89 or 67 != 67)

# NOT 


print(not(True))
print(190 >= 190 and not(34 != 34))
print(not("Casa" == "casa") and 67 != 89)