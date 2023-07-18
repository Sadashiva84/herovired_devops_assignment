st = list(input("Please Enter a string: "))
rev = st[::-1]
if rev == st:
    print(''.join(rev),"is a palindrome")

else:
    print("Not a palindrome")
    
