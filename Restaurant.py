dinner_Group = input("How many people are in your dinner group? ")
dinner_Group = int(dinner_Group)
if dinner_Group > 8:
    print(f"\nYou will have to wait for a table.")
else:
    print("Your table is ready.")