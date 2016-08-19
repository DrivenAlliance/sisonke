names = []

while (raw_input("Do you want to add another name to the list(Y or N)?: ") == "Y"):
    name_to_add = raw_input("Name to add: ")
    names.append(name_to_add)

print("You've added the following names to the list: %s" % names)
