from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):

    def __init__(
        self,
        nombre,
        costo_base,
        disponible=True
    ):

        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "Sala no disponible"
            )

        return self.costo_base * horas

    def descripcion(self):

        return (
            "Servicio de reserva "
            "de sala"
        )


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "Equipo no disponible"
            )

        return self.costo_base * horas

    def descripcion(self):

        return (
            "Servicio de alquiler "
            "de equipos"
        )


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "Asesoría no disponible"
            )

        return self.costo_base * horas

    def descripcion(self):

        return (
            "Servicio de asesoría "
            "especializada"
        )
