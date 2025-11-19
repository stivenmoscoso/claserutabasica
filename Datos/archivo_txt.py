def crearArchivo(nombre):
    with open(nombre, "w") as file:
        file.write("Archivo creado")
        return f"Archivo{nombre} creado correctamente"
    
def agregar (nombre, text):
    with open(nombre, "a") as file: 
        file.write(text)    
        return "agregar"
    
def leer_archivo (nombre):  
    with open(nombre, "r") as file:
        return file.read()