from os import system

option = ""
small_ship = 5
big_ship = 5


while True: 
    system ("cls")
    for x in range(1,11):
        if x == big_ship:
            print( "W", end="" )
        elif x == big_ship + 1:
                print("w", end="")
        elif x == big_ship - 1:
                print("w", end="")
        else:
            print( "~", end="" )
       
            
    print("\n")          
    option = input(">>>: ")

    if option == "a":
        big_ship -= 1
    elif option == "d":
        big_ship += 1
    elif option == "x":
        print("Game over")
        system ("cls")
        break