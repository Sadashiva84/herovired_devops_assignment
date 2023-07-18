#remove duplicates from list

tot_val = int(input("Enter Total Number Of Elements You Want To Enter: "))

act_list = []
i = 0
while i<tot_val:

    list_prep = input(f" Enter Value {i+1}: ")
    act_list.append(list_prep)
    i+=1

print(act_list)
res = [*set(act_list)]
print(res)


