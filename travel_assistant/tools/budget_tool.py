
def calculate_budget(
    transport: float,
    accommodation: float,
    food: float,
    activities: float,
    days: int
) -> dict:
    """Calcula el presupuesto total estimado de un viaje."""

    if days < 1:
        return {"error": "La duración del viaje debe ser de al menos un día."}

    expenses = {
        "transporte": transport,
        "alojamiento": accommodation * days,
        "alimentacion": food * days,
        "actividades": activities
    }

    if any(amount < 0 for amount in expenses.values()):
        return {"error": "Los gastos no pueden tener valores negativos."}

    total = sum(expenses.values())

    return {
        "gastos": expenses,
        "total_estimado": round(total, 2),
        "duracion_dias": days
    }
