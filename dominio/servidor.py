class Servidor:
    def __init__(self, nombre, cpu, ram, estado):
        self._nombre = nombre
        self.cpu = cpu
        self.ram = ram
        if estado in ("activo", "inactivo", "mantenimiento"):
            self._estado = estado
        else:
            raise ValueError("Estado invalido")

    def __eq__(self, otro):
        if not isinstance(otro, Servidor):
            return NotImplemented
        return self.nombre == otro.nombre

    def __str__(self):
        return (f"Nombre: {self._nombre}\nCPU: {self._cpu}\nEstado: {self._estado}\n")

    @property
    def nombre(self):
        return self._nombre

    @property
    def estado(self):
        return self._estado

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, numero):
        if type(numero) is int:
            if numero > 0:
                self._cpu = numero
            else:
                raise ValueError("El numero tiene que ser mayor que cero")
        elif isinstance(numero, str):
                try:
                    num = int(numero)
                except ValueError:
                    raise ValueError("Tipo de dato no permitido")
                else:
                    if num > 0:
                        self._cpu = num
                    else:
                        raise ValueError("El numero tiene que ser mayor que cero")
        else:
            raise TypeError("Tipo de dato no permitido")

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, numero):
        if type(numero) is int:
            if numero > 0:
                self._ram = numero
            else:
                raise ValueError("El numero tiene que ser mayor que cero")
        else:
            raise ValueError("Tipo de dato no permitido")

    def cambiar_nombre(self, nombre):
        if nombre.strip != "":
            try: 
                int(nombre)
            except ValueError:
                raise ValueError("El nombre no puede ser solo un numero")
            else:
                self._nombre = nombre
        else:
            raise ValueError("No se puede ingresar un nombre vacio")
    
    def desactivar(self):
        self._estado = "inactivo"

    def activar(self):
        self._estado = "activo"

    def poner_en_mantemiento(self):
        self._estado = "mantenimiento"
