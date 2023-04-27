import random
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

    payment = float(input("Enter the total bill value: "))
    pay = 0

    if num_friends <= 0:
        print("No one is joining for the party")
    else:
        print("")
        pay = round(payment / num_friends, 2)
        for key in friends_dict:
            friends_dict[key] = pay


    print("")
    random_chose = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")

    if random_chose == "No":
        print("")
        print("No one is going to be lucky")
        print("")
        print(friends_dict)
    elif random_chose == "Yes":
        temp = num_friends - 1
        pay = round(payment / temp, 2)
        print("")
        chose = random.choice(list(friends_dict.keys()))
        print(chose,"is the lucky one!")
        friends_dict[chose] = 0
        for key in friends_dict:
            if key != chose:
                friends_dict[key] = pay
        print("")
        print(friends_dict)
