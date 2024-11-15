responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for user's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ") 

    #store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like another person to respond? (Yes/No) ")
    if polling_active == 'no':
        polling_active = False
    
    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

        

