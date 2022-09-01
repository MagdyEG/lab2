#Declare a list of integers from ZERO to TEN, then print all even numbers in this list.

l1 = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(l1)):
    if i > 1 & i % 2 == 0:
        print(l1[i])


l1[::2]




#declare a list of integers from ZERO to any given integer (by the user),
#then print all numbers in this list that are divisible by 3 in a reverse order.

l2 = [i for i in range(0,int(input("enter your bound:")))]
print(l2[::-3])




#takes in a string argument myStr, which consists of one or more words, and
#returns another string, in which:

def reverse5(myStr):
    l3 = [str(input("enter :"))]
    for i in range(len(l3)):
        print(l3[::-1])



reverse5("hello ahmed 8anam 3aml aeh uy")       

