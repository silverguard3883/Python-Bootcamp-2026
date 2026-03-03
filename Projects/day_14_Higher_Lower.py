import random

demo_data = [
    {
        "name": "Eiffel Tower",
        "popularity": 3.2,
        "description": "Iconic Parisian landmark",
        "location": "France"
    },
    {
        "name": "Taylor Swift",
        "popularity": 8.7,
        "description": "Global pop music star",
        "location": "United States"
    },
    {
        "name": "FIFA World Cup",
        "popularity": 12.5,
        "description": "International football tournament",
        "location": "Global event"
    },
    {
        "name": "Great Wall of China",
        "popularity": 4.1,
        "description": "Ancient defensive fortification",
        "location": "China"
    },
    {
        "name": "Elon Musk",
        "popularity": 6.9,
        "description": "Tech entrepreneur and investor",
        "location": "South Africa"
    },
    {
        "name": "Olympic Games",
        "popularity": 9.3,
        "description": "Global multi-sport competition",
        "location": "Global event"
    },
    {
        "name": "Statue of Liberty",
        "popularity": 2.8,
        "description": "Symbol of freedom",
        "location": "United States"
    },
    {
        "name": "Mona Lisa",
        "popularity": 5.4,
        "description": "Famous Renaissance painting",
        "location": "France"
    }
]

game_over = False
player_score = 0

while game_over is False:
    choice_a, choice_b = random.sample(demo_data, 2)        #Gets 2, non-repeating results from the dictionary and assigns them to choice_a or choice_b. Assigns the dictionary objects directly, instead of their indices  
    
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['location']}\n")
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['location']}")

    player_guess = input("Which is more famous? Type 'A' or 'B':  ").upper()
    
    if player_guess not in ("A", "B"):                      
        print("Invalid input. Try again.")
        continue                                        
    
    correct_guess = "A" if choice_a["popularity"] >= choice_b["popularity"] else "B"    #Sets correct answer once to avoid multiple loop iterations

    if player_guess == correct_guess:
        print("Correct!")
        player_score += 1
    else:
        print(f"Incorrect! Final score: {player_score}")
        game_over = True






























