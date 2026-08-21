"""
Almacenamiento:
    - mascotas: CSV
    - consultas: JSON
    - vacunas: CSV
    - documentos: binario

"""

"""
    nombre,apellido,fecha,registro
"""
import csv

def opener(nombre,tipo_archivo, tipo_apertura):
    a_name = nombre + "." + tipo_archivo
    match tipo_archivo:
        case "csv":
            return open(f"datos/{a_name}", tipo_apertura, newline="", encoding="utf-8")
        case "json":
            return open(f"datos/{a_name}", tipo_apertura, encoding = "utf-8", indent = 4, ensure_ascii = False)
        case "binario":
            return open(f"documentos/{a_name}", tipo_archivo)
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
    def __init__(self, extension, nombre):
        self.extension = extension
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


    def cargar_vacunas(self):
        try: #caso especial: no hay doc para vacunas, así que se crea así bien artesanal
            with opener("vacunas", "csv", "x") as o:
                lector = csv.DictReader(o)
                return False
        except Exception as e:
            pass

        # Ahora sí, se abre el doc vacunas
        with opener("vacunas", "csv", "r") as o:
            lector = csv.DictReader(o)
            next(lector)
            for linea in lector:
                vac = Vacunas(linea["nombre"], linea["fecha"], linea["proxima dosis"], linea["encargado"])
                self.vacunas[linea[0]] = {vac}
            return False


    def guardar_vacunas(self):
        if not self.vacunas:
            return False
        headers = ["nombre", "fecha", "proxima dosis", "encargado"]
        with opener("vacunas", "csv", "w") as o:
            escritor = csv.DictWriter(o, headers)
            escritor.writeheader()
            for vac in self.vacunas.values():
                escritor.writerow(vac)
            return True


    def cargar_documento(self, nombre, tipo):
        try:
            with opener(nombre, tipo, "rb") as o:
                info = o.read()
                self.documentos[nombre] = Documentos(tipo, nombre)
                return True
        except:
            pass
        with opener(nombre, tipo, "wb") as o:
            info = o.read()
            return False


class Operador:
    def __init__(self):
        self.manejador = Manager()

    def
func = Operador()

# ---------- MENÚ CHIDO ----------
while True:
    print("----------SISTEMA VETERINARIA----------\n1. Registrar Mascota\n2. Mostrar mascotas\n3. Buscar mascota\n4. Registrar consulta\n5. Historial de consultas\n6. Registrar vacuna\n7. Consultar vacunas de una mascota\n8. Añadir archivo a mascota\n9. Resumen del sistema\n10. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":pass
        case "2":pass
        case "3":pass
        case "4":pass
        case "5":pass
        case "6":pass
        case "7":pass
        case "8":pass
        case "9":pass
        case "10":
            print("Saliendo...")
            break

        case _:
            print("Opción inválida")