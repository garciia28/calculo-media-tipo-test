#Datos de entrada --> Preguntas correctas, preguntas incorrectas, preguntas sin contestar
#Procedimiento --> (Preguntas correctas * 0.25) || (Preguntas incorrectas *0.25) || (Preguntas sin contestar * 0 )
#Datos de salida --> Tu nota del tipo test --> notafinal

correcto = int(input("Dime cuántas has acertado: "))
incorrecto = int(input("Dime cuántas has fallado: "))
sin = int(input("Dime cuántas has dejado sin contestar: "))

media = (correcto * 0.5) - (incorrecto * 0.25)

print(f"Tu nota final del tipo test ha sido {media}")
