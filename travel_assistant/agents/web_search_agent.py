
from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-2.5-flash",
    description="Busca información actualizada sobre destinos turísticos.",
    instruction="""
    Busca información útil sobre el destino solicitado por el viajero.
    Considera lugares turísticos, horarios, transporte y recomendaciones.
    Utiliza Google Search para consultar información.
    Responde en español y diferencia los datos encontrados de las recomendaciones.
    """,
    tools=[google_search]
)
