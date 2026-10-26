
def review_travel_risks(
    destination: str,
    weather: str,
    transport: str,
    safety: str
) -> dict:
    """Organiza los riesgos y recomendaciones de un viaje."""

    risks = {
        "destino": destination,
        "clima": weather,
        "transporte": transport,
        "seguridad": safety
    }

    recommendations = [
        "Consultar los avisos oficiales antes de viajar.",
        "Verificar el estado del transporte y las rutas.",
        "Mantener documentos y objetos de valor en un lugar seguro."
    ]

    return {
        "riesgos_identificados": risks,
        "recomendaciones": recommendations
    }
