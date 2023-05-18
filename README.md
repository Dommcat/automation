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
[Google](https://www.google.com)  
[ChatGPT](https://openai.com/) - Asked ChatGPT for regex several times before getting working regex. Verified on Regex101.
ChatGPT log:
```
Here's the formatted regex for Python:

python
Copy code
r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
Note that the r before the opening quote indicates a raw string, which is often used with regex patterns to avoid unwanted string escapes.




ty 1776
Write regex to find the following:
Sure! Here are regex patterns to find the following:

Email addresses:
python
Copy code
r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"



ty 1776
(822)773-2085x75019
(489)319-6885x20033
443.538.6520x515
176-099-6255x6289
714-23-3809
+1-355-752-3413x2865
To extract the phone numbers in the formats you provided and store them in xxx-yyy-zzzz format, you can use the following regex pattern:

python
Copy code
r"(?:\+?\d{1,3}[.-])?\(?\d{3}\)?[.-]?\d{3}[.-]?\d{4}(?:x\d+)?"
Here's how the pattern works:

(?:\+?\d{1,3}[.-])?: Matches an optional country code at the beginning of the phone number, followed by an optional separator character (either . or -).
\(?\d{3}\)?: Matches an optional opening parenthesis, then 3 digits (the area code), and then an optional closing parenthesis.
[.-]?: Matches an optional separator character.
\d{3}[.-]?\d{4}: Matches the remaining 7 digits of the phone number, optionally separated by either . or -.
(?:x\d+)?: Optionally matches an extension number, starting with the letter "x" and followed by one or more digits.
So for the phone numbers you provided, the matches using this pattern would be:

(822)773-2085x75019 => 822-773-2085x75019
(489)319-6885x20033 => 489-319-6885x20033
443.538.6520x515 => 443-538-6520x515
176-099-6255x6289 => 206-176-099-6255x6289 (since the area code is missing, we presume it's 206)
714-23-3809 => 206-714-23-3809 (since the area code is missing, we presume it's 206)
+1-355-752-3413x2865 => 355-752-3413x2865
```
[Regex 101](https://regex101.com/)
TAs: Raven helped with some regex issues I was having

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