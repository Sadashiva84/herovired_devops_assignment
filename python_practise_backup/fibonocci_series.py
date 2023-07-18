# program to solve fobonacci series for the 'n' num of the series
while True:
    num = int(input("Please enter the number of series or 'ctrl+z' to quit: \n"))

    i=0
    j=1
    fib_list = [0,1]
    for i in range(1,num):
        fib_list.append(j)
        j=j+fib_list[i]

    print("Your Fibonacci series is: ", fib_list)


