#program to play tic-tac-toe
from random import *


# simple board that looks like this
#    [.|.|.]
#    [.|.|.]
#    [.|.|.]

list1 = ['7','|','8','|','9']
list2 = ['4','|','5','|','6']
list3 = ['1','|','2','|','3']

sel_list = ['1','2','3','4','5','6','7','8','9']

print("Welcome to tic tac toe")

while True:
    player_opt = (input("Select x or o: "))
    
    if player_opt == 'x':
        cpu_opt = 'o'
        break
    elif player_opt == 'o':
        cpu_opt = 'x'
        break
    else:
        continue

# print("\t", x, x, x)
turn = 1
win_stat = False

while True:
    print("         The Board")
    print(list1)
    print(list2)
    print(list3)
    print("")
    turn+=1


    if turn%2==0:
        
        inp = input(f"Please Enter Your Your Position, player {player_opt}: ")

        if list1[0]==list1[2]==list1[4]==player_opt or list2[0]==list2[2]==list2[4]==player_opt or \
            list3[0]==list3[2]==list3[4]==player_opt or list1[0]==list2[0]==list3[0]==player_opt or \
            list1[2]==list2[2]==list3[2]==player_opt or list1[4]==list2[4]==list3[4]==player_opt or \
            list1[0]==list2[2]==list3[4]==player_opt or list1[4]==list2[2]==list3[0]==player_opt:
            win_stat = True
            print(" You Won !!!")
            quit
        
        elif inp=='7':
            list1[0]=player_opt
            sel_list.remove(inp)
        elif inp=='8':
            list1[2]=player_opt
            sel_list.remove(inp)
        elif inp=='9':
            list1[4]=player_opt
            sel_list.remove(inp)
        elif inp=='4':
            list2[0]=player_opt
            sel_list.remove(inp)
        elif inp=='5':
            list2[2]=player_opt
            sel_list.remove(inp)
        elif inp=='6':
            list2[4]=player_opt
            sel_list.remove(inp)
        elif inp=='1':
            list3[0]=player_opt
            sel_list.remove(inp)
        elif inp=='2':
            list3[2]=player_opt
            sel_list.remove(inp)
        elif inp=='3':
            list3[4]=player_opt
            sel_list.remove(inp)


    elif turn%2 != 0:
        # print("          CPU's Turn ")
        if win_stat == True:
            print("Player Wins !!!")
            break

        if (list1[0]==list1[2]==list1[4])==cpu_opt or (list2[0]==list2[2]==list2[4])==cpu_opt or \
            (list3[0]==list3[2]==list3[4])==cpu_opt or (list1[0]==list2[0]==list3[0])==cpu_opt or \
            (list1[2]==list2[2]==list3[2])==cpu_opt or (list1[4]==list2[4]==list3[4])==cpu_opt or \
            (list1[0]==list2[2]==list3[4])==cpu_opt or (list1[4]==list2[2]==list3[0])==cpu_opt:
            print(" CPU Wins !!!")
            break

        else:
            
            while True:

                cpu_check=choice(sel_list)
                break


            if cpu_check=='7':
                list1[0]=cpu_opt
                sel_list.remove(cpu_check) 

            elif cpu_check=='8':
                list1[2]=cpu_opt
                sel_list.remove(cpu_check)

            elif cpu_check=='9':
                list1[4]=cpu_opt
                sel_list.remove(cpu_check)

            elif cpu_check=='4':
                list2[0]=cpu_opt
                sel_list.remove(cpu_check)
            
            elif cpu_check=='5':
                list2[2]=cpu_opt
                sel_list.remove(cpu_check)

            elif cpu_check=='6':
                list2[4]=cpu_opt
                sel_list.remove(cpu_check)
           
            elif cpu_check=='1':
                list3[0]=cpu_opt
                sel_list.remove(cpu_check)

            elif cpu_check=='2':
                list3[2]=cpu_opt
                sel_list.remove(cpu_check)

            elif cpu_check=='3':
                list3[4]=cpu_opt
                sel_list.remove(cpu_check)
            
    elif turn == 11:
        print("/n         Match Draw!")
        break
    





           
                

            
            
            
            
            
            




