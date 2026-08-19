"""
Almacenamiento:
    - mascotas: CSV
    - consultas: JSON
    - vacunas: CSV
    - documentos: binario

"""
import csv
def opener(nombre,tipo_archivo, tipo_apertura):
    a_name = nombre + "." + tipo_archivo
    match tipo_archivo:
        case "csv":
            return open("datos/"+a_name, tipo_apertura, newline="", encoding="utf-8")
        case "json":
            return open("datos/"+a_name, tipo_apertura, enconding = "utf-8", indent = 4, ensure_ascii = False)
        case "binario":
            return open("documentos"+a_name, tipo_archivo)
        case _:
            return None



class Consultas:
    def __init__(self, c_mascota, c_consulta, fecha, motivo, diagnostico, tratamiento, costo):
        self.c_mascota = c_mascota
        self.c_consulta = c_consulta
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostio = diagnostico
        self.tratamiento = tratamiento
        self.costo = costo

class Vacunas:
    def __init__(self, nombre, fecha, prox_dosis, encargado):
        self.nombre = nombre
        self.fecha = fecha
        self.prox_dosis = prox_dosis
        self.encargado = encargado

class Documentos:
    def __init__(self, ruta, nombre):
        self.ruta = ruta
        self.nombre = nombre


class Manager:
    """
    El administrador de los documentos.
    Esta instancia NO debe duplicarse para mantener la integridad del programa.
    """
    def __init__(self):
        self.mascotas = {}
        self.consultas = {}
        self.vacunas = {}
        self.documentos = {}

        self.cargar_mascotas()
        self.cargar_consultas()
        self.cargar_vacunas()
        self.cargar_documentos()

    def cargar_vacunas(self):
        with opener("vacunas", "csv", "r") as o:
            lector = csv.DictReader(o)
            next(lector)
            for linea in lector():
                vac = Vacunas(linea["nombre"], linea["fecha"], linea["proxima dosis"], linea["encargado"])
                self.vacunas[linea[0]] = {vac}


    def cargar_documentos(self): pass