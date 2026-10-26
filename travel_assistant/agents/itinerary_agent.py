
from google.adk.agents import Agent

itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.5-flash",
    description="Organiza itinerarios de viaje según el destino y la duración.",
    instruction="""
    Elabora un itinerario de viaje según el destino, la cantidad de días,
    las preferencias y las actividades solicitadas por el viajero.
    Organiza las actividades por día y en un orden lógico.
    Considera tiempos de traslado y momentos de descanso.
    Responde en español y presenta la información de forma ordenada.
    No inventes horarios ni precios exactos cuando no tengas información.
    """
)
