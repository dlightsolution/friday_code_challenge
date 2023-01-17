import json
import pandas as pd


class MyFunctions:

    def split_address(address: str)-> pd.DataFrame:
        """A Function that takes a string as input
         and returns a pandas DataFrame."""
        # Create a pandas DataFrame with a single column
        df = pd.DataFrame({'address': [address]})
        # Splitting the address into words
        words = df.address[0].split()
        #remove commas from the words if
        words = [word.replace(",", "") for word in words]
        return words

    
    def parse_words(words: pd.DataFrame)-> int:
        """A Function that parses the addess and returns
         the index of the last numeric value"""
        # Determining the index of last numeric value
        try:
            for i in range(len(words)-1,-1,-1):
                if words[i].isnumeric():
                    idx = i
                    break
                #This is for the case the number is strictly alphanumeric (123B)
                elif words[i].isalnum() == True and words[i].isalpha() == False:
                    idx = i
                    break
            return idx
        except:
            print("No numeric value found in the address")
            return None

    
    def assign_values(idx: int, words: pd.DataFrame)-> json:
        """A Function that takes an index and a 
        pd.DataFrame as input and returns a dictionary"""
        #Check if street number index is 0
        if idx == 0:
            street = " ".join(words[1:])
            house_number = words[idx]

        else:
        # Assigning the street name
            street = " ".join(words[:idx])
            #if streetname has "No" in it drop it and move it to the house number
            if "No" in street:
                street = street.replace("No", "")
                house_number = "No "+" ".join(words[idx:])
            #if the address has no house number
            elif idx == None:
                street = " ".join(words)
                house_number = "No house number found"
            else:
            # Assigning the house number
                house_number = " ".join(words[idx:])
            
        # Create a dictionary
        data = {'street': street, 'housenumber': house_number}
        return data

    
    def to_json(data: dict)-> json:
        """A Function that turns a dictionary into json"""
        return json.dumps(data)


    
    def read_csv(path: str)-> pd.DataFrame:
        """A Function that reads csv and turns it into DataFrame"""
        df = pd.read_csv(path)
        return df

