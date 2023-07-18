# Vowels in a string
string = input("Please Enter a string: ")
vow = ['a','e','i','o','u']
vow_count = []
for i in string:
    if i in vow:
        vow_count.append(i)
print("The number of vowels in the string are: ",len(vow_count))

        