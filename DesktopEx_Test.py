p1 = 1111
p2 = 2222.
x  = -1

if (x != p1):
    x = int(input())
    for i in range(0,min(len(p1),len(p2),len(x))):
        if x[i] == p1[i]:
            print("run at p1 program") #p1 Desktop
        elif x[i] == p2[i]:
            print("run at p2 program") #p2 Desktop
        else :
            print("Your password isn't correct please try again") #Wrong password
