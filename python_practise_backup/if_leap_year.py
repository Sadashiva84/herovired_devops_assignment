# check if the year is a leap year
while True:
    year = int(input("Please Enter A Year or Ctrl+z to quit: \t"))

    if year%4==0:
        if year%400==0:
            print("\nIt is Not a leap year\n")
        else:
            print("\nIt is a leap year\n")

    else:
        print("\nIt is Not a leap year\n")