# program to find common elements between the lists

# Enter List 1
num1 = int(input("Enter the number of values you want to enter "))
i=0
user_lst1 = []
while i<num1:

    i+=1
    user_inp = int(input(f"Enter number {i}: "))
    user_lst1.append(user_inp)

print(user_lst1)

# Enter List 2
num2 = int(input("Enter the number of values you want to enter "))
i=0
user_lst2 = []
while i<num2:

    i+=1
    user_inp = int(input(f"Enter number {i}: "))
    user_lst2.append(user_inp)

print(user_lst2)

super_list = []
for i in user_lst1:
    if i in user_lst2:
        super_list.append(i)

print(super_list)