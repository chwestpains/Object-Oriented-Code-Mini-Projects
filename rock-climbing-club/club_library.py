class Club_Member(object): 
    def __init__(self, name, age, member_level, monthly_pay): # constructs a new member
        self.name = name
        self.age = age
        self.member_level = member_level
        self.monthly_pay = monthly_pay
        
    def print_details(self):
        print("Member Name: ", self.name,"\nAge: ", self.age, "\nMember Level: ", self.member_level, "\nMonthly Payment: ", self.monthly_pay)
        
def newMember(): # saves details for a new member
    newMember_name = input("Enter your name: ")
    newMember_age = int(input("Enter your age: "))
    member_levels = ["1: standard", "2: standard plus", "3: elite", "4: vip"]
    print("Member Levels: ", member_levels)
    newMember_member_level = int(input("Choose a membership level: "))
    if newMember_member_level == 1:
        member_price = 10
    elif newMember_member_level == 2:
        member_price = 15
    elif newMember_member_level == 3:
        member_price = 45
    elif newMember_member_level == 4:
        member_price = 100
    else:
        quitting = False
        print("Invalid option")
        choice = input("Would you like to choose again? ")
        if choice == "yes":
            newMember()
        else:
            quitting = True
            pass
    
    member = Club_Member(newMember_name, newMember_age, newMember_member_level, member_price) # creates anobject for that member
    details = [member.name, member.age, member.member_level, member.monthly_pay]
    with open("memberlist.txt", "a") as file:
        for item in details:
            file.write("%s\n" % item)
        
    print("\n")
    print("\nWelcome", member.name, "\n", member.print_details())
    
    additionalMember()
    
def additionalMember():
    choice = input("Would you like to enter another member? ")
    quitting = False
    if choice == "yes":
        newMember()
    elif choice == "no":
        quitting = True
        print("Goodbye")
        pass
    else:
        print("404 Error!")
        pass
    
def existingMember():
    checking_details = []
    with open("memberlist.txt", "r") as file:
        for line in file:
            currentPlace = line[:-1]
            checking_details.append(currentPlace)
    searching(checking_details)
    
def searching(search_list):
    user = input("Enter your name: ")
    i = 0
    
    if user not in search_list:
        print("Sorry, you are not registered")
        quitting = False
        choice = int(input("Would you like to...\n1: Enter name again\n2: Sign up\n3:Quit"))
        if choice == 1:
            searching(search_list)
        elif choice == 2:
            newMember()
        elif choice == 3:
            print("Goodbye")
            quitting = True
            pass
    else:
        if search_list[i] == user:
                n = 4 
                out = search_list[i:i+n]
                print("\nYour details\nName: ", out[0], "\nAge: ", out[1], "\nMembership Level: ", out[2], "\nMonthly Price: ", out[3])
                print("\nWelcome back", out[0])
    
        while user != search_list[i]:
            i += 4
            if search_list[i] == user:
                n = 4 
                out = search_list[i:i+n]
                print("\nYour details\nName: ", out[0], "\nAge: ", out[1], "\nMembership Level: ", out[2], "\nMonthly Price: ", out[3])
                print("\nWelcome back", out[0])
    
    
            
            
            
def typeOfMember(): # asks user if they are a new or existing member
    member_type = input("Are you a new or existing member? ")
    if member_type == "new":
        newMember()
    elif member_type == "existing":
        existingMember()
    else:
        print("Sorry I didn't quite catch that")
        quitting = False
        choice = input("Would you like to choose again? ")
        if choice == "yes":
            typeOfMember()
        else:
            quitting = True
            pass
