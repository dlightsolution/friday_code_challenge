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
        print({"street": row["streetname"], "housenumber": row["housenumber"]})
        #Check if data in csv is equal to the expected output
        if data == {"street": row["streetname"], "housenumber": row["housenumber"]}:
            positiveaddresses.append(row["address"])
        else:
            negativeaddresses.append(row["address"])

    #Print the negative addresses
    print(len(negativeaddresses),"/",len(df)," has failed the test")
        
print(test_addresses())