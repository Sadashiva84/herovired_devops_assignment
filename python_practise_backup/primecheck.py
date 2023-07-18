
while True:

    num = int(input("please enter a number to check if it is prime or not:"))
    check = [2,3,5,7]

# i am checking for my 'i' in check to be divisible 

    for i in check:
        # if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0:
        if num%i==0:
            print("Not a prime")
            break
    
    if num%i==0:
        break
    else:
        print("It is a prime, Hooray!")
            
    
            