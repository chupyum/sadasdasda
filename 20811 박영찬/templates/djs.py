num = 1234567897654123214112333333
k=[]
digit_count = len(str(num))
dia = len(str(num))

while(digit_count>4):
    o=4
    print(num)
    di=format(num/10**(o))
    print(di)
    j=int(di)*10**(o)
    
    k.append(num-j)
    digit_count=digit_count-4
    print(k)
    print(j)
    num=int((num-(num-j))/10**(o))
    print(num)

if(digit_count<=4):
    k.append(num)
    print(k)
s=int(dia/4)
ui=dia/4
print(ui)
if(ui<=1):
    print("%d"%(k[0]))
if(ui>1 and ui<=2):
    print("%d만%d"%(k[1],k[0]))
if(ui>2 and ui<=3):
    print("%d억%d만%d"%(k[s],k[1],k[0]))
if(ui>3 and ui<=4):
    print("%d조%d억%d만%d" %(k[3],k[2],k[1],k[0]))
if(ui>4 and ui<=5):
    print("%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0]))
if(ui>5 and ui<=6):
    print("%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0]))
if(ui>6 and ui<=7):
    print("%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0]))
if(ui>7 and ui<=8):
    print("%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0]))



    


