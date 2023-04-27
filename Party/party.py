friends_dict = {}

num_friends = int(input("Enter the number of friends joining (including you):"))
print("")

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of", num_friends,"friend (including you), each on a new line: ")
    for i in range(num_friends):
        name = input()
        friends_dict[name] = 0
    print("")

    print("")
    payment = float(input("Enter the total bill value: "))
    pay = 0

    if num_friends <= 0:
        print("No one is joining for the party")
    else:
        print("")
        pay = round(payment / num_friends, 2)
        for key in friends_dict:
            friends_dict[key] = pay

        print(friends_dict)
