
# While statement for asking user input indefenitely
while True:

    num = input("Please Enter a Number or press q to quit: ")

    if num.isdigit()==True and num != 'q': 
        # to check if the entered value can 
        #be converted into a digit digit and also if the value is not a 'q'  
        
        num =int(num)
        j= 1
        for i in range(1,num+1):
            j=j*i
            i+=1
        print(j)

# only 'q' quits
    elif num =='q':
        break

# other options lets user prompt main option
    else:
        print("Please retry a valid option")

print("Quitting")
