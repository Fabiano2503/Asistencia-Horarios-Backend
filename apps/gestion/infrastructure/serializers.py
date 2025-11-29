# app/infrastructure/serializers.py
def practicante_to_dict(p):
    return {
        "id": p.id,
        "nombre": f"{p.nombre} {p.apellido}",
        "servidor": p.servidor or "Sin asignar",
        "horario_completo": len(p.horarios) >= 5
    }

def horario_to_dict(horarios):
    if isinstance(horarios, list):
        return [{"id": h.get("id"), "dia": h.get("dia")} for h in horarios]
    return []

def recuperacion_to_dict(r):
    return {
        "id": r.id,
        "practicante": f"{r.practicante.nombre} {r.practicante.apellido}",
        "fecha_declarada": r.fecha_recuperacion,
        "motivo": r.motivo or "Sin motivo",
        "evidencia_url": f"/media/{r.evidencia}"
    }