def check(unique):
    str1=[]
    final=[]
    for i in unique:
        flag = 0
        str1.extend([char for char in i])
        for j in range(0,len(str1)):
            if (str1[j]=='('):
                flag+=1
            else:
                flag-=1
            if(flag==-1):
                break
        else:
            final.append(''.join(str1))
        str1=[]
    print(final)
    
list1 = ['((()))', '(()())', '(())()', '()(())', '()()()', '())(()']

check(list1)
    
