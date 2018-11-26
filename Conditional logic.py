 Name = str(input("what is your name"))
print("You are Welcome!" + Name)
BirthYear = int(input("User should enter year of birth "))
if BirthYear >= 2000:
    print("User is a minor")
elif BirthYear >= 1982 and BirthYear < 2000:
    print("User is a youth")
else:
    print("User is an adult")

