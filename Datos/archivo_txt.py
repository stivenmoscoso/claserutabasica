import csv


def crearArchivo(nombre):
    with open(nombre, "w") as file:
        file.write("Archivo creado")
        return f"Archivo{nombre} creado correctamente"
          
    

def agregar (nombre, text):
    with open(nombre, "a",newline="") as file: 
        file.write(text)    
        return "agregar"
    
def leer_archivo (nombre):  
    with open(nombre, "r") as file:
        return file.read()

def agregarlinea(nombre, datos):   
    with open (nombre, "a", newline="") as file:    
        write = csv.writer(file)
        write.writerow(datos)