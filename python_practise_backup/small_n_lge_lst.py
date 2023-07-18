# program to find the small and large numbers from the list

tot_val = int(input("Enter Total Number Of Elements You Want To Enter: "))

act_list = []
i = 0
j = 0
while i<tot_val:

    list_prep = int(input(f" Enter Value {i+1}: "))
    act_list.append(list_prep)
    i+=1
    
print("Your list is: ", act_list)
act_list.sort()
print("Your Smallest Number is: ", act_list[0])
print("Your Largest Number is: ", act_list[-1])
