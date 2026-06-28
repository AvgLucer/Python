y = int(input("Enter Number of Products : "))
list1 = []
list2 = []
sub_total=[]

for x in range(y):
    try:
        a = x+1
        prod_name = input(f"Enter Name of the Product-{a}:")
        prod_price = int(input(f"Enter Price of the Product-{a}:"))
        list1.append(prod_name)
        list2.append(prod_price)
        if(prod_price>=500):
            discount = 100
            sub_total.append(prod_price - 100)
        else:
            sub_total.append(prod_price)
    except ValueError as o:
        print("Error Occured : " , o)



print(f"List of Products : {list1}")
print(f"Prices of Each Product : {list2}")
print(f"Final Price Before Discount{sum(list2)}")
print(f"Final Price After Discount {sum(sub_total)}")

