def line():
	import math


	# Entrada de datos
	A = float(input("Ingrese el coeficiente A: "))
	B = float(input("Ingrese el coeficiente B: "))
	X1 = float(input("Ingrese el coeficiente X1: "))
	X2 = float(input("Ingrese el coeficiente X2: "))

	# Mostrar los valores ingresados
	print(f"El coeficiente A de su ecuación de la recta es: {A}")
	print(f"El coeficiente B de su ecuación de la recta es: {B}")
	print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
	print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

	# Mostrar la ecuación de la recta
	print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}\n")

	# Cálculo de las coordenadas Y
	Y1 = A * X1 + B
	Y2 = A * X2 + B

	print(f"Dados los siguientes puntos:\n\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})")

	# Calcular la distancia entre los puntos
	distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
	print(f"\nLa distancia entre ellos es: {distancia}")

