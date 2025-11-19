import csv

def crear_csv (nombre, encabezado):
    with open(nombre, "w", newline="") as f:
        write = csv.writer(f)   
        write.writerow(encabezado)