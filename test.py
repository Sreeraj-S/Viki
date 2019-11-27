d1,d2,d3,d4,d5,d6,d7,d8=0,0,0,0,0,0,0,0

ch=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
total=''
while True:
    di=[d8,d7,d6,d5,d4,d3,d2,d1]
    n=0
    for i in range(8):
        total+=ch[di[i]]
    print(total)
    total=''
    if d1==61 and d2==61 and d3==61 and d4==61 and d5==61 and d6==61 and d7==61 and d8==61:
        break
    elif d1==61 and d2==61 and d3==61 and d4==61 and d5==61 and d6==61 and d7==61:
        d1,d2,d3,d4,d5,d6,d7=0,0,0,0,0,0,0
        d8+=1
        n=1
        #print('j')
    elif d1==61 and d2==61 and d3==61 and d4==61 and d5==61 and d6==61:
        d1,d2,d3,d4,d5,d6=0,0,0,0,0,0
        d7+=1
        n=1
        #print('l')
    elif d1==61 and d2==61 and d3==61 and d4==61 and d5==61:
        d1,d2,d3,d4,d5=0,0,0,0,0
        d6+=1
        n=1
        #print('m')
    elif d1==61 and d2==61 and d3==61 and d4==61:
        d1,d2,d3,d4=0,0,0,0
        d5+=1
        n=1
        #print('f')
    elif d1==61 and d2==61 and d3==61:
        d1,d2,d3=0,0,0
        d4+=1
        n=1
        #print('g')
    elif d1==61 and d2==61:
        d1,d2=0,0
        d3+=1
        n=1
        #print('q')
    elif d1==61:
        d1=0
        d2+=1
        n=1
        #print('v')
    if n==0:
        d1+=1
    