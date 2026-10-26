
from travel_assistant.tools.budget_tool import calculate_budget


def test_calculate_budget():
    result = calculate_budget(
        transport=100,
        accommodation=80,
        food=30,
        activities=50,
        days=3
    )

    assert result["total_estimado"] == 480


def test_invalid_days():
    result = calculate_budget(
        transport=100,
        accommodation=80,
        food=30,
        activities=50,
        days=0
    )

    assert "error" in result


def test_negative_expenses():
    result = calculate_budget(
        transport=-100,
        accommodation=80,
        food=30,
        activities=50,
        days=3
    )

    assert "error" in result
