from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(
        self,
        nombre,
        documento,
        correo,
        telefono
    ):

        if not nombre:
            raise ClienteInvalidoError(
                "El nombre es obligatorio"
            )

        if not documento:
            raise ClienteInvalidoError(
                "Documento obligatorio"
            )

        if "@" not in correo:
            raise ClienteInvalidoError(
                "Correo inválido"
            )

        if not telefono:
            raise ClienteInvalidoError(
                "Teléfono obligatorio"
            )

        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Correo: {self.correo}"
        )
