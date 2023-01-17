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
1.Clone or download.
2.Run python main.py
This will let you test one address at a time. To test multiple addresses
## How to test other addresses?
1.Create a csv file with the following column names: address,streetname,housenumber.
2.Fill the file accordingly
3.Save a
3.Run python addresses.py
This will test the streetnames and housenumbers found in "addresses.csv" and cross-validates them against the streetnames and housenumbers identified by our program.
Feel free to test with a bunch of other addresses.
## How does it work?
1.Reads address from user input.
2.Creates a DataFrame with an address column.
3.Parses the words and finds the last numerical value.
4.Assigns the street and housenumber considering the following constraints:

   1.House numbers that starts with a suffix "No":
   "Calle 39 No 1540" outputs "No 1540"
   2.House numbers that are alphanumeric:
   "Blaufeldweg 123B"
   3.Alphanumeric housenumbers with white space:
   "Auf der Vogelwiese 23 b"
5.Outputs results in json format
## Limitations
## Other Approches
