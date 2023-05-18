# LAB - Class 19
# Project: Lab: Automation
# Author: Dominick Martin
# Automation 

# Feature Tasks and Requirements:
- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.
  - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
  - phone numbers with missing area code should presume 206
  - phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

# Implementation Notes
  - Find potential-contacts.txt and existing-contacts.txt in folder assets for today’s class in course repo.

# User Acceptance Tests
- The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

## Links and resources:
ChatGPT 


## SETUP
```
Virtual environment:
python3 -m venv .venv
python3 .venv/bin/activate

pip install -r requirements.txt
# Will install pytest by default

run app with:
python3 automation_directory/automation.py

run pytest with:
NA - Visual Verification
``` 

## Link to code:
[automation](/automation/automation.py)