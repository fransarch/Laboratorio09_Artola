
# Sistema Multiagente de Viajes con Google ADK

Proyecto del curso de Sistemas Inteligentes de la Universidad César Vallejo.

## Agentes

- Travel Coordinator Agent
- Web Search Agent
- Itinerary Agent
- Budget Agent
- Risk Reviewer Agent

## Tecnologías utilizadas

- Python
- Google ADK
- Google Search
- Pytest
- Ruff
- Poetry

## Instalación

1. Crear y activar el entorno virtual.
2. Instalar las dependencias del proyecto.
3. Configurar la variable GOOGLE_API_KEY en el archivo .env.

## Ejecución por consola

```bash
adk run travel_assistant
```

## Interfaz web

```bash
adk web --port 8000
```

Abrir http://localhost:8000 en el navegador.

## Pruebas

```bash
python -m pytest
```

## Calidad del código

```bash
ruff check .
```
## Estado de las pruebas

El proyecto cuenta con 8 pruebas automatizadas que verifican la
estructura de los agentes, el cálculo del presupuesto y la revisión
de riesgos. Todas las pruebas pasan correctamente.

La revisión de calidad del código con Ruff también finaliza sin errores.