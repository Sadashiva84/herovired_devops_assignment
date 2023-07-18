# Sum of elements in a list
import math

tot_val = int(input("Enter Total Number Of Elements You Want To Enter: "))

act_list = []
i = 0
j = 0
while i<tot_val:

    list_prep = int(input(f" Enter Value {i+1}: "))
    act_list.append(list_prep)
    i+=1
    
print(act_list)
print(sum(act_list))

