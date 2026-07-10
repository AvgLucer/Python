#Online Ordering App
y=int(input("How Many Dishes Do You want to Order"))
cost = 0
cancel_order = False

for x in range(y):
    hotels = int(input("Choose Hotel -> 1 . Jaba Ka Dhaba 2 . Kanpur Fried Chinese 3.  Surya Credit Restauraunt and Bar 4. La Bella Baguette"))
    if hotels == 1:
        print(f" Jaba Ka Dhaba Selected")
        menu = int(input("Choose Dish -> 1.Paneer Butter Masala [2$]  2. Dal Makhani [1.5$] 3. Gulab Jamun [0.2$]"))
        if menu == 1:
            print(f"Paneer Butter Masala Selected🍲")
            cost += 2
        elif menu == 2:
            print(f"Dal Makhani Selected 🥘")
            cost += 1.5
        elif menu == 3:
            print(f"Gulab Jamun Selected🧆")
            cost += 0.2
        elif menu not in [1,2,3]:
            print("Invalid Menu Item [0$ Added to Cart]")
            continue
    elif hotels == 2:
        print(f" Kanpur Fried Chinese Selected")
        menu = int(input("Choose Dish ->  1. Veg Triple Fried Rice [1$] 2. Veg Triple Noodles [1$] 3. Veg Combination Rice [0.80$]")) 
        if menu == 1:
            print(f"Veg Triple Fried Rice Selected🍝")
            cost += 1
        elif menu == 2:
            print(f"Veg Triple Noodles Selected🍜")
            cost += 1
        elif menu == 3:
            print(f"Veg Combination Rice Selected🍚")
            cost += 0.8
        elif menu not in [1,2,3]:
            print("Invalid Menu Item [0$ Added to Cart]")
            continue
    elif hotels == 3:
        print(f" Surya Credit Restauraunt and Bar Selected")
        menu = int(input("Choose Dish ->  1. Soya Chaap [4$] 2. Chicken 65 [5$] 3. Chicken Lababdar [6$]"))
        if menu == 1:
            print(f"Soya Chaap Selected 🍢")
            cost += 4
        elif menu == 2:
            print(f"Chicken 65 Selected 🍗")
            cost += 5
        elif menu == 3:
            print(f"Chicken Lababdar Selected 🍖")
            cost += 6
        elif menu not in [1,2,3]:
            print("Invalid Menu Item [0$ Added to Cart]")
            continue
    elif hotels == 4:
        print(f"La Bella Baguette Selected")
        menu = int(input("Choose Dish ->  1. Frosty Vanilla Crossiant [1.95$] 2. Steamed Baguette [2.59$] 3. Singaporean Noodles [4.59$]"))
        if menu == 1:
            print(f"Frosty Vanilla Crossiant Selected🥐")
            cost += 1.95
        elif menu == 2:
            print(f"Steamed Baguette Selected 🥖")
            cost += 2.59
        elif menu == 3:
            print(f"Singaporean noodles Selected🍜")
            cost += 4.59
        elif menu not in [1,2,3]:
            print("Invalid Menu Item [0$ Added to Cart]")
            continue
    elif hotels not in [1,2,3,4]:
        print("Invalid Hotel Choice")
        cancel_order  = True
        
    
    if cancel_order:
        print("Order Cancelled")
        break
if not cancel_order:

    cost 
    print(f"Final Price of the Selected Dishes is {cost} , Please Select the Method of Payment")
    p = int(input("Payment Options :  1. UPI  2. Debit Card 3. Credit Card 4. Cash "))
    if p == 1:
        print(f"Please Pay Through UPI on the Given QR Code")
    elif p == 2:
        print(f"Please Enter Debit Card Details Below:")
        holdername = input("Enter Card Holder's Name")
        cardnumber = int(input("Enter Card Number"))
        Expdate = input("Enter Expiration Date [format : MM/YY]")
        while True:
            cvv = int(input("Enter Social Security number/ CVC/CVV [3 Digit]"))
            if len(cvv) == 3 and cvv.isdigit():
                print("Valid CVV!")
                break
            else:
                print(f"Invalid CVV , CVV Is Suppose to be 3 Digits Only")
        billadd = input("Enter Billing Address")
    elif p ==3:
        print(f"Please Enter Credit Card Details Below:")
        holdername = input("Enter Card Holder's Name")
        cardnumber = int(input("Enter Card Number"))
        Expdate = input("Enter Expiration Date [format : MM/YY]")
        while True:
            cvv = input("Enter Social Security number/ CVC/CVV [3 Digit]")
            if len(cvv) == 3 and cvv.isdigit():
                print("Valid CVV!")
                break
            else:
                print(f"Invalid CVV , CVV Is Suppose to be 3 Digits Only")

        billadd = input("Enter Billing Address")
    elif p ==4:
        print(f"Please Pay to the Counter Using Cash ")

    