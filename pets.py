#Multiple function calling
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}")

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='Max')


#Function with keyword argument
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry')


#Default values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='Max')

#Equivalent function calls
# def describe_pet(pet_name, animal_type='dog'):
#     # A dog named Willie.
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# #describe_pet('willie')
# describe_pet(pet_name='willie')

#     # A hamster named Harry.
# #describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

#Describe city function
def describe_city(country_name, city_name='Kampala'):
    print(f"{city_name} is in {country_name}")
describe_city(country_name='Uganda')
describe_city(country_name='Kenya', city_name='Nairobi')