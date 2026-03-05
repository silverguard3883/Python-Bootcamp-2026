#Creating a custom class

# class User:
#     pass                #Pass allows for mpty functions and classes without throwing indent errors


# user1 = User()

# user1.id = "001"        #Adds "id" attribute to user1 class object
# user1.name = "bob"      #Adds "name" attribute to user1 class object

# print(user1.name)


"""Constructor"""
#Specifies what happens when a class object is created (called "initilzation")
#Can set variable, methods, attributes, etc.


"""Constructor Function"""

# class Class:
#     def __init__(self):
#         #initialize attributes, variables, etc.
#         #Essentially creates STARTING VALUES of attributes


class SocialMediaUser:
    
    def __init__(self, id, name):                       #"self" is the thing being created, in this case a SocialMediaUser
        print("New user being created...")
        self.id = id
        self.name = name
        self.followers = 0                              #Creates a default value that doesn't require a parameter            
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = SocialMediaUser("001", "billy bob")
print(user1.name)
print(user1.followers)

user2 = SocialMediaUser("002", "jane doe")

user1.follow(user2)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)



















