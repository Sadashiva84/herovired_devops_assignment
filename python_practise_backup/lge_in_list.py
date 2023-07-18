#large number in list
num = int(input("Enter the number of values you want to enter "))
i=0
user_lst = []
while i<num:

    i+=1
    user_inp = int(input("Enter number "))
    user_lst.append(user_inp)

print(user_lst)
j=0
for i in user_lst:
    if i>j:
        j=i
    
print(f"Largest number is {j}")


