#Vote Eligibility Checker
list1 = []
list2 = []
list3 = []

for i in range(1,4):
    try:
        name = input("Enter Name of the Person :")
        age = int(input("Enter Age of the Person :"))
        list1.append(name)
        list2.append(age)
        if(age<18):
            list3.append("InEligible for Voting")
        else:
            list3.append("Eligible for Voting")
    except ValueError as e:
        print("Error Occured :" , e)

print(f"List of the names: {list1}")
print(f"List of the Age :{list2}")
print(f"Voting Eligibility :{list3}")
