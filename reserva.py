from excepciones import ReservaError


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        horas
    ):

        if horas <= 0:
            raise ReservaError(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        costo = self.servicio.calcular_costo(
            self.horas
        )

        self.estado = "Confirmada"

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"Reserva confirmada - "
                f"{self.cliente.nombre} - "
                f"{self.servicio.nombre}\n"
            )

        return costo

    def cancelar(self):

        self.estado = "Cancelada"

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"Reserva cancelada - "
                f"{self.cliente.nombre}\n"
            )

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
