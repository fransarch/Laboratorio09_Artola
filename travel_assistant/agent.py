
from google.adk.agents import Agent

from travel_assistant.agents.budget_agent import budget_agent
from travel_assistant.agents.itinerary_agent import itinerary_agent
from travel_assistant.agents.risk_reviewer_agent import risk_reviewer_agent
from travel_assistant.agents.web_search_agent import web_search_agent

root_agent = Agent(
    name="travel_coordinator",
    model="gemini-2.5-flash",
    description="Coordina los agentes especializados en la planificación de viajes.",
    instruction="""
    Eres el coordinador de un asistente de viajes.
    Analiza la solicitud del usuario y utiliza los agentes especializados
    para preparar una respuesta completa.

    Utiliza web_search_agent para buscar información sobre el destino.
    Utiliza itinerary_agent para organizar las actividades.
    Utiliza budget_agent para estimar los gastos.
    Utiliza risk_reviewer_agent para revisar los riesgos del viaje.

    Integra los resultados en una respuesta clara y ordenada.
    Responde en español y señala qué información necesita verificación.
    """,
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent
    ]
)
