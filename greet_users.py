#Passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
usernames = ['Job', 'Jessey', 'Judith', 'Joan']
greet_users(usernames)