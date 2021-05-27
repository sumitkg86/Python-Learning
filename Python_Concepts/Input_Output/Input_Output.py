while(True):
    userData = input("Enter the number: \n")
    try:
        x = int(userData[0])
        y = int(userData[1])
        print("Valur of x=", x, "y=", y)
    except:
        print("Input number is not valid please try again")
    else:
        break