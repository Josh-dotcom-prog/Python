#Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

Programmer = get_formatted_name('Joshua', 'Edyangu')
print(Programmer)

#Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

Lecturer = get_formatted_name('Lubega', 'Jonathan', 'Moses')
print(Lecturer)

#Sometimes the user will not have to provide a middle name since they might not be having it
#so we are going to make it optional using the code below
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

student = get_formatted_name('Joshua', 'Edyangu')
print(student)

student = get_formatted_name('Jonathan', 'Moses', 'Lubega')
print(student)


