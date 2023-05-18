import pytest
from automation.automation import validate_phone, validate_email, read_template, main

# def test_exists():
#     assert main()

# def test_read_potential_contacts():
#     content = read_potential_contacts()
#     assert isinstance(content, str)

# @pytest.mark.skip("TODO")
def test_email_happy():
    actual = validate_email(['hansolo@starwars.com',])
    expected = ['hansolo@starwars.com',]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_bad_char_1():
    actual = validate_email(['han(solo@starwars.com',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_bad_char_2():
    actual = validate_email(['han)solo@starwars.com',])
    expected = []
    assert actual == expected

# @pytest.fixture(scope='module')
def valid_contacts_input_file():
    return 'existing-contexts.txt'

# @pytest.fixture(scope='module')
def invalid_contacts_input_file():
    return 'template_invalid.txt'

# @pytest.fixture(scope='module')
def duplicate_contacts_input_file():
    return 'template_duplicates.txt'

