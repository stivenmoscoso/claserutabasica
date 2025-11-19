from archivo_csv import crear_csv
from archivo_txt import agregar

print(crear_csv ("Coders.csv", ["nombre", "Edad"]))

print( agregar ("Coders.csv",["Andres", "26"]))



from archivojson import guardarjson
print(guardarjson ("curso", ["python", "intermedio"]))