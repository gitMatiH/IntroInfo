'''
Se ingresa el código de tipo de llamada: 
1. Local 
2. Interurbana 
3. Internacional 
y la duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local,
$0.40 para la llamada interurbana y $1.05 para la llamada internacional, diseñar un
algoritmo que permita calcular el monto a pagar por dicha llamada.
'''

precio_local		= float(0.25)
precio_interurbano	= float(0.40)
precio_internacional	= float(1.05)

codigo = int(input("1: Local\n"
				   "2: Interurbana\n"
				   "3: Internacional\n"
				   "Ingrese código: "))
