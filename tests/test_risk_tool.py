
from travel_assistant.tools.risk_tool import review_travel_risks


def test_review_travel_risks():
    result = review_travel_risks(
        destination="Cusco",
        weather="Lluvias",
        transport="Carreteras",
        safety="Cuidar pertenencias"
    )

    assert result["riesgos_identificados"]["destino"] == "Cusco"
    assert result["riesgos_identificados"]["clima"] == "Lluvias"
    assert len(result["recomendaciones"]) > 0


def test_risk_recommendations():
    result = review_travel_risks(
        destination="Lima",
        weather="Soleado",
        transport="Bus",
        safety="Precaución"
    )

    assert "recomendaciones" in result
    assert len(result["recomendaciones"]) == 3
