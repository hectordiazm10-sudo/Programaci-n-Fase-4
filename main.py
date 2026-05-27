from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError
)


def registrar_error(mensaje):

    with open(
        "logs.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            mensaje + "\n"
        )


try:

    cliente1 = Cliente(
        "Hector Diaz",
        "12345",
        "hector@gmail.com",
        "300000000"
    )

    sala = ReservaSala(
        "Sala Principal",
        50000
    )

    reserva1 = Reserva(
        cliente1,
        sala,
        2
    )

    costo = reserva1.confirmar()

    print(
        reserva1.mostrar_reserva()
    )

    print(
        "Costo total:",
        costo
    )

except (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError
) as error:

    registrar_error(
        str(error)
    )


try:

    cliente2 = Cliente(
        "",
        "111",
        "correo",
        "300"
    )

except Exception as error:

    registrar_error(
        str(error)
    )


try:

    equipo = AlquilerEquipo(
        "Proyector",
        30000
    )

    reserva2 = Reserva(
        cliente1,
        equipo,
        3
    )

    print(
        reserva2.mostrar_reserva()
    )

except Exception as error:

    registrar_error(
        str(error)
    )


try:

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        80000
    )

    reserva3 = Reserva(
        cliente1,
        asesoria,
        1
    )

    print(
        reserva3.mostrar_reserva()
    )

except Exception as error:

    registrar_error(
        str(error)
    )
