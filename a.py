import sys
non_terminal=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
op=("+","-","/","*","^","(",")")
x=("|")
n=int(input("Enter the number of terminal :- "))
b=""
a=""
for i in range(n):
    s=input("Enter the starting terminal :- ")
    p=input("Enter the production  :- ")
    grammer=("grammer is "+s+ "->" +p)
    print(grammer)
    b=b+s+"`->"
    a=a+s+"->"
    p=p.split("|")
    #if(p!=x):
    #p.append("ϵ")
    print(p)
    for z in p:
        if s[0]==z[0]:            
            f=("1st production is :-"+s+"->"+z[1]+""+s+"`")
            print(f)
            s1=("2nd production is :-"+s+"`->"+z[1:]+""+s+"`|"+"ϵ")
            print(s1)
            b=b+z[1:]+""+s+"`|"
            a=a+z[1]+""+s+"`|"
        else:
            b=b+z+"|"
            a=a+z+"|"
            print("Grammer is not recursive")
    b=b+"ϵ"
    print(a[:-1])
    print(b)
    b=""
    if s in non_terminal:
        print("Grammer is incorrect")
    elif s[0]==p[0]:
        print("It Is Recursive")
    elif p[0] in op:
        print("Grammer is not recursive")
    else:
        print("Solve")