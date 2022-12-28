import pytest
from app import check_document_existence, get_doc_owner_name

FIXTURES_EX = [("2207 876234", True), ("11-2", True), ("10006", True)]
FIXTURES_NAMES = [("2207 876234", "Василий Пупкин"), ("11-2", "Геннадий Покемонов"), ("10006", "Аристарх Павлов")]

@pytest.mark.parametrize('num, exp_result', FIXTURES_EX)
def test_existence(num, exp_result):
    assert check_document_existence(num) == exp_result

@pytest.mark.parametrize('num, exp_result', FIXTURES_NAMES)
def test_get_name(num, exp_result):
    assert get_doc_owner_name(num) == exp_result

