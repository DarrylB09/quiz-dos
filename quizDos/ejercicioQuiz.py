
Nombre= "Luis Vejarano"
Dias= 7
Salario= 785000

#Calculo de prima
Prima = (Salario * Dias)/360

#Calculo de cesantia
Cesantias = (Salario * Dias) / 360

#Claculo de Interes cesantia
Intereses_cesantias = (Cesantias * 0.12)/Dias

#Calculo de Vacaciones
Vacaciones = (Salario * Dias) / 720

#Calculo de liquidacion
Liquidacion = Prima + Cesantias + Intereses_cesantias + Vacaciones


print(f"""Señor Luis Vejarano para los {Dias} días laborados y
salario ${Salario}, su liquidación se compone así:""")

print(f"Prima: ${Prima:.2f}")
print(f"Cesantía: ${Cesantias:.2f}")
print(f"Intereses cesantía: ${Intereses_cesantias:.2f}")
print(f"Vacaciones: ${Vacaciones:.2f}")
print(f"Liquidación: {Liquidacion:.2f}")


