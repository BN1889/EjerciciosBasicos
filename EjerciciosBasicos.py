# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("Hola Mundo")

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

Saludo = ("Hola Mundo!!")
print(Saludo)

# Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
# donde <nombre> es el nombre que el usuario haya introducido.

Nombre = input("Escribe tu nombre por favor  ")
print("Hola " + Nombre + " hoy es un gran dia")

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2*5)**2

Operacion = ((3+2)/(2*5))**2
print(Operacion)

# Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu pago es", paga)
 
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

Nombre = input("Introduce tu nombre por favor: ")
Entero = int(input("Introduce un nro entero: "))
print((Nombre + "\n") * int(Entero))

# Escribir un programa que pregunte el nombre completo del usuario en la consola y 
# después muestre por pantalla el nombre completo del usuario tres veces,
# una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

Nombre_completo = input('Introduce tu nombre completo por favor: ')
print(Nombre_completo.lower())
print(Nombre_completo.upper())
print(Nombre_completo.title())

# Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

Name = input('escribi tu nombre: ')
print(Name.upper() + " tiene " + str(len(Name)) + " letras")

# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

Frase = input('introduce una frase: ')
print(Frase [::-1])