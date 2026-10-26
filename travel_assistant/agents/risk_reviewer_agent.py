
from google.adk.agents import Agent

from travel_assistant.tools.risk_tool import review_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-2.5-flash",
    description="Revisa los riesgos y las medidas preventivas de un viaje.",
    instruction="""
    Evalúa los posibles riesgos relacionados con el destino,
    el clima, el transporte y la seguridad.
    Utiliza review_travel_risks para organizar la información
    recibida y presentar recomendaciones preventivas.
    No presentes información no verificada como un hecho.
    Responde en español de forma clara y ordenada.
    """,
    tools=[review_travel_risks]
)
