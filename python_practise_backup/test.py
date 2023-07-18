#This is really a test
from random import *
# c = randrange(0,5,2)
# print(c)

# list1 = 1
# list2 = 1
# list3 = 1

# player_opt=0
# inp=0
# #deleteoptions



# if inp==0:
#     print("")
    




# elif inp=='7':
#     list1[0]=player_opt
# elif inp=='8':
#     list1[2]=player_opt
# elif inp=='9':
#     list1[4]=player_opt
# elif inp=='4':
#     list2[0]=player_opt
# elif inp=='5':
#     list2[2]=player_opt
# elif inp=='6':
#     list2[4]=player_opt
# elif inp=='1':
#     list3[0]=player_opt
# elif inp=='2':
#     list3[2]=player_opt
# elif inp=='3':
#     list3[4]=player_opt

# sel_list = ['1','2','3','4','5','6','7','8','9']

# print(sel_list)

# sel_list.remove('5')

# print(sel_list)

lis = [1,2,3,3,4,4,6,75,7]

k = choice(lis)
print(k)


7 8 9
4 5 6
1 2 3



if (list1[0]==list1[2]==list1[4])==cpu_opt or (list2[0]==list2[2]==list2[4])==cpu_opt or \
            (list3[0]==list3[2]==list3[4])==cpu_opt or (list1[0]==list2[0]==list3[0])==cpu_opt or \
            (list1[2]==list2[2]==list3[2])==cpu_opt or (list1[4]==list2[4]==list3[4])==cpu_opt or \
            (list1[0]==list2[2]==list3[4])==cpu_opt or (list1[4]==list2[2]==list3[0])==cpu_opt:
