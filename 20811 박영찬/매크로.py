a=input()
for i in range(0,int(a),1):
    a,b,c,d,e,f=input().split()
    if a==d and e==b and c==f:
        print(-1)
    elif a==d and e==b:
        print(0)
    else:
        xk = (2*int(b)*(int(d)**2 - int(f)**2)**1/2)**2 - 4*(2*(int(d) - int(a)))*((int(a) - int(d))*(int(a) + int(d)) + (int(e) + int(c))*(int(e) - int(c)))
        if xk >0:
            k=2
        if  xk == 0:
            k=1
        if xk<0 :
            k=0
        print(k)