import pytest
from automation.automation import validate_phone, validate_email, read_template, main

def test_exists():
    assert main()

def test_read_potential_contacts():
    content = read_potential_contacts()
    assert isinstance(content, str)

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

# @pytest.fixture(scope='module')
def missing_input_file():
    return 'missing_template.txt'

# @pytest.fixture(scope='module')
def expected_phone_file():
    return './automation/assets/phone-contacts.txt'

@pytest.fixture(scope='module')
def expected_email_file():
    return './automation/assets/email-contacts.txt'

def test_valid_contacts_extraction(valid_contacts_input_file, expected_phone_file, expected_email_file):
    # Run main function
    main(valid_contacts_input_file)

    # Verify phone contacts file
    assert os.path.exists(expected_phone_file)
    with open(expected_phone_file, 'r') as f:
        phone_contacts = f.read()
        # Add assertions for the expected phone contacts format

    # Verify email contacts file
    assert os.path.exists(expected_email_file)
    with open(expected_email_file, 'r') as f:
        email_contacts = f.read()
        # Add assertions for the expected email contacts format

def test_invalid_contacts_exclusion(invalid_contacts_input_file, expected_phone_file, expected_email_file):
    # Run main function
    main(invalid_contacts_input_file)

    # Verify phone contacts file
    assert os.path.exists(expected_phone_file)
    with open(expected_phone_file, 'r') as f:
        phone_contacts = f.read()
        # Add assertions to ensure there are no invalid phone contacts

    # Verify email contacts file
    assert os.path.exists(expected_email_file)
    with open(expected_email_file, 'r') as f:
        email_contacts = f.read()
        # Add assertions to ensure there are no invalid email contacts

def test_duplicate_contacts_removal(duplicate_contacts_input_file, expected_phone_file, expected_email_file):
    # Run main function
    main(duplicate_contacts_input_file)

    # Verify phone contacts file
    assert os.path.exists(expected_phone_file)
    with open(expected_phone_file, 'r') as f:
        phone_contacts = f.read()
        # Add assertions to ensure there are no duplicate phone contacts

    # Verify email contacts file
    assert os.path.exists(expected_email_file)
    with open(expected_email_file, 'r') as f:
        email_contacts = f.read()
        # Add assertions to ensure there are no duplicate email contacts

def test_missing_input_file(missing_input_file):
    # Run main function and expect FileNotFoundError
    with pytest.raises(FileNotFoundError):
        main(missing_input_file)
