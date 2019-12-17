from itertools import permutations 

def check(unique):
    str1=[]
    final=[]
    for i in unique:
        flag = 0
        str1.extend([char for char in i])
        print(str1)
        for j in range(0,len(str1)):
            if (str1[j]=='('):
                flag+=1
            else:
                flag-=1
            print(flag)
            if(flag==-1):
                break
        else:
            final.append(''.join(str1))
                
            print("after{}" .format(flag))
        str1=[]
    print(final)

def print_brackets(list1):
    unique_list = []
    for j in list1:
        if j not in unique_list:
            unique_list.append(j)        
    #print(unique_list)
    check(unique_list)

def brackets(list2):
    perm = permutations(list2) 
    list1 = []
    #print (perm) 
    for i in list(perm): 
        str = ''.join(i)
        
        list1.append('('+str+')')
    #print(list1)
    print_brackets(list1)

def generate_brackets(n):
    list2 = []
    for i in range(1,n):
        list2.append('(')
    for i in range(1,n):
        list2.append(')')
    #print (list2)
    brackets(list2)


n = int(input("Enter number:"))

generate_brackets(n)