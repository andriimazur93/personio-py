import responses

from tests.test_mock_employee import mock_employees, mock_personio


@responses.activate
def test_mock_search():
    # mock data & configure personio
    mock_employees()
    personio = mock_personio()
    # search for employees
    results = personio.search("Ada Alan")
    assert len(results) == 2
    # check search index state
    index = personio.search_index
    assert index.valid
    assert index.index
    assert index.last_update > 0


@responses.activate
def test_mock_search_first():
    # mock data & configure personio
    mock_employees()
    personio = mock_personio()
    # search for employees
    result = personio.search_first("stallman")
    assert result.first_name == "Richard"
    assert result.last_name == "Stallman"
