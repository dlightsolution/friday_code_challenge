# CODE CHALLENGE
Following is my submission to the code challenge provided by [FRIDAY](https://www.friday.de/) as part of their selection process.
## The challenge: Addressline
An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

1. Write a simple program that does the task for the most simple cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   2. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   3. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   2. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   2. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   3. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   4. `"Calle 39 No 1540"` -> import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))`{"street": "Calle 39", "housenumber": "No 1540"}`
# Solution
## Technology used
I have used VS Code as a code editor.<br>
Python and pandas to manipulate the address strings.<br>
Google and ChatGPT as mentors.
## How to Run?
1. Clone or download repo.
2. pip install -r requirements.txt
3. Run python main.py.

This will let you test one address at a time.
## How to test multiple addresses?
1. Create a csv file with the following column names: address,streetname,housenumber.
2. Fill the file accordingly.
3. Save as addresses.csv.
4. Run python test.py.

This will cross-validates the streetnames and housenumbers found in "addresses.csv" against the streetnames and housenumbers identified by our program.
Feel free to test with a bunch of other addresses.
## How does it work?
the main.py is our entry point and imports MyFunctions class from functions.py to perform the following:
1. Reads address from input.
3. Splits address into words.
4. Finds the last numerical value.
5. Assigns the street and housenumber considering the following constraints:
   1. House numbers that starts with a suffix "No":
   `"Calle 39 No 1540" outputs "No 1540"`
   2. House numbers that are alphanumeric:
   `"Blaufeldweg 123B"`
   3. Alphanumeric housenumbers with white space:
    `"Auf der Vogelwiese 23 b"`

6. Outputs results in json format.

Further explanation of the functions are included along the code in the comments.
## Limitations
This will not work for addresses that:
1. Starts with the house number and the streetname contains a numeric or an alphanumeric value, e.g.
   1. `"8, rue 9 Avril"` -> `{"street": "8 rue", "housenumber": "9 Avril"}`
2. Has a suffix for the house number different from "No":
   1. `"Av Raccada Apt 15"` -> `{"street": "Av Raccada Apt", "housenumber": "15"}`
## Other Approches
### Regex
Another approch to solve this challenge is using regex (regular expression) but I preferred to avoid it as the expression tends become very complex and difficult to read and understand. The solution will not scale well as we add add other variation of addresses.<br>
### NLP
The approch I would go for is using a combination of rule-based and machine learning methods like Named Entity Recognition (NER) to extract structured data from unstructured text.<br>
[Parserator](https://github.com/datamade/parserator) is a toolkit that could be used to train a probabilistic parser to extract data from addresses.<br>
And [usaddress](https://github.com/datamade/usaddress) is a python library built on top of it.
