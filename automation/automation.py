import re

def main(filename):
    input_text = ''
    input_list = []
    potential_phone_numbers = []
    potential_emails = []
    good_phone_numbers = []
    good_emails = []

    input_text = read_template(filename)

    input_list = input_text.split()

    for word in input_list:
        if '@' in word:
            potential_emails.append(word)
        else:
            if sum(char.isdigit() for char in word) > 6:
                potential_phone_numbers.append(word)

    good_emails = validate_email(potential_emails)
    good_phone_numbers = validate_phone(potential_phone_numbers)

    good_emails = remove_duplicates(good_emails)
    good_phone_numbers = remove_duplicates(good_phone_numbers)

    good_emails.sort()
    good_phone_numbers.sort()

    save_to_file(good_emails, './automation/assets/email-contacts.txt')
    save_to_file(good_phone_numbers, './automation/assets/phone-contacts.txt')

def read_template(filename):
    try:
        with open(filename, "r") as template_file:
            template_content = template_file.read()
            template_content = template_content.strip()
            return template_content
    except FileNotFoundError:
        raise FileNotFoundError

def validate_email(potential_emails):
    good_emails = []
    bad_emails = []  

    for address in potential_emails:
        valid_email = True
        bad_characters = '(),:"";<>[]"\"'


        sum_of_at = 0
        for char in address:
            if char == '@':
                sum_of_at += 1
        if sum_of_at != 1:
            valid_email = False
            bad_emails.append(address)

        elif len(address) > 254:
            valid_email = False
            bad_emails.append(address)

        else:
            for char in address:
                if char in bad_characters:
                    valid_email = False
                    bad_emails.append(address)

        if valid_email is True:
            local, domain = address.split("@")

            if len(local) > 64:
                valid_email = False
                bad_emails.append(address)

            elif local[0] == '.':
                valid_email = False
                bad_emails.append(address)

            elif local[-1] == '.':
                valid_email = False
                bad_emails.append(address)

        if valid_email is True:
            good_emails.append(address)

    return good_emails

def validate_phone(input_phone_num):
    good_phone_num = []
    bad_phone_num = [] 

    for phone_num in input_phone_num:
        num_to_test = phone_num
        valid_number = True

        if 'x' in num_to_test:
            main, extension = num_to_test.split('x')
        else:
            main = num_to_test
            extension = ''





#     # Adapted Code from Mike Shen & iterated using ChatGPT
#     # https://github.com/mikeshen7/automation/blob/main/automation/automation.py