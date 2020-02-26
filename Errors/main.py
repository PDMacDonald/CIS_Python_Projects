while(True):
    try:
        xi = input("Enter an integer 1 - 10: ")
        x = int(xi)

        if(x >= 1 and x <= 10):
            print(x)
            break
        print("Not in range 1 to 10. Try again...")
    except ValueError as ve:
        print("You think your funny?")

    

    

print("\nEND OF PROGRAM #1")

def increment1(x):
    x += 1
    print(x)
    if(x == 10):
        return x


def fx(x):
    x = increment1(x)
    return x

print(fx(1))
