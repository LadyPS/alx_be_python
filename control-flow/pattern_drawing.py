Size = int(input("Enter the size of the pattern: "))
number_of_rows = 1

while number_of_rows <= Size: 
    for _ in range(Size):
        print("*", end="")
    print("")
    number_of_rows += 1
