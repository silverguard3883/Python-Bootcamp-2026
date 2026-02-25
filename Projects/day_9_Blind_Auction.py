bidders = {}
bidding_over = False
print("Welcome to the blind auction!")

while bidding_over is False:

    bidder_name = input("What is your name? ")
    bidder_bid = int(input("How much would you like to bid? $"))
    
    #Assigns bidder's name as the key and their dollar amount bid as the value
    bidders[bidder_name] = bidder_bid
    
    any_bidders_left = input("Are there any bidders left? Input 'yes' or 'no': ").lower()
    
    #Creates hundreds of new lines to simulate clearing a screen
    #print("\n" * 100)
    
    #Exit condition
    if any_bidders_left == 'no':
        highest_bid = 0                                                     #Sets the current highest bid to 0
        
        for bidder_name in bidders:                                         #Iterates through the dictionary using the bidder's name
            bidder_bid = bidders[bidder_name]                               #Sets the bidder's bid amount as found in the bidder's dictionary
            
            if bidder_bid > highest_bid:                                    #Compares bid amounts to find highest bidder
                highest_bid = bidder_bid                                    #Sets highest bidder amount to highest bid variable
                winner = bidder_name                                        #Sets the loop variable (bidder_name; only used during the looping process) to a static variable that meets the condition (in this case, the name of the person who had the highest bid)
        print(f"{winner} has won the auction, bidding at ${highest_bid}!")
        bidding_over = True
