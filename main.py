from functions import MyFunctions

if __name__ == '__main__':
    
    #Get address from user
    address = input("Enter your address:" )

    #Split address into words
    words = MyFunctions.split_address(address)

    #Parse words to get the index of the last numeric value
    idx = MyFunctions.parse_words(words)

    #Assign values to street and house number
    data = MyFunctions.assign_values(idx, words)

    #Print results in json format
    print(MyFunctions.to_json(data))