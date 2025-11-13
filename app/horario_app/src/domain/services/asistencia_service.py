from datetime import datetime


class AsistenciaService:
    @staticmethod
    def calcular_estado(hora_entrada: str, hora_inicio: str, hora_fin: str) -> str:
        try:
            entrada = datetime.strptime(hora_entrada, "%H:%M")
            inicio = datetime.strptime(hora_inicio, "%H:%M")
            fin = datetime.strptime(hora_fin, "%H:%M")
            if inicio <= entrada <= fin:
                return "aprobado"
            return "pendiente"
        except:
            return "pendiente"

        