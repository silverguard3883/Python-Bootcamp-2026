#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r'Input\Names\invited_names.txt', "r") as names:
    names = names.readlines()

with open(r'Input\Letters\starting_letter.txt', "r") as letter:
    content = letter.read()

for name in names:
    name = name.strip()
    addressed_letter = content.replace("[name],", f"{name},")
    with open(fr"Output\ReadyToSend\{name}.txt", "w") as ready_letter:
        ready_letter.write(addressed_letter)


