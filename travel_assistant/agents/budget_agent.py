
from google.adk.agents import Agent

from travel_assistant.tools.budget_tool import calculate_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.5-flash",
    description="Calcula y organiza el presupuesto de un viaje.",
    instruction="""
    Ayuda al viajero a organizar los gastos de su viaje.
    Solicita la duración, el transporte, el alojamiento por día,
    la alimentación por día y el costo de las actividades.
    Utiliza calculate_budget para calcular el total.
    No inventes precios exactos ni presentes estimaciones como precios verificados.
    Explica los resultados en español y de forma ordenada.
    """,
    tools=[calculate_budget]
)
