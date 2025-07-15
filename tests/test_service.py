from app.service import Service


def test_should_return_matching_results():
    filters = '{"brand": "Honda"}'
    service = Service(filters)
    result = service.execute()
    assert isinstance(result, str)
    assert "Honda" in result


def test_should_return_empty_list_when_no_match():
    filters = '{"brand": "MarcaInexistente123"}'
    service = Service(filters)
    result = service.execute()
    assert result == "[]"


def test_should_apply_multiple_filters():
    filters = '{"brand": "Toyota", "fuel_type": "flex", "transmission": "automatico"}'
    service = Service(filters)
    result = service.execute()
    assert isinstance(result, str)


def test_should_return_all_if_no_filters():
    filters = "{}"
    service = Service(filters)
    result = service.execute()
    assert isinstance(result, str)
    assert result.startswith("[")
