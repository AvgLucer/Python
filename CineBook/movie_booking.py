#Movie Ticket Booking System
y = int(input("How Many Tickets Do You want to Book"))
mlist=[]
price=[]
for x in range(y):
    Movie = int(input("Select Movie -> 1. Batman Vs Superman 2. Hitman's Bodyguard 3. Free Guy 4. Avengers Endgame : "))

    if Movie==1:
        print("Batman Vs Superman : Dawn of Justice Selected")
        print("Price of the Movie is : 10$") 
        mlist.append("Batman vs Superman🎫")
        price.append(10)
    elif Movie==2:
        print("Hitman's Bodyguard Selected")
        print("Price of the Movie is 9$")
        mlist.append("Hitman's Bodyguard🎫")
        price.append(9)

    elif Movie==3:
        print("Free Guy Selected")
        print("Price of the Movie is 8$")
        mlist.append("Free Guy Selected🎫")
        price.append(8)

    elif Movie==4:
        print("Avenger's Endgame Selected")
        print("Price of the Movie is 12$")
        mlist.append("Avenger's Endgame Selected🎫")
        price.append(12)
print("List of the Movies Selected: ",mlist)
print("Indivisual Prices of Selected Movies [in $] : ",price)
subprice = sum(price)
print("Total Sub Price of the Movies :" , sum(price),"$")

for z in range(y):
    print(f"Enter Type of Seat for Each Movie Respectively : {mlist}")
    seat = int(input(f"Select Type of Seat for Movie {z+1} : 1. Basic [0$] 2. Exclusive [5$ Extra] 3. Recliner[10$ Extra] : "))
    if seat==1:
        subprice +=0
    elif seat==2:
        subprice +=5
    elif seat==3:
        subprice += 10

finalprice = subprice
print("Total Price of the Movies is :", finalprice,"$")
