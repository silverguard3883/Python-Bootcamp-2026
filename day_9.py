#Dictionaries

dict = {"key": "value",
        "word": "defintion of the word",
        "function": "a thing that does something",
        123: "example of using the integer data type in a dictionary"
    
}

print(dict["word"])
print(dict[123])

#Adding a value to a dictionary
dict["added value"] = "this is an example of an added value"

print(dict)

empty_dict = {}

"""
#Delete an entire dictionary
dict = {}
"""

#Edit an item in a dictionary
dict["word"] = "an edited entry in the dictionary"
print()

#Loop through a dictionary
for index in dict:
    print(index)        #Only loops through keys
    print(dict[index])  #Returns value of the key at the index
    print()
    
    
#Nesting

nested_dict = {
    "key": ["a", "b", "c"],
    "key1": "value",
    "key2": {"a": 54,
             "b": "some stuff"
    },
    "key3": {"c": 88,
             "d": 99
                    
    }
}


#Access an index of a list in a dictionary

print(nested_dict["key"][0])    #"Key" is the key of the list you want to access
                                #"0" is the index of that list
                                
                                
#Nested list
nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][0])

#Nested dictionary
print(nested_dict["key2"]["b"])
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
    
    
    
    
    
    
    
    
    

