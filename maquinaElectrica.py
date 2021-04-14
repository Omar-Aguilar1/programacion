from maquina import Maquina


class maquinaElectrica(Maquina):
    MIN_VOLTAJE: int = 10
    MAX_VOLTAJE: int = 400
    DEFAULT_VOLTAJE: int = MIN_VOLTAJE
    MIN_POTENCIA_ELECTRICA: float = 700.00

    def __init__(self, marca: str, modelo: str, voltaje=None, potenciaElectrica=None):
        super().__init__(marca, modelo)
        self._voltaje: int = maquinaElectrica.MIN_VOLTAJE if voltaje is None else voltaje
        self._potenciaElectrica: float = maquinaElectrica.MIN_POTENCIA_ELECTRICA if potenciaElectrica is None else potenciaElectrica
