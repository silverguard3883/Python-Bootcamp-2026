file = open("example.txt")
content = file.read()
print(content)
file.close()                                    #The "close" method can be hard to remember to input after a lot of code it written.
                                                #Below is a standard convention

with open("example.txt") as file:
    content = file.read()
    print(content)

with open("example.txt", "w") as file:             #"W" makes file writable
    file.write("\nNew Text inserted")
    content = file.read()
    print(content)

with open("new_text.txt", "w") as file:             #When using this trick, if the file being called doesn't exist
    file.write("\nNew Text inserted")               #Python will create the file instead


