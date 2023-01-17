from functions import MyFunctions


def test_addresses():
    #Read csv file
    df = MyFunctions.read_csv("addresses.csv")
    #Create empty lists to store positive and negative addresses
    positiveaddresses = []
    negativeaddresses = []
    #Iterate through the DataFrame
    for i,row in df.iterrows():
        words = MyFunctions.split_address(row['address'])
        idx = MyFunctions.parse_words(words)
        data = MyFunctions.assign_values(idx, words)
        #print(data)
        #print({"street": row["streetname"], "housenumber": row["housenumber"]})
        #This will compare the json output from the main.py file with the expected output
        if data == {"street": row["streetname"], "housenumber": row["housenumber"]}:
            positiveaddresses.append(row["address"])
        else:
            negativeaddresses.append(row["address"])

    #print the number of negative addresses
    print(len(negativeaddresses),"/",len(df)," has failed the test")
    #Print the negative addresses if found
    if len(negativeaddresses) > 0:
        print("The following addresses have failed the test:", negativeaddresses)
    else:
        print("Alles gut!")
        
print(test_addresses())
